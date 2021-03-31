// #pragma once
#ifndef __MYCLASS_H
#define __MYCLASS_H

class AVL{
    private:
        struct node{
            int valor;
            struct node *esq;
            struct node *dir;
        };

        typedef struct node Node;

        typedef struct node* Arvore;

        Arvore *start;

        struct heap{
            int value;
            heap *next;
        };
    public:
        AVL();

        bool vazia();

        void add(int val);

        void remove(int k);

        int cont_altura(Node *n);

        int altura(Node *n);

        bool AVL_check(Node *n);

        bool is_AVL();

        void check_node(Node *n, Node *hook);

        void turn_AVL();

        void cont_print_alt(Node *n, heap H[], int num);

        void print_alt();
};
#endif