from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

texts = [
    "I really enjoyed learning pythone today!",
    "I am disappointed with the results.",
    "The weather is cloudy today."
]

for text in texts:
    result = sentiment_analyzer(text)
    print("Input text:",text)
    print(" Model's Output:", result)