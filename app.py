import streamlit as st
from openai import OpenAI

f = open("key.txt")
OPENAI_API_KEY = f.read()

st.title("Code Reviewer")
st.subheader("Welcome to Code Reviewer")

client = OpenAI(api_key=OPENAI_API_KEY)

prompt = st.text_area("Enter your Code")

if st.button("Generate"):
    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code with comments. You can also provide alternative better code"},
        {"role": "user", "content": prompt}
      ]
    )
