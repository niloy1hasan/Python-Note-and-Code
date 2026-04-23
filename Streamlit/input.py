import streamlit as st
st.title("Create an Account", anchor=False)
name = st.text_input("Your Name:", value=None, placeholder="Enter your name")
age = st.number_input("Your Age:", value=None, placeholder="Enter your age")
email = st.text_input("Your Email:", value=None, placeholder="Enter your Email")
password = st.text_input("Your Password:", value=None, placeholder="Enter your Password", type="password")



if st.button("Create Account", width="stretch", type="primary"):
    st.write(f"Hello, {name}! You are {age} years old.")
