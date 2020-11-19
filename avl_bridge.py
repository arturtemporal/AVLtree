#!/usr/bin/env python3
"""
Modulo ponte entre scripts Python e a biblioteca avl_module.so
Autores: Gabriel Nascarella Hishida e Artur Temporal Coelho
"""

import ctypes
from ctypes import byref
# Usamos 'byref' muitas vezes

buffer_size = 16

# Importando a lib para usos futuros:
lib = ctypes.CDLL("./avl_module.so")

class avl_tree(ctypes.Structure):
    """Arvore AVL, definida a partir da struct avl_t"""

    _fields_ = [
        ("root", ctypes.POINTER(ctypes.c_void_p)),
    ]

    def __init__(self):
        """Inicializa a classe/struct"""
        # Verifique docs/sources.txt: By Reference
        lib.initialize_avl(byref(self))

    def insert_key(self, key):
        """
        Insere uma chave int na árvore,
        retorna 0 em caso de erro e !0 caso contrário
        """
        if type(key) != int:
            raise TypeError
        c_key = ctypes.c_int(key)

        return lib.insert_key_avl(byref(self), c_key)

    def search_key(self, key):
        """
        Procura uma chave key na árvore,
        retorna 0 em caso de erro e !0 caso contrário
        """
        if type(key) != int:
            raise TypeError
        c_key = ctypes.c_int(key)

        return lib.search_key_avl(byref(self), c_key)

    def remove_key(self, key):
        """
        Remove uma chave da árvore,
        retorna 0 em caso de erro e !0 caso contrário
        """
        if type(key) != int:
            raise TypeError
        c_key = ctypes.c_int(key)

        return lib.remove_key_avl(byref(self), c_key)

    def print_tree(self):
        """
        Imprime a árvore in-order na saída padrão,
        retorna 0 em caso de erro e !0 caso contrário
        """
        return lib.print_tree_avl(byref(self))

    def print_tree_parenthesis(self):
        """Imprime a árvore com a notação de parenteses"""
        return lib.print_parethesis(byref(self))

    def print_with_height(self):
        """Imprime a árvore com a notação de altura"""
        return lib.print_with_height(byref(self))

    def print_graph(self):
        return lib.print_graph(byref(self))


    def as_parenthesis_string(self):
        """Retorna o texto de 'print_tree_parenthesis' como string"""
        size = len(self) * buffer_size
        string = ctypes.create_string_buffer(size)
        lib.string_parenthesis(byref(self), byref(string), size)
        ctypes.cast(string, ctypes.c_char_p)
        s = str(string.value)
        return s[2:-1]

    def as_height_string(self):
        """Retorna o texto de 'print_tree_by_height' como string"""
        size = len(self) * buffer_size
        string = ctypes.create_string_buffer(size)
        lib.string_height(byref(self), byref(string), size)
        ctypes.cast(string, ctypes.c_char_p)
        s = str(string.value)
        return s[2:-1]

    def size(self):
        """ Retorna o tamanho da árvore """
        return lib.tree_size(byref(self))

    def destroy(self):
        """Destroi a árvore, retorna 0 em caso de erro e !0 caso contrário"""
        return lib.destroy_tree_avl(byref(self))

    def __del__(self):
        """Destrutor de classe"""
        return self.destroy()

    def __str__(self):
        """Verificador usado pela funcao built-in 'print'"""
        return self.as_parenthesis_string()

    def __contains__(self, key):
        """ Verificador usado pelo operador 'in' """
        # Mais em docs/sources.txt: In Operator 
        return self.search_key(key)

    def __len__(self):
        """Verificador usado pela funcao built-in 'len()'"""
        return self.size()
