import streamlit as st


st.title("Welcome to Streamlit!")

name = st.text_input("Enter your name")

if st.button("Greet Me"):
    if name.strip():
        st.write(f"Hello, {name.strip()}!")
    else:
        st.write("Hello! Please enter your name.")
