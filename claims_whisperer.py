import streamlit as st
import openai

st.title("Claims Whisperer")
st.subheader("AI-Powered Medical Claim Assistant")

visit_summary = st.text_area("Describe the patient visit", placeholder="e.g., Follow-up for post-op left knee arthroscopy...")

if st.button("Generate Claim Info"):
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a certified medical coder. Given a patient visit summary, return appropriate CPT and ICD-10 codes with brief justification."},
                {"role": "user", "content": visit_summary}
            ]
        )
        st.markdown("### ✅ Suggested Codes")
        st.write(response["choices"][0]["message"]["content"])