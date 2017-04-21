'''Project info'''
'''Imports'''
from functions import *
'''Variables'''
ji = BST()
'''Program'''
ji.insert(5,'Duro de matar','ação', 'disponivel', 2)
ji.insert(3,'Pôneis malditos','irritante', 'alugado', 2)
ji.insert(6,'XXX - gretchen','pornô', 'alugado', 2)
ji.insert(1,'Dumb','animação', 'disponivel', 3)
ji.insert(4,'João e o pé de feijão','animação', 'disponivel', 2)
ji.insert(9,'Power rangers','ação/ficção', 'alugado', 4)
ji.insert(2,'meu pé esquerdo','drama', 'disponivel', 2)
ji.insert(10,'festa na piscina','porno', 'alugado', 4)

ji.inOrderTraversal()
print('\n -----------------')
print(ji.search(1,4),'\n ------------------------')
ji.inOrderTraversal()
print('\n -----------------')
print(ji.search(2,'João e o pé de feijão'))