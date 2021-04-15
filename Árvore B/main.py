import os
from avb import avB

def menu():
    print(
        """
--------- Menu ----------
| 1) Adicionar nó       |
| 2) Buscar nó          |
| 3) Remover nó         |
| 4) Imprimir árvore    |
| 5) Sair               |
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
            if(arvre.busca(num)[0]):
                print("Valor encontrado com sucesso!")
            else:
                print("Valor não foi encontrado!")
        elif(num == 3):
            num = int(input("Insira o valor que deseja remover: "))
            arvre.remove(num)
        elif(num == 4):
            arvre.print_tree()
        elif(num == 5):
            print("Por hoje é só pessoal! ;)")
            b = False
        else:
            print("Entrada inválida. Tente novamente!\n")
        input("Insira enter para continuar...")
        os.system('clear')

if __name__ == "__main__":
    main()    