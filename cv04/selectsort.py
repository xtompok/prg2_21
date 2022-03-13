# Strings are sorted lexicographically, according to the position in Unicode,
# not according to locale-specific ordering
alist = ['a', 'b', 'z', 'y', 'e', 'š', 'ch']


def selectsort(alist: list) -> list:
	""" Not-inplace select sort. Destroys original list and returns new
	sorted list"""

	output = []
	# Find minimum n times and add it to the new list
	for i in range(len(alist)):
		# Choose first list element as a minimum candidate
		amin = alist[0]
		aminidx = 0
		# Iterate over list and update minimum
		for idx, val in enumerate(alist):
			if val < amin:
				amin = val
				aminidx = idx
		# Remove minimum from original list
		alist.pop(aminidx)
		# Append minimum to the output list
		output.append(amin)
	return output
	

def inplace_selectsort(alist: list)->None:
	""" Inplace select sort. Modifies input list, returns nothing."""
	# Find minimum n times and move it to the appropriate position
	for i in range(len(alist)):
		# Choose first uprocessed element as minimum candidate
		amin = alist[i]
		aminidx = i
		# Iterate over uprocessed elements and update minimum
		for j in range(i,len(alist)):
			if alist[j] < amin:
				amin = alist[j]
				aminidx = j
		# Swap minimum with the first uprocessed element thus process it
		alist[aminidx] = alist[i]
		alist[i] = amin

print(f"Original list: {alist}")
print(f"Copy selectsort: {selectsort(list(alist))}")
inplace_selectsort(alist)
print(f"Inplace selectsort: {alist}") 

