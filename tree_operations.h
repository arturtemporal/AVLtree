#ifndef __AVL_OPERATOR__
#define __AVL_OPERATOR__

#include "avl_tree.h"

// retorna 1 caso a árvore ja tenha sido inicializada, 0 caso contrário 
int tree_is_empty(avl_t *t);

// insere a chave 'key' a partir um nodo apontado, retorna 1 em caso de sucesso, 0 caso contrário
int insert_key_by_node(node_t **top, node_t *nd, key_t key);

// insere uma chave no nodo especificado, com o pai
int insert_key(node_t **nd, node_t *top, key_t key);

// procura a chave 'key' a partir de um nodo apontado, 1 se a chave esta presente e 0 caso contrario
int search_key_by_node(node_t *nd, key_t key);

void print_tree_by_node(node_t *nd);



#endif