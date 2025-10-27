import matplotlib.pyplot as plt
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

for article_num in [1, 2, 3]:
    with open(f'../data/article{article_num}.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]

    sentiments = []

    for line in lines:
        scores = analyzer.polarity_scores(line)
        sentiments.append({
            'Text': line,
            'Negative': scores['neg'],
            'Neutral': scores['neu'],
            'Positive': scores['pos'],
            'Compound': scores['compound']  # overall sentiment score (-1 to +1)
        })

    df = pd.DataFrame(sentiments)

    print(f"\n=== Article {article_num} Sentiment Summary ===")
    print(df.head())

    plt.figure(figsize=(8, 4))
    plt.plot(df['Compound'], marker='o')
    plt.title(f'Article {article_num} Sentiment Trend')
    plt.xlabel('Line Number')
    plt.ylabel('Compound Sentiment Score')
    plt.grid(True)
    plt.show()
