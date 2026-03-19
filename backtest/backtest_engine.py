# backtest/backtest_engine.py

class BacktestEngine:

    def run(self, signals):
        results = []

        for s in signals:
            outcome = self._simulate_trade(s)
            results.append(outcome)

        return results

    def _simulate_trade(self, signal):
        # mock simulation
        return {
            "signal": signal,
            "result": "win" if signal["confidence"] > 0.6 else "loss"
        }
