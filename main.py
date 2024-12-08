import openai

openai.api_key ="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"
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()


#from langchain_openai import ChatOpenAI
#chat_model = ChatOpenAI()

#subject = "AI"
#result = chat_model.invoke(subject + "에 대한 시를 써줘")
#print(result.content)

import streamlit as st

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중......."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)