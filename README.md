# Student Marks Predictor

A beginner Machine Learning project that predicts student marks based on study hours using Linear Regression.

---

## 📌 Project Overview

This project uses a Linear Regression model to predict marks from the number of study hours.

It helps beginners understand:
- Data preprocessing
- Machine Learning workflow
- Linear Regression
- Data visualization
- Model evaluation

---

## 🚀 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 📂 Project Structure

student-marks-predictor/
│
├── data.csv
├── model.py
├── app.py
├── requirements.txt
└── README.md

---

## 📊 Dataset

Example dataset:

| Study Hours | Marks |
|-------------|-------|
| 1 | 15 |
| 2 | 20 |
| 3 | 35 |
| 4 | 40 |
| 5 | 50 |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/student-marks-predictor.git
Move into project folder:

cd student-marks-predictor
Install dependencies:

pip install -r requirements.txt
▶️ Run the Project
python model.py
For Streamlit app:

streamlit run app.py
📈 Machine Learning Concept
This project uses Linear Regression.

Linear Regression equation:

y = mx + b

Where:

y = predicted marks

x = study hours

m = slope

b = intercept

📉 Accuracy Evaluation
The model uses R² Score for evaluation.

Example:

from sklearn.metrics import r2_score

score = r2_score(y_test, predictions)

print(score)
📷 Output
Example prediction:

Enter study hours: 7
Predicted Marks: 69.52
🔥 Future Improvements

Add larger dataset
Predict performance using:
Attendance
Sleep hours
Assignment completion
Deploy project online
Add GUI using Streamlit

💡 Skills Learned
Python Programming
Data Analysis
Machine Learning Basics
Linear Regression
Model Training
Data Visualization

👨‍💻 Author
Aaryan Patil
Diploma in Artificial Intelligence and Machine Learning

📚 References
Scikit-learn Documentation

Pandas Documentation

Matplotlib Documentation