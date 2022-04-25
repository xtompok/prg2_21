data = [{"name": "Anna", "age": 15}, {"name": "Bedřich", "age": 10}]

def name(item):
	return item['name']

def age(item):
	return item['age']

print(data)
data.sort(key = lambda it : it['coordinates'][0] )
print(data)