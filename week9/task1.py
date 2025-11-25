import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("student_scores.csv")
df.head()

plt.scatter(df['hours'], df['score'])
plt.xlabel('Hours Studied')
plt.ylabel('Scores Obtained')
plt.title('Hours Studied vs Scores Obtained')
# plt.show()

X = df[['hours']]
y = df['score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

r2 = r2_score(y_test, y_pred)
print(f"R^2 Score: {r2}")

slope = model.coef_[0]
intercept = model.intercept_

print(f"Regression Line: score = {slope} * hours + {intercept}")

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), linewidth=3, color='red')
plt.xlabel('Hours Studied')
plt.ylabel('Scores Obtained')
plt.title('Regression Line: Hours Studied vs Scores Obtained')
# plt.show()

hours = [[7.5]]
predicted_score = model.predict(hours)
print("Predicted Score", predicted_score[0])