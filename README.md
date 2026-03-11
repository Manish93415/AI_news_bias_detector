# AI News Bias Detector

## Overview

The **AI News Bias Detector** is a Natural Language Processing (NLP) project that analyzes news articles and provides insights about their tone, sentiment, and potential bias. The application allows users to paste a news article and receive automated analysis including sentiment detection and a concise summary.

This project demonstrates how transformer-based models from Hugging Face can be used to build practical AI-powered applications.

---

## Problem Statement

In today's digital world, people consume news from many different online sources. However, not all news articles are neutral. Some articles may contain political or emotional bias that can influence readers.

The goal of this project is to build an AI-powered system that analyzes news articles and helps users understand the tone and sentiment of the content.

---

## Features

- **Sentiment Analysis**
  Detects whether the tone of the article is positive, negative, or neutral.

- **Bias Detection**
  Attempts to detect potential bias in the news article.

- **Article Summarization**
  Generates a short summary of long news articles.

- **Interactive Interface**
  Allows users to paste a news article and instantly receive analysis results.

---

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Gradio
- Natural Language Processing (NLP)

---

## Project Structure

```
ai-news-bias-detector
│
├── app
│   └── app.py
│
├── src
│   ├── bias_detector.py
│   ├── sentiment_analyzer.py
│   ├── summarizer.py
│   └── utils.py
│
├── notebooks
│   └── experimentation.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

1. User enters a news article.
2. The system processes the text using NLP models.
3. The models analyze sentiment and generate a summary.
4. Results are displayed through an interactive interface.

---

## Future Improvements

- Improve bias detection accuracy
- Add fake news detection
- Support multiple languages
- Add result visualizations
- Deploy the application publicly

---

## Learning Outcomes

This project helps developers learn:

- Hugging Face Transformers
- NLP pipelines
- Model inference
- Building ML-powered web applications
- Deploying AI applications

---

## Author

**Manish Singh**
