import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# con write metemos markdown en la app para que se vea
st.write("""
# Simple Iris Flower Prediction App

This app predicts the **Iris flower** type.
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    """
    Funcion de lectura d elos inputs desde los widgets del 
    sidebar
    """
    sepal_length = st.sidebar.slider("Sepal length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("Sepal width", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("Petal length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("Petal width", 0.1, 2.5, 0.2)

    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    features = pd.DataFrame(data, index = [0])

    return features


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)
# en este ejemplo se reentrena el modelo cada vez 
# que se cambian los inputs
iris = datasets.load_iris()
X = iris.data
y = iris.target

clf = RandomForestClassifier()
clf.fit(X, y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Prediction')
st.write(iris.target_names[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)