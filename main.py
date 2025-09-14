## Fazer com que uma função leia um arquivo e retorne o conteudo desse arquivo
def ler_cadeia(file_name: str) -> str:
    cadeia: str = ''
    with open(file_name, 'r') as f:
        cadeia = f.read()

    f.close()
    return cadeia

## Fazer script que le um arquivo com uma cadeia alfabeto {a,b} somente
def check_alfabeto(cadeia: str) -> bool:
    return set(cadeia).issubset({'a', 'b'})



## Fazer script que le um arquivo contendo um AFD
## Fazer com que o AFD leia uma cadeia e retorne se ela pertence a uma linguagem

def main():
    print("HII")
    cadeia = ler_cadeia("cadeia.txt")
    print(cadeia)
    isInAlphabet = check_alfabeto(cadeia)
    print(isInAlphabet)



if __name__ == "__main__":
    main()

