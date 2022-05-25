import streamlit as st
st.title("Basic Calculator")
st.write("Performs Addition")
a= st.number_input("Enter the first number")
b= st.number_input("Enter the second number")
cal=a+b
st.title(f"The sum of {a} and {b} is {cal}")
