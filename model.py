import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("data.csv")

# Independent variable
X = data[['Hours']]

# Dependent variable
y = data['Marks']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Print predictions
print("Predicted Marks:")
print(predictions)

#Accuracy score
score = r2_score(y_test, predictions)

print("Accuracy:", score)

# Plot graph
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

# User input prediction
hours = float(input("Enter study hours: "))

predicted_marks = model.predict([[hours]])

print(f"Predicted Marks: {predicted_marks[0]:.2f}")