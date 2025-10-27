from textblob import TextBlob

print("=== Mini polarity Analyzer ===")
print("Type 'exit' to quit.\n")

while True:
    text = input("Enter a sentence or paragraph.\n")
    
    if text.lower() == 'exit':
        print("Goodbye!")
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    print(f"Polarity Score: {polarity:.2f}")
    if polarity > 0:
        print("-> Positive :)\n")
    elif polarity < 0:
        print("-> Negative :(\n")
    else:
        print("-> Neutral :|\n")