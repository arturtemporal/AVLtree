#!/usr/bin/env python3

# declara o objeto libc, para podermos utilizar diretamente funções padrões de C
import ctypes
avl = ctypes.CDLL("./avl_module.so")

# avl.initialize_avl();
# print(avl.avl_teste())
# avl.avl_soma_teste(1, 3)
print(avl.teste_avl())