import streamlit as st
st.title("Select an option:")

selected = st.selectbox("Choose Your Profession:",
             ("Student", "Employee", "Businessman"), index=None,
             accept_new_options = True)

if selected:
    st.write("You select", selected)
