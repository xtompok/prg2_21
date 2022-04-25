
from this import d


class Node(object):
	def __init__(self,data) -> None:
		self.data = data
		self.left : Node = None
		self.right : Node = None
		self.parent : Node = None

	def __str__(self):
		return f"Node {id(self)}: {self.data}, left: {id(self.left)}, right: {id(self.right)}, parent: {id(self.parent)}"

class BinaryTree(object):
	def __init__(self) -> None:
		self.root : Node = None
	
	def __str__(self) -> str:
		return f"BinaryTree {id(self)}: root: {id(self.root)}"

class BinarySearchTree(BinaryTree):
	def insert(self, data) -> None:
		if not self.root:
			self.root = Node(data)	
			return
		cur = self.root
		while True:
			if data < cur.data:
				if cur.left:
					cur = cur.left
				else:
					cur.left = Node(data)
					return
			elif data > cur.data:
				if cur.right:
					cur = cur.right
				else:
					cur.right = Node(data)
					return
			else:
				return
		# Pokud kořen neexistuje, vytvořím ho a jsem hotov
		# Pokud kořen existuje, držím si aktuální vrchol a podle jeho hodnoty se pohybuji stromeme
		# Když se mám pohnout do neexistujícího syna, vyrobím nový vrchol a připojím ho do stromu
		pass
	
	def query(self, data) -> bool:
		# Pokud kořen neexistuje, vracím False
		# Pokud kořen existuje, držím si aktuální vrchol a podle jeho hodnoty se pohybuji stromeme
		# Když najdu hledanou hodnotu, vrátím True
		# Když najdu prázdného syna, vrátím False
		pass


n1 = Node(1)
n2 = Node(2)

print(id(None))
print(n1)
print(n2)

n1.right = n2
n2.parent = n1

print(n1)
print(n2)

tree = BinaryTree()
tree.root = n1

print(tree)