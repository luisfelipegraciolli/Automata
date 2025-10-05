class Automato:

## q == Estados
## sigma == Alfabeto
## q0 == Estado Inicial
## f == Estados finais
## delta == Tabela de transições

    def __init__(self, q: set, sigma: set, q0: str, f: set, delta: list):
        self.q = q
        self.sigma = sigma
        self.q0 = q0
        self.f = f
        self.delta = delta
    

    def check_cadeia(cadeia: str) -> bool:
        pass