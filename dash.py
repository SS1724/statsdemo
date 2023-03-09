import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Irish Dashboard')
df=pd.read_csv('iris.csv')
st.dataframe(df)
col1,col2 = st.columns(2)

st.line_chart(df['sepal_length'])
st.bar_chart(df['species'])
st.header('sepal length and sepal width')
st.area_chart(df['species'])
st.header("Line chart")
st.line_chart(df.iloc[:,:-1])
st.bar_chart(df['sepal_length','sepal_width','petal_length','petal_width'])
# fig,ax=plt.subplot()
# ax.scatter(df.iloc[:,0],df.iloc[:,1])
# plt.scatter(df.iloc[:,2],df.iloc[:,3])
# st.pyplot(fig)