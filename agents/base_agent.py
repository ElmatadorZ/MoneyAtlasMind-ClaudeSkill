# agents/base_agent.py

from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class AgentOutput:
    name: str
    data: Dict[str, Any]
    confidence: float
    reasoning: str


class BaseAgent:
    name = "base"

    async def run(self, context: Dict[str, Any]) -> AgentOutput:
        raise NotImplementedError
