# orchestrator/war_brain.py

from intelligence.alpha_engine import AlphaEngine
from intelligence.macro_engine import MacroEngine
from intelligence.geopolitic_engine import GeopoliticEngine
from strategy.asymmetric_engine import AsymmetricEngine
from strategy.scenario_war_game import ScenarioWarGame
from cognition.meta_cognition import MetaCognition

class WarBrain:

    def __init__(self):
        self.alpha = AlphaEngine()
        self.macro = MacroEngine()
        self.geo = GeopoliticEngine()
        self.asym = AsymmetricEngine()
        self.scenario = ScenarioWarGame()
        self.meta = MetaCognition()

    def run(self, smc_layers):

        alpha = self.alpha.detect(smc_layers)
        macro = self.macro.analyze()
        geo = self.geo.evaluate()

        asym = self.asym.find(alpha, macro, geo)
        scenarios = self.scenario.simulate(macro, geo)

        warnings = self.meta.check(asym)

        return {
            "alpha": alpha,
            "macro": macro,
            "geopolitics": geo,
            "asymmetric_opportunities": asym,
            "scenarios": scenarios,
            "bias_warnings": warnings
        }
