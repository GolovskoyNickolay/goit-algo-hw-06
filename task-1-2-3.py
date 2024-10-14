import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф для моделювання транспортної мережі міста
G = nx.Graph()

# Додаємо вершини (наприклад, транспортні вузли: станції метро, автобусні зупинки)
stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F']

# Додаємо вершини до графа
G.add_nodes_from(stations)

# Додаємо ребра (зв'язки між станціями, наприклад, дороги або лінії метро)
edges = [('Station A', 'Station B'),
         ('Station A', 'Station C'),
         ('Station B', 'Station D'),
         ('Station C', 'Station D'),
         ('Station D', 'Station E'),
         ('Station E', 'Station F')]

# Додаємо ребра до графа
G.add_edges_from(edges)

# Візуалізуємо граф
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=2000, font_size=12)
plt.title('Transport Network Graph')
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()  # кількість вершин
num_edges = G.number_of_edges()  # кількість ребер
degree_centrality = nx.degree_centrality(G)  # ступінь вершин

# Повертаємо характеристики графа
print('task1', num_nodes, num_edges, degree_centrality)


# Функції для виконання DFS і BFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

# Виконання пошуку шляху для графа, розробленого раніше
start_node = 'Station A'
goal_node = 'Station F'

# Знаходження шляхів з A до F
dfs_result = list(dfs_paths(G, start_node, goal_node))
bfs_result = list(bfs_paths(G, start_node, goal_node))

# DFS (Пошук у глибину) знайшов два шляхи:
#
# Station A → Station C → Station D → Station E → Station F
# Station A → Station B → Station D → Station E → Station F
# BFS (Пошук у ширину) також знайшов два шляхи:
#
# Station A → Station B → Station D → Station E → Station F
# Station A → Station C → Station D → Station E → Station F

# Різниця між результатами:
# DFS використовує пошук у глибину, тобто спершу досліджує найглибші можливі шляхи, а потім повертається до менш глибоких. В результаті, перший шлях DFS проходить через Station C, оскільки цей вузол опрацьовується раніше.
# BFS, на відміну від DFS, спочатку обробляє всі вузли на найближчому рівні (рівні 1), тому його перший шлях проходить через Station B. BFS гарантує знаходження найкоротшого шляху в термінах кількості ребер, оскільки обробляє вершини по рівнях.
# Висновок:
# BFS забезпечує, що перший знайдений шлях є мінімальним у кількості ребер, тоді як DFS може знайти глибші шляхи, які не обов'язково є найкоротшими

print('task 2', dfs_result, bfs_result)


# Додаємо ваги до ребер графа (наприклад, вага = довжина дороги між станціями)
weighted_edges = [
    ('Station A', 'Station B', 4),
    ('Station A', 'Station C', 2),
    ('Station B', 'Station D', 5),
    ('Station C', 'Station D', 8),
    ('Station D', 'Station E', 6),
    ('Station E', 'Station F', 3)
]

# Очищаємо ребра графа і додаємо нові з вагами
G.clear()
G.add_weighted_edges_from(weighted_edges)

# Функція для знаходження найкоротшого шляху за допомогою алгоритму Дейкстри
def dijkstra_all_pairs_shortest_paths(graph):
    return dict(nx.all_pairs_dijkstra_path(graph))

# Знаходимо найкоротші шляхи між всіма вершинами
shortest_paths = dijkstra_all_pairs_shortest_paths(G)

# Візуалізація графа з вагами
pos = nx.spring_layout(G)  # Позиція для вузлів
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Transport Network with Weights')
plt.show()

print('task 3', shortest_paths)


