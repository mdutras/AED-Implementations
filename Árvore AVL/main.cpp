#include<cstdio>
#include<iostream>
#include <stdlib.h>
#include "avl.hh"

void menu(){
    printf("-------------Menu-------------\n");
    printf("| 1 - Adicionar nó           |\n");
    printf("| 2 - Remover nó             |\n");
    printf("| 3 - Imprimir árvore        |\n");
    printf("| 4 - Sair                   |\n");
    printf("------------------------------\n");
}

int main(){
    int choose, val;
    AVL *tree = new  AVL();
    bool b = true;
    while(b){
        menu();
        printf("Insira sua opção: ");
        std::cin >> choose;
        switch (choose){
        case 1:
            printf("Insira o valor que deseja adicionar na árvore: ");
            std::cin >> val;
            tree->add(val);
            break;

        case 2:
            printf("Insira o valor que deseja remover na árvore: ");
            std::cin >> val;
            tree->remove(val);
            break;

        case 3:
            tree->print_alt();
            break;

        case 4:
            b = false;
            break;
            
        default:
            printf("Entrada inválida!\n");
            break;
        }
    }
    return 0;
}