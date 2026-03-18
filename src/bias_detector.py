from transformers import pipeline

bias_classifier = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

label_map = {
    "LABEL_0": "Negative Bias",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive Bias"
}

def detect_bias(text):

    result = bias_classifier(text)[0]

    label = label_map.get(result["label"], result["label"])

    return {
        "label": label,
        "score": result["score"]
    }