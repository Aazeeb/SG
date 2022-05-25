import pandas as pd
import streamlit as st
table=pd.read_html('https://en.wikipedia.org/wiki/Iris_flower_data_set')
df=table[0]
X=df.iloc[:,1:5]
y=df.iloc[:,5]
from sklearn.svm import SVC
clf=SVC(kernel='linear')
clf.fit(X,y)
Sepal_length=st.slider('Sepal_length',0.1,8.0)
Sepal_width=st.slider('Sepal_width',0.1,5.0)
Petal_length=st.slider('Petal_length',0.1,8.0)
Petal_width=st.slider('Petal_width',0.1,5.0)

if st.button("PREDICT"):
    y_pred=clf.predict([[Sepal_length,Sepal_width,Petal_length,Petal_width]])[0][3:]
    st.title(y_pred)
    

