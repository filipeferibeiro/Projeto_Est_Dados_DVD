class BST:
    def __init__(self):
        self.root = None

    def insert(self, code, name, gender, state, value, root=-1):
        if root == -1:
            self.root = self.insert(code, name, gender, state, value, self.root)
            return
        else:
            if root == None:
                root = TreeNode(code, name, gender, state, value)
            elif code > root.code:
                root.right = self.insert(code, name, gender, state, value, root.right)
            elif code < root.code:
                root.left = self.insert(code, name, gender, state, value, root.left)
            return root

    def balanced(self, root = -1): # está funcionando
        if self.root is None:
            return None
        if root is -1:
            root = self.root
        ji = 0
        ji2 = 0
        if root.left is not None:
            ji = self.balanced(root.left)
        if root.right is not None:
            ji2 = self.balanced(root.right)
        if ji is not 0:
            return ji
        if ji2 is not 0:
            return ji2
        if root.left is None and root.right is None:
            return 0
        else:
            esq = self.ObterAltura(root.left)
            dir = self.ObterAltura(root.right)
            if (esq - dir) >= 2 or (dir - esq) >= 2:
                return root.code
            else:
                return 0

    def ObterAltura(self, root=-1):
        if self.root is None:
            return
        if root is -1:
            root = self.root
        if root is None:
            return 0
        maioraltura = 0
        altura = 0
        if root.left is not None:
            altura = self.ObterAltura(root.left)
        if altura > maioraltura:
            maioraltura = altura
        if root.right is not None:
            altura = self.ObterAltura(root.right)
        if altura > maioraltura:
            maioraltura = altura

        return (maioraltura + 1)




    def search(self, type_search, data, root = -1):
        if type_search == 1: #Search by Code
            elements = self.get_informations(data)
            if elements != False:
                return (data, elements.name, elements.gender, elements.state, elements.value)
            else:
                return None
        elif type_search == 2: #Search by Name
            if self.root == None:
                return None
            if (root == -1):
                root = self.root
            elements = None
            dados = None
            if root.left is not None:
                elements = self.search(type_search, data, root.left)
            if dados is None:
                dados = elements
            if dados is not None:
                return dados
            if root.right is not None:
                elements = self.search(type_search, data, root.right)
            if root.informations.name is data:
                elements = root.informations
                return(root.code, elements.name, elements.gender, elements.state, elements.value)
            if dados is None:
                dados = elements
            if dados is not None:
                return dados
            return dados

    #def login(self, user, password, database):
     #   if user in database:
      #      if password is



    def get_informations(self, code):
        root = self.root
        while root != None and root.code != code:
            if code > root.code:
                root = root.right
            else:
                root = root.left
        if root == None:
            return False
        else:
            return root.informations

    def minValue(self, root=-1):
        if (root == -1):
            root = self.root

        if (root is None):
            return None

        while (root.left is not None):
            root = root.left

        return root

    def remove_node(self, code, informations = -1, root=-1):
        if (root == -1):
            root = self.root
            if root != None:
                if (informations == -1):
                    informations = self.get_informations(code)
            root = self.remove_node(code, informations, self.root)

        else:
            if root == None:
                return root
            if code < root.code:
                root.left = self.remove_node(code, informations, root.left)
                return root
            if code > root.code:
                root.right = self.remove_node(code, informations, root.right)
                return root
            else:
                if root.left == None and root.right == None:
                    return None
                elif root.left == None or root.right == None:
                    if root.left != None:
                        return root.left
                    else:
                        return root.right
                else:
                    next = self.minValue(root.right)
                    tempCode = root.code
                    tempInformations = root.informations
                    root.code = next.code
                    root.informations = next.informations
                    next.code = tempCode
                    next.informations = tempInformations
                    root.right = self.remove_node(tempCode, tempInformations, root.right)
                    return root

    def inOrderTraversal(self, root=-1):
        if (root == -1):
            root = self.root

        if (root is not None):
            self.inOrderTraversal(root.left)
            print(root.code, root.informations.name, end=' ')
            self.inOrderTraversal(root.right)

class TreeNode:
    def __init__(self, code, name, gender, state, value):
        self.code = code
        self.informations = NodeInformations(name, gender, state, value)
        self.left = None
        self.right = None

class NodeInformations:
    def __init__(self, name, gender, state, value):
        self.name = name
        self.gender = gender
        self.state = state
        self.value = value

