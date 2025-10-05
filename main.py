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



## Fazer script que le um arquivo contendo um AFD
def ler_automato(file_name: str) -> Automato:

    obj1 = Automato()
    return obj1

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

