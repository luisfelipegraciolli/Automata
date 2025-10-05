from automato import Automato
import re
import os

def ler_cadeia(file_name: str) -> str:
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read().strip()

def check_alfabeto(cadeia: str, alfabeto: set) -> bool:
    """Verifica se todos os símbolos da cadeia pertencem ao alfabeto."""
    return set(cadeia).issubset(alfabeto)

def get_set(line: str) -> set:
    """Extrai o conteúdo de um conjunto no formato {x,y,z}."""
    m = re.search(r'\{([^}]*)\}', line)
    if not m:
        return set()
    conteudo = m.group(1)
    return set(x.strip() for x in conteudo.split(',') if x.strip())

def ler_automato(file_name: str) -> Automato:
    """Lê um arquivo texto e retorna um objeto Automato."""
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    q = set()
    sigma = set()
    q0 = ""
    f_estados = set()
    delta = []

    for line in lines:
        if line.startswith('q='):
            q = get_set(line)
        elif line.startswith('sigma='):
            sigma = get_set(line)
        elif line.startswith('q0='):
            q0 = line.split('=', 1)[1].strip()
        elif line.startswith('f='):
            f_estados = get_set(line)
        elif line.startswith('delta='):
            delta_str = line.split('=', 1)[1].strip()
            if delta_str.startswith('{') and delta_str.endswith('}'):
                delta_str = delta_str[1:-1]
            matches = re.findall(r'\{\s*([^,{}]+)\s*,\s*([^,{}]+)\s*,\s*([^{}]+)\s*\}', delta_str)
            for origem, simbolo, destino in matches:
                delta.append((origem.strip(), simbolo.strip(), destino.strip()))

    print("\n[INFO] Autômato carregado com sucesso:")
    print("Estados:", q)
    print("Alfabeto:", sigma)
    print("Inicial:", q0)
    print("Finais:", f_estados)
    print("Transições:", delta)

    return Automato(q, sigma, q0, f_estados, delta)

def check_afd_cadeia(automato: Automato, cadeia: str) -> str:
    """Executa a verificação e retorna mensagem legível."""
    if automato.check_cadeia(cadeia):
        return "✅ Cadeia Aceita"
    else:
        return "❌ Cadeia Inválida"

def main():
    automatoAfd = ler_automato("automato.txt")
    alfabeto = automatoAfd.sigma

    if os.path.exists("cadeia.txt"):
        cadeia = ler_cadeia("cadeia.txt")
    else:
        cadeia = "abb"
        print("[WARN] Arquivo 'cadeia.txt' não encontrado — usando 'abb' para teste.")

    print("\n[INFO] Cadeia a validar:", repr(cadeia), "\n")

    if check_alfabeto(cadeia, alfabeto):
        print(check_afd_cadeia(automatoAfd, cadeia))
    else:
        print("⚠️ Cadeia contém símbolos fora do alfabeto")

if __name__ == "__main__":
    main()
