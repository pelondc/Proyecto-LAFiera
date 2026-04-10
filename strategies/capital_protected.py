from strategies.base_strategy import BaseStrategy

class CapitalProtected(BaseStrategy):
    def __init__(self, allocation, protection, participation, K):
        super().__init__("Capital Protected", allocation)
        self.protection = protection
        self.participation = participation
        self.K = K

    def payoff(self, ST):
        return max(self.protection, self.participation * max(ST - self.K, 0))
