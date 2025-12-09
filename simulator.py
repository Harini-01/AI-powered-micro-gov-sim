# simulator.py
from utils import call_llm_or_mock
import json

def generate_summary(scenario, reports):
    # Prepare a clear prompt for the summary agent (Mayor-2)
    prompt = f"""
You are the City Mayor synthesizing department reports.
Scenario:
{scenario}

Finance Report:
{json.dumps(reports.get('Finance', {}), ensure_ascii=False)}

Transport Report:
{json.dumps(reports.get('Transport', {}), ensure_ascii=False)}

Health Report:
{json.dumps(reports.get('Health', {}), ensure_ascii=False)}

Disaster Report:
{json.dumps(reports.get('Disaster', {}), ensure_ascii=False)}

Produce a JSON with keys: overall_impact, key_risks, recommendations (each short).
"""
    # Use role "Mayor" for mock selection
    summary = call_llm_or_mock(prompt, role="Mayor")
    # If summary is dict-like return it; else wrap.
    if isinstance(summary, dict):
        return summary
    else:
        return {"summary_text": summary}
