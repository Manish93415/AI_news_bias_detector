from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_article(text):

    # If text is short, return it directly
    if len(text.split()) < 40:
        return text

    inputs = tokenizer(
        "summarize: " + text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=80,
        min_length=20,
        num_beams=4,
        repetition_penalty=2.5,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary