# https://github.com/amaljpc/educhat.git
import streamlit as st
from gpt4free import you
# simple request with links and details
def fetch(content):
    response = ""
    try:
        response = you.Completion.create(prompt=content,detailed=True,include_links=True, )
    except Exception as e:
        print(e)
    if response:
        return response.text
    else:
        return "Try again, Server busy"



# Set the page title
st.set_page_config(page_title="EduChat")

# Create a sidebar with some information about your chatbot
with st.sidebar:
    st.title("EduChat")
    st.write("Educational search only")

# App layout
st.markdown("<h2>Prompt Responsibly!</h2>", unsafe_allow_html=True)


    
# Human user input
user_input = st.text_area(label="prompt",placeholder="Enter your prompt here",label_visibility="hidden")

# Bot response output
if user_input:
    # session_state.user_input = user_input
    bot_response = fetch(user_input)
    print(bot_response)
    st.write("", bot_response)

