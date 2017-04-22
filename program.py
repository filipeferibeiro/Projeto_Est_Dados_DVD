'''Project info'''
'''Imports'''
from functions import *
'''Variables'''
Tree = BST()
'''Program'''
Tree.insert(5,'Duro de matar','ação', 'disponivel', 2)
Tree.insert(3,'Pôneis malditos','irritante', 'alugado', 2)
Tree.insert(6,'XXX - gretchen','pornô', 'alugado', 2)
Tree.insert(1,'Dumb','animação', 'disponivel', 3)
Tree.insert(4,'João e o pé de feijão','animação', 'disponivel', 2)
Tree.insert(9,'Power rangers','ação/ficção', 'alugado', 4)
Tree.insert(2,'meu pé esquerdo','drama', 'disponivel', 2)
Tree.insert(10,'festa na piscina','porno', 'alugado', 4)

Tree.inOrderTraversal()
print('\n -----------------')
print(Tree.search(1,4),'\n -----------------')
Tree.inOrderTraversal()
print('\n -----------------')
print(Tree.search(2,'João e o pé de feijão'))

