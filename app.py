# app.py
import streamlit as st
from mayor import MayorAgent
from simulator import generate_summary
import json

st.set_page_config(page_title="AI Micro-Government Simulator", layout="centered")
st.title("🏛 AI-Powered Micro-Government Simulator (Demo)")

st.markdown("Enter a policy scenario and run a multi-agent simulation. Agents use a local LLM if configured, otherwise deterministic mock responses for quick demo.")

with st.form("scenario_form"):
    scenario = st.text_area("Policy scenario", value="Simulate a 5% increase in property tax city-wide for 12 months.")
    horizon = st.selectbox("Simulation horizon (months)", [6, 12, 24], index=1)
    seed = st.number_input("Random seed (for reproducibility, demo use)", value=42)
    submitted = st.form_submit_button("Run Simulation")

if submitted:
    st.info("Running simulation — this may take a few seconds (mock or local LLM).")
    mayor = MayorAgent()
    reports = mayor.process_scenario(scenario)
    st.subheader("Departmental Reports")
    for dept, report in reports.items():
        with st.expander(dept):
            if isinstance(report, dict):
                st.json(report)
            else:
                # if it's raw text or string
                try:
                    st.json(json.loads(report))
                except Exception:
                    st.write(report)

    st.subheader("City-wide Summary (Mayor-2)")
    summary = generate_summary(scenario, reports)
    if isinstance(summary, dict):
        st.json(summary)
    else:
        st.write(summary)
