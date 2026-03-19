class BiasEngine:

    def analyze(self, narratives):

        bias_score = {
            "bullish": 0,
            "bearish": 0,
            "risk_off": 0
        }

        for n in narratives:

            if n["bias"] == "hawkish":
                bias_score["bearish"] += 1

            if n["bias"] == "risk_off":
                bias_score["risk_off"] += 1

        return bias_score
