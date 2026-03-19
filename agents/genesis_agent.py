from .base_agent import BaseAgent, AgentOutput
from core.genesis_core import GenesisCore


class GenesisAgent(BaseAgent):
    name = "genesis"

    def __init__(self):
        self.core = GenesisCore()

    async def run(self, context):

        result = self.core.run(context)

        return AgentOutput(
            name=self.name,
            data=result,
            confidence=0.9,
            reasoning="Genesis Protocol executed"
        )
