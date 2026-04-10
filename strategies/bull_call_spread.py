from strategies.base_strategy import BaseStrategy

class BullCallSpread(BaseStrategy):
    def __init__(self, allocation, K1, K2):
        super().__init__("Bull Call Spread", allocation)
        self.K1 = K1
        self.K2 = K2

    def payoff(self, ST):
        return max(ST - self.K1, 0) - max(ST - self.K2, 0)
