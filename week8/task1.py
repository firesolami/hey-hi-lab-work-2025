import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

print("Features:", iris.feature_names)
print("Target names:", iris.target_names)
print("Shape of data:", X.shape)

df = pd.DataFrame(data=X, columns=iris.feature_names)
sns.pairplot(df, hue='species')
plt.show()  

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))