import streamlit as st

# Page config
st.set_page_config(
    page_title="AI Health FAQ Chatbot",
    page_icon="💬",
    layout="centered"
)

st.title("🩺 AI Health FAQ Chatbot")
st.write("Ask simple health-related questions")

# Simple FAQ database
faq = {
    "fever": "Fever is a temporary increase in body temperature. Drink fluids and rest. See a doctor if it lasts more than 2 days.",
    "cold": "Common cold causes runny nose and sneezing. Rest and warm fluids help.",
    "headache": "Headache can be due to stress or dehydration. Drink water and rest.",
    "cough": "Cough may be due to cold or allergy. Warm water and honey may help.",
    "covid": "COVID-19 symptoms include fever, cough, and breathing issues. Get tested if symptoms appear.",
    "diabetes": "Diabetes is a condition where blood sugar levels are high. Regular checkups are important.",
    "bp": "High blood pressure can cause heart problems. Reduce salt and stress."
}

# User input
user_input = st.text_input("Enter your health question:")

if user_input:
    found = False
    for key in faq:
        if key in user_input.lower():
            st.success(faq[key])
            found = True
            break

    if not found:
        st.warning("Sorry, I can answer only basic health FAQs. Please consult a doctor.")

st.markdown("---")
st.caption("⚠️ This chatbot provides basic information only. Not a medical diagnosis.")
