# core/decision_engine.py

class DecisionEngine:

    def decide(self, options: list):
        scored = []

        for opt in options:
            score = opt["reward"] - opt["risk"]
            scored.append((score, opt))

        best = sorted(scored, key=lambda x: x[0], reverse=True)[0][1]

        return {
            "decision": best,
            "confidence": 0.7,
            "reason": "Best risk-reward ratio"
        }
