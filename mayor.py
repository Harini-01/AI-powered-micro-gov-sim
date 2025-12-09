# mayor.py
from agents import FinanceAgent, TransportAgent, HealthAgent, DisasterAgent

class MayorAgent:
    def __init__(self):
        self.finance = FinanceAgent()
        self.transport = TransportAgent()
        self.health = HealthAgent()
        self.disaster = DisasterAgent()

    def process_scenario(self, scenario):
        # Can be parallelized later; for demo run sequentially
        finance_report = self.finance.analyze(scenario)
        transport_report = self.transport.analyze(scenario)
        health_report = self.health.analyze(scenario)
        disaster_report = self.disaster.analyze(scenario)

        return {
            "Finance": finance_report,
            "Transport": transport_report,
            "Health": health_report,
            "Disaster": disaster_report
        }
