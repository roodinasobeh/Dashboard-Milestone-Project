# 🚢 Titanic Interactive Dashboard (EDA + Prediction)

### 📌 Project Overview
This project is an **interactive data analysis dashboard** built using **Streamlit**.  
It allows users to explore the Titanic dataset, visualize insights, and even predict passenger survival using a trained **Logistic Regression model**.

---

### 🎯 Objectives
- Perform **Exploratory Data Analysis (EDA)** on the Titanic dataset.  
- Create an **interactive dashboard** where users can:
  - Filter data dynamically (by gender, age range, survival status).
  - Visualize distributions and relationships (Age, Fare, Class, etc.).
- Integrate a **Machine Learning model** to predict whether a passenger would survive or not based on input details.

---
 ### 🧩 Dataset

Dataset used: Titanic - Machine Learning from Disaster
Available on Kaggle :https://www.kaggle.com/datasets/dimplebathija/titanic-machine-learning-from-disaster

### 🧠 Machine Learning Model
- Model used: **Logistic Regression**
- Libraries: `scikit-learn`, `pandas`, `numpy`
- Features used in training:
- The trained model was saved as `model.pkl` and integrated into the dashboard for real-time predictions.

---

### ⚙️ Technologies Used
- **Python**
- **Streamlit**
- **Pandas**
- **Seaborn**
- **Plotly Express**
- **Matplotlib**
- **Scikit-learn**
- **Pickle**

---

### 🖥️ How to Run the App
To run the dashboard locally, open your terminal and run:

```bash
streamlit run dash.py
Then open your browser at:
👉 http://localhost:8501
