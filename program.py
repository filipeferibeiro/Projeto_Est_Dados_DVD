'''Project info'''
'''Imports'''
from functions import *
'''Variables'''
ji = BST()
'''Program'''
ji.insert(5,'Joãozinho','Madculino', 'Separado', 69)
ji.insert(3,'Joãozinh','Madculino', 'Separado', 25)
ji.insert(6,'Joãozin','Madculino', 'Separado', 24)
ji.insert(1,'Joãozi','Madculino', 'Separado', 32)
ji.insert(4,'Joãoz','Madculino', 'Separado', 2)
ji.insert(9,'Joã','Madculino', 'Separado', 7)
ji.insert(2,'Jo','Madculino', 'Separado', 10)
ji.insert(10,'guilhermeMERDA','Madculino', 'Separado', 10)

ji.inOrderTraversal()
ji.remove_node(6)
print(ji.get_informations(4).value)
print('')
ji.inOrderTraversal()
print('\n --------------')
print(ji.search(2,'Joãozinh'))