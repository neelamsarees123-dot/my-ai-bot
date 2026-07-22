import streamlit as st

# पेज की सेटिंग
st.set_page_config(page_title="Deepak AI Pro", page_icon="🤖", layout="centered")

st.title("🤖 Deepak AI Pro")
st.write("नमस्ते! मैं आपका अपना स्मार्ट एआई हूँ। मुझसे कुछ भी पूछिए!")

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

    # सवाल को छोटा करके चेक करना ताकि आसानी से समझ आ जाए
    user_query = prompt.lower().strip()

    # एआई के फिक्स और स्मार्ट जवाब
    if "hi" in user_query or "hello" in user_query or "हाए" in user_query or "नमस्ते" in user_query:
        response = "हाँ बिल्कुल मैं आपके लिए तैयार हूँ!"
    elif "your name" in user_query or "naam" in user_query or "तुम्हारा नाम" in user_query or "तेरा नाम" in user_query:
        response = "मेरा नाम दीपक एआई प्रो है।"
    elif "prime minister" in user_query or "pm of india" in user_query or "भारत के प्रधानमंत्री" in user_query or "प्रधानमंत्री कौन है" in user_query:
        response = "भारत के वर्तमान प्रधानमंत्री श्री नरेंद्र मोदी हैं।"
    elif "kaise ho" in user_query or "كيف حالك" in user_query or "कैसे हो" in user_query:
        response = "मैं एकदम बढ़िया हूँ! बताइए आज मैं आपकी क्या मदद कर सकता हूँ?"
    else:
        # अगर कोई दूसरा सवाल पूछे तो उसके लिए जनरल जवाब
        response = f"आपने बहुत अच्छा सवाल पूछा है: '{prompt}'। दीपक एआई प्रो इस पर काम कर रहा है, और बहुत जल्द आपको इसकी पूरी जानकारी मिल जाएगी!"

    # एआई का जवाब दिखाना
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # एआई का जवाब सेव करना
    st.session_state.messages.append({"role": "