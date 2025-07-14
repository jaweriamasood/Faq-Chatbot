import streamlit as st
from chatbot import get_faq_response

st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask any question related to our product or service.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your question", key="input")

if st.button("Ask") and user_input:
    response = get_faq_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history:
    icon = "🧑" if sender == "You" else "🤖"
    st.markdown(f"**{icon} {sender}:** {message}")
