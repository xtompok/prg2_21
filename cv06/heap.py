# Halda

def insert(heap: list,item):
	""" Inserts item into the heap"""
	# Vlozime na konec haldy
	heap.append(item)
	# Opravime haldovou podminku na usporadani
	fixUp(heap)

def fixUp(heap):
	"""Fix heap condition upwards"""
	# Nemusime predavat index, protoze pokud opravujeme smerem nahoru,
	# tak je to po pridani noveho prvku a ten vime, ze je uplne na konci.

	# dokud nejsem v koreni
	# 	podivam se na rodice
	# 	pokud rodic je mensi nez ja, koncim
	# 	jinak 
	# 		prohodim rodice s mensim ze synu
	# 		posunu se na pozici rodice

def lchld(me: int):
	""" Get index of my left child"""
	return me*2

def rchld(me: int):
	""" Get index of my right child"""
	return me*2+1

def parent(me: int):
	""" Get mine parent"""
	return me//2
