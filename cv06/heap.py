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
	idx = len(heap)-1
	# dokud nejsem v koreni
	while idx > 1:
	# 	podivam se na rodice
		pidx = parent(idx)
	# 	pokud rodic je mensi nez ja, koncim
		if heap[pidx] <= heap[idx]:
			return
	# 	jinak
		if idx % 2 == 0:
			if len(heap) - 1 == idx:
				idx2 = idx
			else:
				idx2 = idx + 1
		else:
			idx2 = idx - 1
	# 		prohodim rodice s mensim ze synu
		if heap[idx] < heap[idx2]:
			temp = heap[idx]
			heap[idx] = heap[idx//2]
			heap[idx//2] = temp
		else:
			temp = heap[idx2]
			heap[idx2] = heap[idx//2]
			heap[idx//2] = temp
	# 		posunu se na pozici rodice
		idx = idx // 2

def lchld(me: int):
	""" Get index of my left child"""
	return me*2

def rchld(me: int):
	""" Get index of my right child"""
	return me*2+1

def parent(me: int):
	""" Get mine parent"""
	return me//2


heap = [None]
insert(heap,29)
insert(heap,14)
print(heap)
