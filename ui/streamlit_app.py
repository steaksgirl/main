import os
import requests
import streamlit as st

API_URL = os.getenv("CLAIMS_RAG_API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Claims RAG Assistant", page_icon="📄")
st.title("Claims RAG Assistant")
st.caption("Source-grounded claim review support — not a coverage determination.")

with st.form("claim"):
    claim_id = st.text_input("Claim ID", "CLM-1001")
    policy_number = st.text_input("Policy number", "HO-12345")
    loss_date = st.date_input("Loss date")
    loss_type = st.text_input("Loss type", "Water damage")
    description = st.text_area("Loss description", "A pipe burst in the kitchen and damaged cabinets.")
    amount = st.number_input("Claimed amount", min_value=0.0, value=3500.0)
    submitted = st.form_submit_button("Analyze claim")

if submitted:
    payload = {"claim_id": claim_id, "policy_number": policy_number, "loss_date": str(loss_date), "loss_type": loss_type, "description": description, "claimed_amount": amount}
    try:
        requests.post(f"{API_URL}/claims", json=payload, timeout=10).raise_for_status()
        result = requests.post(f"{API_URL}/claims/{claim_id}/analysis", timeout=20)
        result.raise_for_status()
        analysis = result.json()
        st.subheader("Analysis")
        st.write(analysis["summary"])
        st.subheader("Sources")
        for source in analysis["sources"]:
            st.markdown(f"**{source['document_id']}** ({source['category']})")
            st.caption(source["excerpt"])
        st.info(analysis["disclaimer"])
    except requests.RequestException as exc:
        st.error(f"Could not reach the API: {exc}")
