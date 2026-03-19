import asyncio
from smc.smc_layer_masterpiece import load_ohlcv_csv, SMCLayerEngine

async def main():
    candles = load_ohlcv_csv("examples/sample_data.csv")

    engine = SMCLayerEngine()

    result = await engine.analyze(
        symbol="BTCUSDT",
        timeframe="4H",
        candles=candles
    )

    for layer in result.layers:
        print(f"Layer {layer.layer}: {layer.price_low} - {layer.price_high}")
        print(f"State: {layer.state}, Confidence: {layer.confidence}")
        print("-" * 40)

asyncio.run(main())
