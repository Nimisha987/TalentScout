import streamlit as st
from chatbot.flow import ChatFlow

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Page config
st.set_page_config(
    page_title="TalentScout – AI Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.markdown("<h1 style='text-align: center;'>TalentScout – AI Hiring Assistant</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Smart candidate screening powered by AI</div>", unsafe_allow_html=True)

# Initialize session state FIRST
if "chatflow" not in st.session_state:
    st.session_state.chatflow = ChatFlow()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Auto welcome message
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Welcome to TalentScout! I’ll guide you through a short screening process. Let’s begin"
    })

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Bot reply
    reply = st.session_state.chatflow.process(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()
