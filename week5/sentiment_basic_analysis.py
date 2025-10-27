from textblob import TextBlob

sentences = [
    "I love studying Artificial Intelligence!",
    "This project is really difficult and frustrating.",
    "The movie was okay, not great but not terrible either.",
    "Our AI model performed exceptionally well on the dataset!",
    "I hate when my code doesn't run.",
    "Hitler and the work of the Nazis"
]

for text in sentences:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(f"Text: {text}")
    print(f"Sentiment Score: {sentiment}")
    if sentiment > 0:
        print("-> Positive :)\n")
    elif sentiment < 0:
        print("-> Negative :(\n")
    else:
        print("-> Neutral :|\n")