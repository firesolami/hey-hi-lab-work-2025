from collections import Counter
import matplotlib.pyplot as plt
text = """Artificial Intelligence (AI) is changing the way we live and work. AI helps in language translation, chatbots, and data analysis."""

lower_case_text = text.lower()
cleaned_text = ""

for char in lower_case_text:
    if char in "(),.":
        continue
    cleaned_text += char

print(cleaned_text)

tokens = cleaned_text.split()

print(tokens)

stopwords = ["and", "is", "in", "the", "we", "of", "a"]

filtered_tokens = [word for word in tokens if word not in stopwords]

print(filtered_tokens)

freq = Counter(filtered_tokens)

print(freq)

most_common = freq.most_common(5)
words = [w for w, c in most_common]
counts = [c for w, c in most_common]

plt.bar(words, counts)
plt.title("Top 5 Words in Text")
plt.show()
