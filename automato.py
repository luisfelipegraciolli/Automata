class Automato:
    """Representa um AFD simples."""
    def __init__(self, q: set, sigma: set, q0: str, f: set, delta: list):
        self.q = q
        self.sigma = sigma
        self.q0 = q0
        self.f = f
        self.delta = delta

    def check_cadeia(self, cadeia: str) -> bool:
        """
        Verifica se a cadeia é aceita pelo AFD, imprimindo o passo a passo
        da função de transição estendida (delta^).
        """
        estado_atual = self.q0
        
        print("\n[INFO] Iniciando verificação passo a passo:")
        
        cadeia_para_mostrar = cadeia if cadeia else "epsilon" 
        print(f"  delta^({estado_atual}, \"{cadeia_para_mostrar}\")")

        for i, simbolo in enumerate(cadeia):
            proximo_estado = None
            for (origem, simbolo_transicao, destino) in self.delta:
                if origem == estado_atual and simbolo_transicao == simbolo:
                    proximo_estado = destino
                    break
            
            if proximo_estado is None:
                # Mostra o passo que falhou
                print(f"  = δ^({estado_atual}, \"{simbolo}{cadeia[i+1:]}\")")
                print(f"\n[PASSO] Transição indefinida.")
                print(f"         Não existe transição para o símbolo '{simbolo}' partindo do estado '{estado_atual}'.")
                print("\n[RESULTADO] ❌ Cadeia REJEITADA.")
                return False  # Não existe transição para esse símbolo
            
            estado_atual = proximo_estado
            
            # Pega o restante da cadeia
            cadeia_restante = cadeia[i+1:]
            # Se for vazia:
            cadeia_para_mostrar = cadeia_restante if cadeia_restante else "epsilon"
            print(f"  = delta^({estado_atual}, \"{cadeia_para_mostrar}\")")

        # Verificação final
        is_final = estado_atual in self.f
        
        print(f"  = {estado_atual}") 
        
        print("\n[RESULTADO]")
        print(f"A função termina no estado: {estado_atual}")
        if is_final:
            print(f"Como {estado_atual} pertence a {self.f} (estados finais), a cadeia é ✅ ACEITA.")
        else:
            print(f"Como {estado_atual} não pertence a {self.f} (estados finais), a cadeia é ❌ REJEITADA.")
                
        return is_final