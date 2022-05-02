# NetworkX je knihovna pro praci s grafy v Pythonu. Obsahuje mnozstvi funkci pro
# prochazeni grafu, hledani komponent, hledani cest a dalsi
import networkx as  nx
# Matplotlib slouzi pro kresleni grafu (funkci i grafu)
import matplotlib.pyplot as plt

# Vytvoreni prazdneho grafu
G = nx.Graph()

# Pridame vrcholy
G.add_node(1)
G.add_node(3)
# Pridame hranu
G.add_edge(1,3)
G.add_node(2)
# Pridame hranu s atributem `weight`
G.add_edge(1,2,weight = 2)

# Strucne informace o grafu
print(nx.info(G))
# Vypiseme jmena vrcholu 
print(G.nodes)
# Vypiseme hrany
print(G.edges)
# Vypiseme hodnotu atributu hrany
print(G.edges[(1,2)]["weight"])

# Vykreslime graf, vrcholy budou mit popisky podle svych jmen
nx.draw(G,with_labels = True)

# Abychom videli vykresleny graf, je potreba zavolat plt.show()
plt.show()
