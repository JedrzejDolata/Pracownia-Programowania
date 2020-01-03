# implementacja drzewa binarnego wyszukiwania (BST)
# autor: Jędrzej Dolata 2D
# pracownia programowania, prof. Kowalewski
# program moze tworzyć drzewo; dodawać elementy pojedynczo, lub wiele na raz; drukować drzewo w dwóch postaciach; usuwać elementy drzewa; sprawdzać, czy element występuje w drzewie
# program nie jest w stanie usunąć elementu bazowego (w przykładzie uzycia jest to 64) ze względu na ograniczenia języka
# moznaby uciec co C i podmienić komórki pamięci, ale sądzę ze nie o to Panu chodziło
# wszystkie zmienne i funkcje nazwane są po angielsku, poniewaz osobiście preferuję takie nazewnictwo

# definiuje klasę, umoliwia dodanie drzewa

class Node:
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# drukuje drzewo w wielu liniach, w kolejności rosnącej

def printMe(node):
    if node:
        printMe(node.left)
        print(node.val)
        printMe(node.right)

# drukuje drzewo w jednej linii, pokazuje węzły w nawiasach

def printTree(node):
    if node:
        print(node.val, end = '')
        print(" ( ", end = '')
        printTree(node.left)
        print(" ) ( ", end = '')
        printTree(node.right)
        print(" ) ", end = '')

# dodaje pojedynczy element do drzewa

def addNode(node, key):
    if node.val < key.val:
        if node.right:
            addNode(node.right, key)
        else:
            node.right = key
    else:
        if node.left:
            addNode(node.left, key)
        else:
            node.left = key

# dodaje wiele elementów na raz, wprowadzane w postaci zmiennej typu list

def addList(node, keys):
    for i in keys:
        addNode(node, Node(i))

# wyszukuje element w drzewie, True lub False, w zależności od tego, czy element istnieje

def search(node, key):
    if node.val < key:
        if node.right:
            if node.right.val == key:
                return True
            else:
                return search(node.right, key)
        else:
            return False
    else:
        if node.left:
            if node.left.val == key:
                return True
            else:
                return search(node.left, key)
        else:
            return False

# usuwa dany element drzewa

def removeKey(node, key):
    foundNode = node
    motherNode = None
    isFound = False
    while not isFound:
        if key > foundNode.val:
            if foundNode.right:
                motherNode = foundNode
                foundNode = foundNode.right
            else:
                return False
        elif key < foundNode.val:
            if foundNode.left:
                motherNode = foundNode
                foundNode = foundNode.left
            else:
                return False
        elif foundNode.val == key:
            isFound = True
    if not foundNode.left and not foundNode.right:
        if foundNode.val < motherNode.val:
            motherNode.left = None
        else:
            motherNode.right = None
    elif not foundNode.right:
        motherNode.left = foundNode.left
    elif not foundNode.left:
        motherNode.right = foundNode.right
    else:
        predecessor = foundNode.left
        predecessorMotherNode = foundNode
        while predecessor.right:
            predecessorMotherNode = predecessor
            predecessor = predecessor.right
        foundNode.val = predecessor.val
        predecessorMotherNode.right = predecessor.left
    return True

#przykład uzycia

drzewko = Node(64)
addNode(drzewko, Node(8))
addList(drzewko,[2, 13, 40, 32, 115, 6, 16, 83, 234, 103, 980, 979])
print(search(drzewko, 13))
printMe(drzewko)
removeKey(drzewko, 13)
print(search(drzewko, 13))
printTree(drzewko)
