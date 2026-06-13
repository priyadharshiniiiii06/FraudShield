import streamlit as st

st.title("💳 FraudShield")
st.write("Welcome to FraudShield")

amount = st.number_input("Enter Transaction Amount")

if st.button("Check"):
    if amount > 10000:
        st.error("⚠ Fraudulent Transaction")
    else:
        st.success("✅ Genuine Transaction")