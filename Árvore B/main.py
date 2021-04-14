from avb import avB

def menu():
    print(
        """
--------- Menu ----------
| 1) Adicionar nó       |
| 2) Buscar nó          |
| 3) Remover nó         |
| 4) Sair               |
-------------------------
        """
    )

def main():
    num = int(input('Digite o grau da árvore B: '));
    arvre = avB(num)
    b = True
    while(b):
        menu()
        num = int(input("Insira sua opção: "))
        if(num == 1):
            num = int(input("Insira o valor que deseja inserir: "))
            arvre.add(num)
        elif(num == 2):
            num = int(input("Insira o valor que deseja buscar: "))
            a = arvre.busca(num)
            print(a[0])
        # elif(num == 3):

        elif(num == 4):
            print("Por hoje é só pessoal! ;)")
            b = False
        else:
            print("Entrada inválida. Tente novamente!\n")

if __name__ == "__main__":
    main()    