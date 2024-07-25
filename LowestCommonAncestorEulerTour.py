class TreeNode:
    def __init__(self, index, parent=None):
        self.index = index
        self.parent = parent
        self.children = []
        self.n = None

    def addChildren(self, nodes):
        self.children.append(nodes)

    def setSize(self, n):
        self.n = n

    def size(self):
        return self.n
    
    def index(self):
        return self.index
    
    def parent(self):
        return self.parent
    
    def children(self):
        return self.children
    
    def rootTree(graph, rootId):
        root = TreeNode(rootId)
        rootedTree = buildTree(graph, root)
        if rootedTree.size() < graph.size():
            print("WARNING: Input graph malformed. Did you forget to include all n-1 edges?")
        return rootedTree
    
    def buildTree(graph, node):
        subtreeNodecount = 1
        for neighbor in range(graph.get(node.index())):
            if node.parent() != None and neighbor == node.parent().index():
                continue

            child = TreeNode(neighbor, node)
            node.addChildren(child)

            buildTree(graph, child)
            subtreeNodecount += child.size()
        node.setSize(subtreeNodecount)
        return node
    
x = TreeNode(5)
