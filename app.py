import gradio as gr

from src.sentiment_analyzer import analyze_sentiment
from src.summarizer import summarize_article
from src.bias_detector import detect_bias


def analyze_news(article):
    try:
        article = article[:1500]

        sentiment = analyze_sentiment(article)
        bias = detect_bias(article)
        summary = summarize_article(article)

        print("DEBUG:", sentiment, bias)   # 👈 ADD THIS

        sentiment_text = f"{sentiment['label']} ({round(sentiment['score']*100,2)}%)"
        bias_text = f"{bias['label']} ({round(bias['score']*100,2)}%)"

        return sentiment_text, bias_text, summary

    except Exception as e:
        print("ERROR:", str(e))   # 👈 VERY IMPORTANT
        return "Error", "Error", "Something went wrong"
    

def get_color(label):
    if "POSITIVE" in label:
        return "green"
    elif "NEGATIVE" in label:
        return "red"
    else:
        return "orange"

def analyze_news_ui(article):
    try:
        sentiment, bias, summary = analyze_news(article)

        sentiment_color = get_color(sentiment)
        bias_color = get_color(bias)

        sentiment_html = f"""
        <div style='padding:10px'>
            <h4>📊 Sentiment</h4>
            <div style='color:{sentiment_color}; font-weight:bold; font-size:18px'>
                {sentiment}
            </div>
        </div>
        """

        bias_html = f"""
        <div style='padding:10px'>
            <h4>⚖️ Bias</h4>
            <div style='color:{bias_color}; font-weight:bold; font-size:18px'>
                {bias}
            </div>
        </div>
        """

        return sentiment_html, bias_html, summary

    except Exception as e:
        return f"<b>Error:</b> {str(e)}", "<b>Error</b>", "Check logs"

with gr.Blocks(theme=gr.themes.Soft(), css="""
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}
.gradio-container {
    font-family: 'Segoe UI', sans-serif;
}
""") as demo:

    gr.Markdown("# 🚀 AI News Bias Detector")
    gr.Markdown("### 🧠 Analyze sentiment, bias & summary instantly")

    with gr.Group():
        article_input = gr.Textbox(
            lines=8,
            placeholder="📰 Paste your news article here...",
            label="Article"
        )

    with gr.Row():
        sentiment_output = gr.HTML(label="Sentiment")
        bias_output = gr.HTML(label="Bias")

    summary_output = gr.Textbox(label="📄 Summary", lines=4)

    with gr.Row():
        analyze_btn = gr.Button("🔍 Analyze", variant="primary")
        clear_btn = gr.Button("🧹 Clear")

    analyze_btn.click(
        fn=analyze_news_ui,
        inputs=article_input,
        outputs=[sentiment_output, bias_output, summary_output],
        show_progress=True   
    )

    clear_btn.click(
        fn=lambda: ("", "", ""),
        outputs=[article_input, sentiment_output, bias_output, summary_output]
    )

demo.launch()