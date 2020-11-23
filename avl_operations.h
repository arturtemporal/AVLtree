#ifndef AVL_OPS
#define AVL_OPS

#include "avl_module.h"

// retorna o fator de balanceamento da subárvore
int balance_factor(node_t *nd);

int rotate_right(node_t **nd);
int rotate_left(node_t **nd);

// rotaciona a árvore para realizar seu balanço
int rotate(node_t **nd, int *bal);

int adjust_bf_up(node_t *nd);

int balance_to_key(node_t **nd, key_t key);

#endif