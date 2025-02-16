from collections import deque


# Функція для пошуку збільшуючого шляху (BFS)
def bfs(capacity_matrix, flow_matrix, source, sink, parent):
    visited = [False] * len(capacity_matrix)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(capacity_matrix)):
            # Перевірка, чи є залишкова пропускна здатність у каналі
            if (
                not visited[neighbor]
                and capacity_matrix[current_node][neighbor]
                - flow_matrix[current_node][neighbor]
                > 0
            ):
                parent[neighbor] = current_node
                visited[neighbor] = True
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False


# Основна функція для обчислення максимального потоку
def edmonds_karp(capacity_matrix, source, sink):
    num_nodes = len(capacity_matrix)
    flow_matrix = [
        [0] * num_nodes for _ in range(num_nodes)
    ]  # Ініціалізуємо матрицю потоку нулем
    parent = [-1] * num_nodes
    max_flow = 0

    # Поки є збільшуючий шлях, додаємо потік
    while bfs(capacity_matrix, flow_matrix, source, sink, parent):
        # Знаходимо мінімальну пропускну здатність уздовж знайденого шляху (вузьке місце)
        path_flow = float("Inf")
        current_node = sink

        while current_node != source:
            previous_node = parent[current_node]
            path_flow = min(
                path_flow,
                capacity_matrix[previous_node][current_node]
                - flow_matrix[previous_node][current_node],
            )
            current_node = previous_node

        # Оновлюємо потік уздовж шляху, враховуючи зворотний потік
        current_node = sink
        while current_node != source:
            previous_node = parent[current_node]
            flow_matrix[previous_node][current_node] += path_flow
            flow_matrix[current_node][previous_node] -= path_flow
            current_node = previous_node

        # Збільшуємо максимальний потік
        max_flow += path_flow

    return max_flow


# Матриця пропускної здатності для каналів у мережі (capacity_matrix)

capacity_matrix = [
    # I  1  2  1  2  3  4  1  2  3  4  5  6  7  8  9  0  1  2  3  4  O
    [
        0,
        float("Inf"),
        float("Inf"),
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # Повний вхід  0
    [
        0,
        0,
        0,
        25,
        20,
        15,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # Термінал 1   1
    [
        0,
        0,
        0,
        0,
        10,
        15,
        30,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # Термінал 2   2
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        15,
        10,
        20,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # Склад 1      3
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        15,
        10,
        25,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # Склад 2      4
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        20,
        15,
        10,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # Склад 3      5
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        20,
        10,
        15,
        5,
        10,
        0,
    ],  # Склад 4      6
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 1    7
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 2    8
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 3    9
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 4    10
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 5    11
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 6    12
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 7    13
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 8    14
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 9    15
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 10   16
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 11   17
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 12   18
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 13   19
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        float("Inf"),
    ],  # Магазин 14   20
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ],  # Загальні продажі  21
    # 1  2  1  2  3  4  1  2  3  4  5  6  7  8  9  0  1  2  3  4
]


stor = {}
stor2 = {}
for i in range(3, 7):
    stor[i] = edmonds_karp(capacity_matrix, 0, i)
    stor2[i] = stor[i]


shop = {}
shop2 = {}
shop3 = {}

for i in range(7, 21):
    shop[i] = edmonds_karp(capacity_matrix, 0, i)
    for j in range(3, 7):
        if capacity_matrix[j][i] != 0:
            if stor[j] >= shop[i] > 0:
                shop2[i] = shop[i]
                stor[j] -= shop[i]
                stor2[j] -= shop[i]
            elif stor[j] < shop[i]:
                shop2[i] = stor[j]
                stor[j] = 0
                stor2[j] -= shop[i]
            else:
                shop2[i] = 0

source = 0  # Повний вхід
sink = 21  # Повний вихід

print(f"Максимальний потік усієї мережі: {edmonds_karp(capacity_matrix, source, sink)}")

print("Максимальний потік від терміналу до магазину")
for i in range(1, 3):
    for j in range(7, 20):
        print(f"Термінал {i}: Магазин {j-6} {edmonds_karp(capacity_matrix, i, j)}")


print("Максимальний потік від терміналу")
for i in range(1, 3):
    print(f"Термінал {i}: Найбільший потік {edmonds_karp(capacity_matrix, i, 21)}")


print("Максимальний потік до магазину")
for sh_k, sh_v in shop.items():
    print(f"Магазин {sh_k-6} {sh_v}")

