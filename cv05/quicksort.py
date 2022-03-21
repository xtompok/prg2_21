def swap(alist: list, l:int, r:int, pivot)->tuple:
	""" Prohodi prvky v `alist` tak, aby na zacatku byly mensi nez pivot a na konci vetsi nez pivot
	Vraci, kdyz se indexy prohodi, tedy `i` je alespoň tak vpravo jako `j`.
	"""
	i = l
	j = r
	while i < j:
		# Posouvame levou hranici doprava
		while alist[i] < pivot:
			i+=1
		# Posouvame pravou hranici doleva
		while alist[j] > pivot:
			j-=1
		# Pokud se indexy prekrizily, koncime
		if i > j:
			return i,j
		# Jinak mame 2 kandidaty na prohozeni
		# Prohodime je
		tmp = alist[i]
		alist[i] = alist[j]
		alist[j] = tmp
		# A posuneme indexy, protoze po prohozeni jsou hotovy
		i+=1
		j-=1

	return i,j

def qs(alist: list, l:int, r:int):
	# kontrola indexu, jestli nejsou prekrizene nebo netridime jednoprvkovy seznam
	if l >= r:
		return
	# volba pivota - prvek uprostred aktualne zpracovavane casti
	pivot = alist[(l+r)//2]
	# swap - nalezneme hranice pro rekurzi
	i,j = swap(alist, l, r, pivot)
	# qs() na levou část
	qs(alist,l,j)
	# qs() na pravou část
	qs(alist,i,r)

def quicksort(alist):
	""" Sorts given list using quicksort"""
	qs(alist, 0, len(alist)-1)

l = [3,2,1]
quicksort(l)
print(l)

