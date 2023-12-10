# from openai import OpenAI
# import streamlit as st

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# st.title("💬 Chatbot")
# st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()

#     client = OpenAI(api_key=openai_api_key)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)

# from openai import OpenAI
# import streamlit as st
# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
# st.title(":speech_balloon: Chatbot")
# st.caption(":rocket: A streamlit chatbot powered by OpenAI LLM")
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])
# if prompt := st.chat_input():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()
#     client = OpenAI(api_key=openai_api_key)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-4", messages=st.session_state.messages)
#     msg = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)
import openai
import streamlit as st
# Sidebar for API key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
    st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)")
    st.markdown("[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)")
# Title and caption for the Streamlit app
st.title(":speech_balloon: Foodie and Tourist Guide Chatbot")
st.caption(":rocket: A Streamlit chatbot powered by OpenAI LLM")
# Initialize session state for storing messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you today?"}]
# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Define the system prompt
    system_prompt = """
        As an expert foodie and tourist guide with comprehensive knowledge of restaurant locations, event schedules, and geographical expertise, your task is to provide personalized recommendations. Use live data from APIs like Yelp and SeatGeek for real-time event and dining suggestions.
        Procedure:
        1. Ask the user, What are three activities that you enjoy the most?
        2. Based on the response, ask, What can I help you with today?
        3. Use the user's response to fetch relevant events from SeatGeek and dining options from Yelp that fit the user's preferences, location, and specified time.
        4. Prioritize suggestions that are geographically convenient and suitable for walking, driving, or public transportation.
        5. Adapt recommendations based on the user's past interactions and preferences.
        6. If no suitable event or restaurant is found, respond with a respective fallback message.
    """

chat_history = [
        {"role": "system", "content": system_prompt},
    ]

# User input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    client = openai.OpenAI(api_key=openai_api_key)
    # # Define the system prompt
    # system_prompt = """
    #     As an expert foodie and tourist guide with comprehensive knowledge of restaurant locations, event schedules, and geographical expertise, your task is to provide personalized recommendations. Use live data from APIs like Yelp and SeatGeek for real-time event and dining suggestions.
    #     Procedure:
    #     1. Ask the user, What are three activities that you enjoy the most?
    #     2. Based on the response, ask, What can I help you with today?
    #     3. Use the user's response to fetch relevant events from SeatGeek and dining options from Yelp that fit the user's preferences, location, and specified time.
    #     4. Prioritize suggestions that are geographically convenient and suitable for walking, driving, or public transportation.
    #     5. Adapt recommendations based on the user's past interactions and preferences.
    #     6. If no suitable event or restaurant is found, respond with a respective fallback message.
    # """
    # Combine system prompt with user's latest message
    # full_prompt = system_prompt + f"\nUser's request: {prompt}\n"
    # # Get response from OpenAI
    # chat_history = [
    #     {"role": "system", "content": system_prompt},
    #     {"role": "user", "content": prompt},
    # ]
    chat_history.append({"role": "user", "content": prompt})
    # chat_history.append({"role": "assistant", "content": msg})
    response = client.chat.completions.create(model="gpt-4", messages=chat_history)
    msg = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": msg})

    # Update session state with the new messages
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": msg})
    # Display the new messages
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write(msg)
