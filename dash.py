import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px 
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\Z BOOK\\Documents\\Machine Learning\\Titanic-Dataset.csv')
#-----------------------------------------------------------------------------------------
st.sidebar.header("Titanic Survival Analysis")
st.sidebar.image("undefined.jpeg")
st.sidebar.markdown("Made with by Roodina sobeh")
data['Age'].fillna(data['Age'].median(), inplace=True) 
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True) 
data['Survived_Status'] = data['Survived'].map({0: 'Not Survive', 1: 'Survived'})
#---------------------------------------------------------------------------------
st.sidebar.subheader(" Dynamic Filters :")
survival_status = st.sidebar.selectbox(
    '1. Filter by Survival Status:',
    options=['All', 'Survived', 'Did Not Survive']
)
#-------------------------------------------------
gender_filter = st.sidebar.selectbox(
    '2. Filter by Gender:',
    options=['All', 'male', 'female']
)
#-----------------------------------------------
min_age = int(data['Age'].min())
max_age = int(data['Age'].max())
age_range = st.sidebar.slider(
    '3. Filter by Age Range:',
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age)
)
#---------------------------------------------------------------
filtered_data = data.copy()

if survival_status != 'All':
    filtered_data = filtered_data[filtered_data['Survived_Status'] == survival_status]
if gender_filter != 'All':
    filtered_data = filtered_data[filtered_data['Sex'] == gender_filter]

filtered_data = filtered_data[
    (filtered_data['Age'] >= age_range[0]) & 
    (filtered_data['Age'] <= age_range[1])
]
#-----------------------------------------------------
st.title("Titanic Dashboard: Exploratory Data Analysis")
#------------------------------------------------------
st.subheader("1. Age Distribution")
fig_hist, ax_hist = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_data, x='Age', bins=20, kde=True, ax=ax_hist, color='skyblue')
st.pyplot(fig_hist) 
#---------------------------------------------------
st.subheader(" 2. Age vs. Fare Colored by Survival ")
fig_scatter = px.scatter(filtered_data,
                         x='Age', 
                         y='Fare', 
                         color='Survived_Status', 
                         hover_data=['Pclass', 'Sex'],
                         title='Relationship between Age and Fare'
)
st.plotly_chart(fig_scatter, use_container_width=True)
#----------------------------------------------------------

import pickle
model = pickle.load(open("model.pkl", "rb"))


st.sidebar.header("Enter Passenger Details")

pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
sex = st.sidebar.selectbox("Sex", ["male", "female"])
age = st.sidebar.slider("Age", 0, 80, 25)
sibsp = st.sidebar.number_input("Siblings/Spouses Aboard", 0, 10, 0)
parch = st.sidebar.number_input("Parents/Children Aboard", 0, 10, 0)
fare = st.sidebar.slider("Fare", 0, 500, 50)
embarked = st.sidebar.selectbox("Embarked", ["C", "Q", "S"])

sex_male = 1 if sex == "male" else 0
embarked_Q = 1 if embarked == "Q" else 0
embarked_S = 1 if embarked == "S" else 0

# Create input DataFrame in same order as model training
input_data = pd.DataFrame({
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Fare_Simple': [fare],
    'Sex_male': [1 if sex == "male" else 0],
    'Embarked_Q': [1 if embarked == "Q" else 0],
    'Embarked_S': [1 if embarked == "S" else 0],
    'Pclass': [pclass]
})

if st.sidebar.button("Predict"):
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result:")
    if prediction == 1:
        st.write("The passenger would survive!")
    else:
        st.write(" The passenger would not survive.")


