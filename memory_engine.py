import json
from datetime import datetime

MEMORY_FILE = "memory.json"

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_trade(symbol, entry, sl, tp, result=None):
    data = load_memory()
    trade = {
        "symbol": symbol,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "result": result,
        "time": str(datetime.utcnow())
    }
    data["trades"].append(trade)
    save_memory(data)

def log_insight(text):
    data = load_memory()
    data["insights"].append({
        "text": text,
        "time": str(datetime.utcnow())
    })
    save_memory(data)
