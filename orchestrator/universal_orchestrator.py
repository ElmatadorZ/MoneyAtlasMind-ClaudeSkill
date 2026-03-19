from analyzer.insight_engine import InsightEngine
from analyzer.risk_engine import RiskEngine
from strategic.scenario_engine import ScenarioEngine
from strategic.decision_engine import DecisionEngine

class UniversalOrchestrator:

    def __init__(self):
        self.insight = InsightEngine()
        self.risk = RiskEngine()
        self.scenario = ScenarioEngine()
        self.decision = DecisionEngine()

    def run(self, smc_layers):

        insights = self.insight.generate(smc_layers)
        risks = self.risk.evaluate(smc_layers)
        scenarios = self.scenario.simulate(smc_layers)

        return self.decision.advise(insights, risks, scenarios)
