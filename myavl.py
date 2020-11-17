#!/usr/bin/env python3

from avl_bridge import avl_tree
tree = avl_tree()

def process_input(s):

    try:
        command, arguments = s.split(maxsplit=1)
    except ValueError:
        command = s

    if (command == "p"): # imprime a arvore
        print(tree)
        return 1

    try:
        n = int(arguments)
    except:
        return 0

    if (command == "i"): # input na árvore 
        tree.insert_key(n)
    elif (command == "r"): # remove da árvore
        tree.remove_key(n)
    elif (command == "s"): # pesquisa na arvore
        print(n in tree)
    else:
        return 0

    return 1

if __name__ == '__main__':
    try:
        line = input()
        while (line): # linha nao eh vazia
            if (not process_input(line)):
                print("Input inválido!")
            line = input()
    except EOFError:
        pass

    tree.print_tree_parenthesis()
