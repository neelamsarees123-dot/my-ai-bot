import streamlit as st

# पेज की सेटिंग
st.set_page_config(page_title="My AI Assistant", page_icon="🤖")

st.title("🤖 My AI Assistant")
st.write("नमस्ते! बताइए, आज मैं आपकी क्या मदद कर सकता हूँ?")

# चैट हिस्ट्री के लिए
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुरानी चैट दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# यूजर से इनपुट लेना
if prompt := st.chat_input("यहाँ अपना सवाल लिखें..."):
    # यूजर का मैसेज जोड़ना
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # एआई का जवाब
    response = f"आपने कहा: '{prompt}'। यह एआई ऐप अब बिल्कुल तैयार और लाइव है!"
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # एआई का जवाब सेव करना
    st.session_state.messages.append({"role": "assistant", "content": response})