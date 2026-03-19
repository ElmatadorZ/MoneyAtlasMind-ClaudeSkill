import requests

class MarketAPI:

    def get_price(self, symbol="XAUUSD"):
        # Example: use free endpoint or broker API
        url = f"https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

        try:
            r = requests.get(url, timeout=5)
            data = r.json()
            return float(data["price"])
        except:
            return None
