class Automato:
    """Representa um AFD simples."""
    def __init__(self, q: set, sigma: set, q0: str, f: set, delta: list):
        self.q = q
        self.sigma = sigma
        self.q0 = q0
        self.f = f
        self.delta = delta

    def check_cadeia(self, cadeia: str) -> bool:
        """Verifica se a cadeia é aceita pelo AFD."""
        estado_atual = self.q0
        for simbolo in cadeia:
            proximo_estado = None
            for (origem, simbolo_transicao, destino) in self.delta:
                if origem == estado_atual and simbolo_transicao == simbolo:
                    proximo_estado = destino
                    break
            if proximo_estado is None:
                return False  # Não existe transição para esse símbolo
            estado_atual = proximo_estado
        return estado_atual in self.f
