import streamlit as st
#pip install groq
from groq import Groq

#api
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.title("Summarize")

text = st.text_area("Write your text", height=200)

if st.button("Summarize"):
    if len(text.split()) < 10:
        st.warning("text is too short") 
    else:
        with st.spinner("Summarizing..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[{"role" : "system", "content" : "You are a helpful assistant, summarize this text in 3 or 4 "
                "sentences in the same language"} , {"role" : "user" , "content" : text}]
            )
        st.success(response.choices[0].message.content) 