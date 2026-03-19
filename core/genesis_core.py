# core/genesis_core.py

from typing import Dict, Any


class GenesisCore:

    def __init__(self):
        pass

    def first_principle(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reduce asset to fundamental drivers
        """
        symbol = context.get("symbol")

        if "BTC" in symbol:
            return {
                "asset_type": "digital scarcity",
                "value_driver": "liquidity + adoption",
                "risk": "macro liquidity tightening"
            }

        if "GOLD" in symbol:
            return {
                "asset_type": "store of value",
                "value_driver": "real rates",
                "risk": "strong dollar"
            }

        return {
            "asset_type": "unknown",
            "value_driver": "unknown",
            "risk": "unknown"
        }

    def system_map(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map macro → liquidity → asset
        """
        macro = context.get("macro", {})

        if macro.get("macro_bias") == "bearish":
            return {
                "liquidity": "tightening",
                "impact": "risk_off"
            }

        return {
            "liquidity": "neutral",
            "impact": "sideways"
        }

    def narrative(self, context: Dict[str, Any]) -> str:
        """
        Money Atlas narrative layer
        """
        smc = context.get("smc", {})

        if smc:
            return "Smart money is positioning around key liquidity zones"

        return "Market lacks clear dominant force"

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full Genesis Execution
        """

        fp = self.first_principle(context)
        sm = self.system_map(context)
        narrative = self.narrative(context)

        return {
            "first_principle": fp,
            "system_map": sm,
            "narrative": narrative
        }
