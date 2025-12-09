# agents.py
from utils import call_llm_or_mock

class FinanceAgent:
    def analyze(self, scenario):
        prompt = f"""
You are a city Finance Minister. Analyze the policy scenario concisely.

Scenario:
{scenario}

Return a JSON with keys: budget_impact, tax_effect, risk (short sentences).
"""
        return call_llm_or_mock(prompt, role="Finance")

class TransportAgent:
    def analyze(self, scenario):
        prompt = f"""
You are the Transport Commissioner. Analyze mobility and transport impacts.

Scenario:
{scenario}

Return a JSON with keys: traffic_impact, logistics_cost, public_transport (short sentences).
"""
        return call_llm_or_mock(prompt, role="Transport")

class HealthAgent:
    def analyze(self, scenario):
        prompt = f"""
You are the Chief Health Officer. Analyze health system impact.

Scenario:
{scenario}

Return a JSON with keys: hospital_load, public_health, long_term (short sentences).
"""
        return call_llm_or_mock(prompt, role="Health")

class DisasterAgent:
    def analyze(self, scenario):
        prompt = f"""
You are the Disaster Management Head. Analyze disaster preparedness implications.

Scenario:
{scenario}

Return a JSON with keys: emergency_funds, preparedness, warning (short sentences).
"""
        return call_llm_or_mock(prompt, role="Disaster")
