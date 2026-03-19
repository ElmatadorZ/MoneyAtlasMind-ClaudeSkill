from .news_collector import NewsCollector
from .nlp_engine import NLPEngine
from .narrative_engine import NarrativeEngine
from .bias_engine import BiasEngine
from .impact_mapper import ImpactMapper
from .signal_engine import SignalEngine

class NewsIntelligence:

    def __init__(self):
        self.collector = NewsCollector()
        self.nlp = NLPEngine()
        self.narrative = NarrativeEngine()
        self.bias = BiasEngine()
        self.impact = ImpactMapper()
        self.signal = SignalEngine()

    def run(self, smc_layers):

        headlines = self.collector.fetch()
        parsed = self.nlp.extract(headlines)
        narratives = self.narrative.detect(parsed)
        bias = self.bias.analyze(narratives)
        impact = self.impact.map(bias)

        signals = self.signal.generate(impact, smc_layers)

        return {
            "headlines": headlines[:5],
            "narratives": narratives,
            "bias": bias,
            "impact": impact,
            "signals": signals
        }
