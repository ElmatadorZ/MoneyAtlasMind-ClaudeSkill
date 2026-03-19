from data_pipeline.ingestion_engine import IngestionEngine
from data_pipeline.normalization_engine import NormalizationEngine
from orchestrator.war_brain import WarBrain

def main():

    ingestion = IngestionEngine()
    norm = NormalizationEngine()
    brain = WarBrain()

    def loop():

        raw = ingestion.fetch_all()
        clean = norm.process(raw)

        smc_layers = [
            type("Layer", (), {
                "state": "accumulating",
                "confidence": 0.8,
                "cost_basis": 1900,
                "layer": 1
            })()
        ]

        result = brain.run(smc_layers, clean)

        print("=== REAL-TIME INTELLIGENCE ===")
        print(result)

    # simulate stream
    import time
    while True:
        loop()
        time.sleep(15)

if __name__ == "__main__":
    main()
