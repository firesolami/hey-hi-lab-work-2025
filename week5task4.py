from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

with open('article1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines if line.strip()]

print("Sample lines:")
print(lines[:5])

sentiments = []

for line in lines:
    blob = TextBlob(line)
    polarity = blob.sentiment.polarity # -1 (negative) -> +1 (positive)
    subjectivity = blob.sentiment.subjectivity # 0 (objective) -> 1 (subjective)
    sentiments.append({'Text': line, 'Polarity': polarity, 'Subjectivity': subjectivity})

df = pd.DataFrame(sentiments)
print(df.head())