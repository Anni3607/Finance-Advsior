os.system("pip install joblib")  # Add this at the top of app.py
import joblib
import streamlit as st
import pandas as pd
import joblib
import os


# Load trained model
model = joblib.load('finance_advisor_model.pkl')

# Page Config
st.set_page_config(
    page_title="WealthyWays 💸 | Powered by Anni",
    page_icon="💰",
    layout="centered"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(145deg, #f7fdfc, #d1f7e3);
        font-family: 'Segoe UI', sans-serif;
    }
    .header {
        font-size: 48px;
        font-weight: bold;
        color: #1a3c40;
        text-align: center;
        margin-bottom: 0;
    }
    .subheader {
        font-size: 20px;
        color: #345;
        text-align: center;
        margin-top: -10px;
    }
    .section-title {
        font-size: 24px;
        color: #134e4a;
        margin-top: 40px;
    }
    .stButton>button {
        background-color: #16a34a;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Branding Title
st.markdown('<div class="header">WealthyWays</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Your Smart Finance Partner 🤝 — Meet Anni, the Budget Bot 💬</div>', unsafe_allow_html=True)

st.markdown("### 📥 Enter Your Monthly Financial Snapshot")

# User Inputs
income = st.number_input("💼 Monthly Income (₹)", min_value=0, help="Net take-home income")
expenses = st.number_input("🧾 Monthly Expenses (₹)", min_value=0, help="All regular outflows incl. rent, bills, food")
savings = st.number_input("🏦 Monthly Savings (₹)", min_value=0, help="Amount you save after expenses")
debt = st.number_input("💳 Current Debt (₹)", min_value=0, help="Include EMIs, credit card dues, loans")

# Predict & Show Advice
if st.button("💡 Ask Anni for Advice"):
    input_df = pd.DataFrame([[income, expenses, savings, debt]], columns=['income', 'expenses', 'savings', 'debt'])
    prediction = model.predict(input_df)[0]

    st.markdown("---")
    st.markdown("### 🧠 Anni's Advice:")

    if prediction == "Investment Ready":
        st.success("📈 You're in a strong financial position! Anni suggests exploring SIPs, mutual funds, or long-term stock investments.")
    elif prediction == "Cut Expenses":
        st.warning("📉 Your expenses seem high relative to income. Anni recommends reviewing subscriptions, food spending, and luxury buys.")
    elif prediction == "Basic Saving":
        st.info("💡 You're saving decently. Anni suggests automating savings and gradually increasing the amount.")
    elif prediction == "Emergency Mode":
        st.error("🚨 You're in a red zone. Reduce unnecessary spending and build at least 3 months of emergency savings.")

    # Saving Score Breakdown
    score = ((savings - debt) / (income + 1)) * 100
    st.markdown("### 📊 Your Saving Score")
    st.progress(min(max(score / 100, 0), 1))

    if score > 25:
        st.balloons()
        st.markdown("✅ Great job! You're financially secure. Now diversify investments.")
    elif score > 10:
        st.markdown("🟡 You’re doing okay. Focus more on savings consistency.")
    else:
        st.markdown("🔴 You need to rebalance income-expense-debt ratios. Anni believes small changes = big results.")

    # Optional Tip Box
    with st.expander("💬 Bonus Tip from Anni"):
        st.info("“Track your daily spending. You'll be surprised how little leaks add up!” – Anni")

# Footer
st.markdown("---")
st.markdown("Built with 💚 by **WealthyWays** | Your personal finance copilot 🚀")
st.markdown("Bot Advisor: **Anni** 🧠")
