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

    def search(self, type_search, data, root = -1):
        if type_search == 1: #Search by Code
            elements = self.get_informations(data)
            if elements != False:
                return (data, elements.name, elements.gender, elements.state, elements.value)
            else:
                return 'Filme não encontrado.'
        elif type_search == 2: #Search by Name
            if (root == -1):
                root = self.root
            elements = None
            dados = None
            if root.left is not None:
                elements = self.search(type_search, data, root.left)
            if dados is None:
                dados = elements
            if root.right is not None:
                elements = self.search(type_search, data, root.right)
            if root.informations.name is data:
                elements = root.informations
                return(root.code, elements.name, elements.gender, elements.state, elements.value)
            if dados is None:
                dados = elements
            return dados


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