print("Реальний потік до магазину (по порядку)")
for sh_k, sh_v in shop2.items():
    print(f"Магазин {sh_k-6} {sh_v}")


print("Можливість збільшення потоку через склади для заповнення усіх магазинів")
for sh_k, sh_v in stor2.items():
    print(f"Склад {sh_k-2} {-sh_v}")

import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.DiGraph()

# Додаємо ребра з пропускною здатністю
edges = [
    ("Термінал 1", "Склад 1", 25),  # Термінал 1 -> Склад 1
    ("Термінал 1", "Склад 2", 20),  # Термінал 1 -> Склад 2
    ("Термінал 1", "Склад 3", 15),  # Термінал 1 -> Склад 3
    ("Термінал 2", "Склад 2", 10),  # Термінал 2 -> Склад 2
    ("Термінал 2", "Склад 3", 15),  # Термінал 2 -> Склад 3
    ("Термінал 2", "Склад 4", 30),  # Термінал 2 -> Склад 4
    ("Склад 1", "Магазин 1", 15),  # Склад 1 -> Магазин 1
    ("Склад 1", "Магазин 2", 10),  # Склад 1 -> Магазин 2
    ("Склад 1", "Магазин 3", 20),  # Склад 1 -> Магазин 3
    ("Склад 2", "Магазин 4", 15),  # Склад 2 -> Магазин 4
    ("Склад 2", "Магазин 5", 10),  # Склад 2 -> Магазин 5
    ("Склад 2", "Магазин 6", 25),  # Склад 2 -> Магазин 6
    ("Склад 3", "Магазин 7", 20),  # Склад 3 -> Магазин 7
    ("Склад 3", "Магазин 8", 15),  # Склад 3 -> Магазин 8
    ("Склад 3", "Магазин 9", 10),  # Склад 3 -> Магазин 9
    ("Склад 4", "Магазин 10", 20),  # Склад 3 -> Магазин 10
    ("Склад 4", "Магазин 11", 10),  # Склад 3 -> Магазин 11
    ("Склад 4", "Магазин 12", 15),  # Склад 3 -> Магазин 12
    ("Склад 4", "Магазин 13", 5),  # Склад 3 -> Магазин 13
    ("Склад 4", "Магазин 14", 10),  # Склад 3 -> Магазин 14
]

# Додаємо всі ребра до графа
G.add_weighted_edges_from(edges)

# Позиції для малювання графа
pos = {
    "Термінал 1": (1, 2),  # Термінал 1
    "Термінал 2": (5, 2),  # Термінал 2
    "Склад 1": (2, 3),  # Склад 1
    "Склад 2": (4, 3),  # Склад 2
    "Склад 3": (2, 1),  # Склад 3
    "Склад 4": (4, 1),  # Склад 4
    "Магазин 1": (0, 4),  # Магазин 1
    "Магазин 2": (1, 4),  # Магазин 2
    "Магазин 3": (2, 4),  # Магазин 3
    "Магазин 4": (3, 4),  # Магазин 4
    "Магазин 5": (4, 4),  # Магазин 5
    "Магазин 6": (5, 4),  # Магазин 6
    "Магазин 7": (0, 0),  # Магазин 7
    "Магазин 8": (1, 0),  # Магазин 8
    "Магазин 9": (2, 0),  # Магазин 9
    "Магазин 10": (3, 0),  # Магазин 10
    "Магазин 11": (4, 0),  # Магазин 11
    "Магазин 12": (5, 0),  # Магазин 12
    "Магазин 13": (6, 0),  # Магазин 13
    "Магазин 14": (7, 0),  # Магазин 14
}

mapping = {
    0: "Термінал 1",
    1: "Термінал 2",
    2: "Склад 1",
    3: "Склад 2",
    4: "Склад 3",
    5: "Склад 4",
    6: "Магазин 1",
    7: "Магазин 2",
    8: "Магазин 3",
    9: "Магазин 4",
    10: "Магазин 5",
    11: "Магазин 6",
    12: "Магазин 7",
    13: "Магазин 8",
    14: "Магазин 9",
    15: "Магазин 10",
    16: "Магазин 11",
    17: "Магазин 12",
    18: "Магазин 13",
    19: "Магазин 14",
}
H = nx.relabel_nodes(G, mapping)

# Малюємо граф
plt.figure(figsize=(10, 6))
nx.draw(
    H,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="lightgreen",
    font_size=12,
    font_weight="bold",
    arrows=True,
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Відображаємо граф
plt.show()
