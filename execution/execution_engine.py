class ExecutionEngine:

    def __init__(self, broker, risk_engine):
        self.broker = broker
        self.risk_engine = risk_engine

    def execute(self, signal):

        size = self.risk_engine.calculate_position_size(
            signal.entry,
            signal.stop_loss
        )

        if size <= 0:
            return {"status": "rejected"}

        return self.broker.place_order(
            symbol=signal.symbol,
            direction=signal.direction,
            size=size,
            entry=signal.entry,
            sl=signal.stop_loss,
            tp=signal.take_profit
        )
