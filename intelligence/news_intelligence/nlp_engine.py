class NLPEngine:

    def extract(self, headlines):

        parsed = []

        for h in headlines:

            parsed.append({
                "text": h,
                "keywords": [w for w in h.lower().split() if len(w) > 4]
            })

        return parsed
