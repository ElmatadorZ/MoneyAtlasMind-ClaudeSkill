# cognition/meta_cognition.py

class MetaCognition:

    def check(self, decisions):

        warnings = []

        for d in decisions:
            if "high" in str(d):
                warnings.append("Potential overconfidence bias")

        return warnings
