class BaseStrategy:
    def __init__(self, name, allocation):
        self.name = name
        self.allocation = allocation

    def payoff(self, ST):
        raise NotImplementedError
