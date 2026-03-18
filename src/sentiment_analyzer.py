from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    
    Parameters:
    text (str): The input text to analyze.
    
    Returns:
    dict: Sentiment Label and confidence score
    """

    result = sentiment_pipeline(text)

    return result[0]


     
    