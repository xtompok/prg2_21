import geopandas
import networkx as nx
import matplotlib.pyplot as plt


# Prevod GeoJSONu na graf. Kazdy lomovy bod je vrcholem grafu
# Vstupni GeoJSON by mel byt tvoren LineStringy

# GeoPandas umi nacitat mnoho ruznych geoformatu
gdf = geopandas.read_file("test.geojson")

# Vytvorime prazdny obycejny graf
# existuji ruzne druhy grafu, viz https://networkx.org/documentation/stable/reference/classes/graph.html#networkx.Graph
G = nx.Graph()

# Prochazime jednotlive prvky vstupnich dat, iterrows() vraci dvojice (index:int, df: GeoSeries)
for idx, r in gdf.iterrows():
	# Vytahneme souradnice z GeoSeries
	coords = r.geometry.coords
	print(coords)
	
	# Zapamatujeme si souradnice prvniho bodu
	mempoint = coords[0]

	# Prochazime lomove body od druheho dale
	for point in coords[1:]:
		# Pridame do grafu hranu mezi minulym a soucasnym bodem, nastavime atribut `index` na index linestringu
		# Vrcholy neni treba explicitne vytvaret, vzniknou automaticky. Jmenem vrcholu je dvojice souradnic
		G.add_edge(mempoint, point,index=idx)
		# Posuneme predchozi bod na soucasny
		mempoint = point

# Vypis strucnych informaci o grafu
print(nx.info(G))
# Vykresleni grafu. Slovnik predavany jako argument pos obsahuje jako klice jmena vrcholu a jako hodnoty souradnice vrcholu. 
# Pozice vrcholu v grafu pak odpovidaji skutecnym pozicim. 
nx.draw(G,pos = {n: [n[0],n[1]] for n in list(G.nodes)},with_labels = True)

# Aby se vykresleny graf ukazal, je potreba zavolat plt.show(), protoze vykresleni probehne pomoci matplotlib
plt.show()
