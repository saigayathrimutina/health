import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Health FAQ Chatbot",
    page_icon="💬",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        font-family: Arial, sans-serif;
    }

    .card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
        margin-top: 40px;
    }

    h1 {
        text-align: center;
        color: #1b5e20;
    }

    .footer {
        text-align: center;
        font-size: 13px;
        color: gray;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- UI ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.title("🩺 AI Health FAQ Chatbot")
st.write("Ask simple health-related questions")

faq = {
    "fever": "Fever is a temporary increase in body temperature. Drink fluids and rest. See a doctor if it lasts more than 2 days.",
    "cold": "Common cold causes runny nose and sneezing. Rest and warm fluids help.",
    "headache": "Headache can be due to stress or dehydration. Drink water and rest.",
    "cough": "Cough may be due to cold or allergy. Warm water and honey may help.",
    "covid": "COVID-19 symptoms include fever, cough, and breathing issues. Get tested if symptoms appear.",
    "diabetes": "Diabetes is a condition where blood sugar levels are high. Regular checkups are important.",
    "bp": "High blood pressure can cause heart problems. Reduce salt and stress."
}

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

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='footer'>⚠️ This chatbot provides basic information only. Not a medical diagnosis.</div>",
    unsafe_allow_html=True
)
