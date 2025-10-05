from automato import Automato

## Fazer com que uma função leia um arquivo e retorne o conteudo desse arquivo
def ler_cadeia(file_name: str) -> str:
    cadeia: str = ''
    with open(file_name, 'r') as f:
        cadeia = f.read()

    f.close()
    return cadeia

## Fazer script que le um arquivo com uma cadeia alfabeto {a,b} somente
def check_alfabeto(cadeia: str, alfabeto: set) -> bool:
    return set(cadeia).issubset(alfabeto)

def get_set(line: str) -> set:
    return set(line.split('=')[1].strip('{}').split(','))

## Fazer script que le um arquivo contendo um AFD
def ler_automato(file_name: str) -> Automato:

    ## q == Estados
    ## sigma == Alfabeto
    ## q0 == Estado Inicial
    ## f == Estados finais
    ## delta == Tabela de transições

    with open(file_name, 'r') as f:
       lines = [line.strip() for line in f if line.strip()]

    q: set
    sigma: set 
    q0: str 
    f: set 
    delta: list = []


    for line in lines:
        if line.startswith('q='):
            ## divide a string em dois a partir de '=', pega a segunda e separa por ','
            q = get_set(line)
        elif line.startswith('sigma='):
            sigma = get_set(line)
        elif line.startswith('q0='):
            q0 = line.split('=')[1].strip()
        elif line.startswith('f='):
            f = get_set(line)
        elif line.startswith('delta='):
            delta_str = line.split('=', 1)[1].strip()
            # Extrai todas as transições do tipo {s1, a, s2}
            import re
            matches = re.findall(r'\{([^}]+)\}', delta_str)
            for m in matches:
                partes = [x.strip() for x in m.split(',')]
                if len(partes) == 3:
                    delta.append(tuple(partes))

    print(delta)

    automato = Automato(q, sigma, q0, f, delta)
    return automato

## Fazer com que o AFD leia uma cadeia e retorne se ela pertence a uma linguagem
def check_afd_cadeia(automato: Automato) -> str:
    if(automato.check_cadeia()):
        return "Cadeia Aceita"
    else:
        return "Cadeia invalida"

def main():
    automatoAfd = ler_automato("automato.txt")
    alfabeto = automatoAfd.sigma

    cadeia = ler_cadeia("cadeia.txt")

    isInAlphabet = check_alfabeto(cadeia, alfabeto)

    if(isInAlphabet):
        print(check_afd_cadeia(automatoAfd))
    else:
        print("Cadeia não pertence ao alfabeto")


if __name__ == "__main__":
    main()

