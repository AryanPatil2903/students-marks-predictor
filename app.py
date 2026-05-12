import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = pd.read_csv("data.csv")

X = data[['Hours']]
y = data['Marks']

# Train model
model = LinearRegression()
model.fit(X, y)

# UI
st.title("Student Marks Predictor")

hours = st.slider("Study Hours", 1, 12)

prediction = model.predict([[hours]])

st.write(f"Predicted Marks: {prediction[0]:.2f}")