import streamlit as st

st.title("मेरा खुद का AI चैटबॉट 🤖")
st.write("नमस्ते! मैं आपका अपना बनाया हुआ AI हूँ। मुझसे कुछ भी पूछिए!")

# चैट का इतिहास याद रखने के लिए
if "messages" not in st.session_state:
    st.session_state.messages = []

# पुरानी चैट स्क्रीन पर दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# यूजर से इनपुट लेना
if user_query := st.chat_input("यहाँ अपना सवाल लिखें..."):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # एआई का जवाब तय करना
    query_lower = user_query.lower()
    if "kaise ho" in query_lower:
        ai_reply = "मैं एकदम बढ़िया हूँ! आप बताइए।"
    elif "tumhara naam kya hai" in query_lower:
        ai_reply = "मेरा नाम आपका अपना बनाया हुआ AI है!"
    elif "bye" in query_lower or "exit" in query_lower:
        ai_reply = "अलविदा! फिर मिलेंगे।"
    else:
        ai_reply = f"wah! आपने पूछा: '{user_query}', लेकिन मैं अभी धीरे-धीरे सीख रहा हूँ!"

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.markdown(ai_reply)