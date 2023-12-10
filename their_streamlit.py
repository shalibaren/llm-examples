import asyncio
import os

import openai
import streamlit as st
# from dotenv import load_dotenv
import streamlit as st

# No need for load_dotenv() or os.getenv()
openai.api_key = st.secrets["openai_api_key"]

from aiconfig import AIConfigRuntime

load_dotenv()
openai.api_key = os.getenv("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")


# Get assistant response based on user prompt (prompt routing)
async def assistant_response(prompt):
    config = AIConfigRuntime.load("assistant_aiconfig.json")

    params = {"student_question": prompt}

    await config.run("router", params)
    topic = config.get_output_text("router")

    dest_prompt = topic.lower()

    await config.run(dest_prompt, params)
    response = config.get_output_text(dest_prompt)

    return response


# Streamlit Setup
st.title("LocaLLM")
st.markdown(
    "Ask a math, physics, or general question. Based on your question, an AI math prof, physics prof, or general assistant will respond."
)
st.markdown(
    "**This is a simple demo of prompt routing - based on your question, an LLM decides which AI teacher responds.**"
)

# Chat setup
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a math, physics, or general question"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    chat_response = asyncio.run(assistant_response(prompt))

    response = f"AI: {chat_response}"

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})