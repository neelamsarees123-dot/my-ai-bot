import streamlit as st

st.set_page_config(page_title="Deepak AI Pro", page_icon="🤖")

st.title("🤖 Deepak AI Pro")
st.write("नमस्ते! मैं आपका अपना स्मार्ट एआई हूँ। मुझसे कुछ भी पूछिए!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    user_query = prompt.lower().strip()

    if "hi" in user_query or "hello" in user_query or "हाए" in user_query or "नमस्ते" in user_query:
        response = "हाँ बिल्कुल मैं आपके लिए तैयार हूँ!"
    elif "your name" in user_query or "naam" in user_query or "नाम" in user_query:
        response = "मेरा नाम दीपक एआई प्रो है।"
    elif "prime minister" in user_query or "pm" in user_query or "प्रधानमंत्री" in user_query:
        response = "भारत के वर्तमान प्रधानमंत्री श्री नरेंद्र मोदी हैं।"
    elif "kaise ho" in user_query or "कैसे हो" in user_query:
        response = "मैं एकदम बढ़िया हूँ! बताइए आज मैं आपकी क्या मदद कर सकता हूँ?"
    else:
        response = f"आपने बहुत अच्छा सवाल पूछा है: '{prompt}'। दीपक इस पर काम कर रहा है!"

    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.messages.append
