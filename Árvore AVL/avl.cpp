#include<cstdio>
#include<iostream>
#include <stdlib.h>

#include "avl.hh"

AVL::AVL(){
    start = (Arvore*)malloc(sizeof(Arvore));
    *start = NULL;
}

bool AVL::vazia(){
    bool ans = false;
    if(*start == NULL){
        ans = true;
        printf("Lista vazia!\n");
    }
    return ans;
}

void AVL::add(int val){
    Node *novo = (Node*)malloc(sizeof(Node));
    novo->valor = val;
    novo->esq = NULL;
    novo->dir = NULL;
    if(*start == NULL){
        *start = novo;
    }else{
        Node *aux = *start;
        Node *ant = aux;
        while(aux != NULL & ant != NULL){
            ant = aux;
            if(aux->valor > novo->valor){
                aux = aux->esq;
            }else if(aux->valor < novo->valor){
                aux = aux->dir;
            }else{
                ant = NULL;
            }
        }
        if(ant != NULL){
            (ant->valor > novo-> valor? ant->esq:ant->dir) = novo; 
            turn_AVL();
        }else{
            printf("Elemento já inserido!\n");
        }
    }
}

void AVL::remove(int k){
    if(!vazia()){
        Node *aux = *start;
        Node *ant = NULL;
        while(aux->valor != k & aux != NULL){
            ant = aux;
            aux = (aux->valor > k? aux->esq:aux->dir);
        }
        if(aux != NULL){
            if(aux == *start & aux->esq == NULL || aux->dir == NULL){
                *start = NULL;
            }else{
                while(aux!=NULL){
                    if(aux->esq == NULL || aux->dir == NULL){
                        (ant->esq == aux? ant->esq: ant->dir) = NULL;
                        aux = NULL;
                    }else{
                        Node *maior;
                        if(aux->esq == NULL & aux->dir != NULL){
                            maior = aux->dir;
                        }else if(aux->dir == NULL & aux->esq != NULL){
                            maior = aux->esq;
                        }else{
                            maior = (aux->dir->valor > aux->esq->valor? aux->dir: aux->esq);
                        }
                        aux->valor = maior->valor;
                        ant = aux;
                        aux = maior;
                    }   
                }
                turn_AVL();
            }
        }else{
            printf("Elemento não pertence à lista.");
        }     
    }
}

int AVL::cont_altura(Node *n){
    if(n == NULL){
        return 0;
    }else{
        int esq = cont_altura(n->dir);
        int dir = cont_altura(n->esq);
        return ((esq > dir)? esq:dir) + 1;
    }
}

int AVL::altura(Node *n){
    int altura = cont_altura(n);
    return altura;
}

bool AVL::AVL_check(Node *n){
    bool ans;
    if(n == NULL){
        ans = true;
    }else{
        int esq = altura(n->esq);
        int dir = altura(n->dir);
        ans = (abs(esq - dir) > 1? false:(AVL_check(n->esq) & AVL_check(n->dir)));
    }
    return ans;
}

bool AVL::is_AVL(){
    return AVL_check(*start);
}

void AVL::check_node(Node *n, Node *hook){
    if(n != NULL){
        check_node(n->esq, n);
        check_node(n->dir, n);
        int esq = altura(n->esq);
        int dir = altura(n->dir);
        if(abs(esq - dir) > 1){
            if(esq > dir){
                if(altura(n->esq->dir) > altura(n->esq->esq)){
                    Node *u = n->esq;
                    Node *v = n->esq->dir;
                    Node *t2 = v->esq;
                    Node *t3 = v->dir;
                    if(hook == NULL){
                        *start = v;
                    }else{
                        hook->esq = v;
                    }
                    u->dir = t2;
                    n->esq = t3;
                    v->esq = u;
                    v->dir = n;
                }else{
                    Node *t2 = n->esq->dir;
                    Node *u = n->esq;
                    if(hook == NULL){
                        *start = u;
                    }else{
                        hook->esq = u;
                    }
                    n->esq = t2;
                    u->dir = n;
                }
            }else{
                if(altura(n->dir->esq) > altura(n->dir->dir)){
                    Node *u = n->dir;
                    Node *v = n->dir->esq;
                    Node *t2 = v->esq;
                    Node *t3 = v->dir;
                    if(hook == NULL){
                        *start = v;
                    }else{
                        hook->dir = v;
                    }
                    n->dir = t2;
                    u->esq = t3;
                    v->esq = n;
                    v->dir = u;
                }else{
                    Node *t2 = n->dir->esq;
                    Node *u = n->dir;
                    if(hook == NULL){
                        *start = u;
                    }else{
                        hook->dir = u;
                    }
                    n->dir = t2;
                    u->esq = n;
                }
            }
        }
    }
}

void AVL::turn_AVL(){
    if(!vazia()){
        if(!is_AVL()){
            check_node(*start, NULL);
        }
    }
}

void AVL::cont_print_alt(Node *n, heap H[], int num){
    if(n != NULL){
        if(H[num].next == &H[num]){
            H[num].value = n->valor;
            H[num].next = NULL;
        }else{
            struct heap *novo = (struct heap*)malloc(sizeof(struct heap));
            novo->value = n->valor;
            novo->next = NULL;
            struct heap *aux = &H[num];
            while(aux->next != NULL){
                aux = aux->next;
            }   
            aux->next = novo;
        }
        cont_print_alt(n->esq, H, num + 1);
        cont_print_alt(n->dir, H, num + 1);
    }
}

void AVL::print_alt(){
    if(!vazia()){
        int alt = altura(*start);
        struct heap H[alt];
        for(int i = 0; i < alt; i++){
            H[i].value = 0;
            H[i].next = &H[i];
        }
        cont_print_alt(*start, H, 0);
        for(int i = 0; i < alt; i++){
            printf("%d: ", i);
            struct heap *aux = &H[i];
            while(aux != NULL){
                printf("%d ", aux->value);
                aux = aux->next;
            }
            printf("\n\n");
        }
    }            
}



