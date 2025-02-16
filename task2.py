from BTrees.OOBTree import OOBTree
import csv
import timeit
from random import randint

# Створення OOBTree
tree = OOBTree()

prod_dict = dict()


def add_item_to_tree(id, datadict):
    tree.update({id: datadict})


def add_item_to_dict(id, datadict):
    prod_dict[id] = datadict


with open("generated_items_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        add_item_to_tree(
            int(row[0]), {"name": row[1], "category": row[2], "price": row[3]}
        )
        add_item_to_dict(
            int(row[0]), {"name": row[1], "category": row[2], "price": row[3]}
        )


def range_query_tree(k_min=randint(0, 100000), k_max=randint(0, 100000)):
    if k_min > k_max:
        k_min, k_max - k_max, k_min
    return tree.items(k_min, k_max)


def range_query_dict(k_min=randint(0, 100000), k_max=randint(0, 100000)):
    result = {}
    if k_min > k_max:
        k_min, k_max - k_max, k_min
    k_min = k_min if min(prod_dict.keys()) < k_min else min(prod_dict.keys())
    k_max = k_max if max(prod_dict.keys()) > k_max else max(prod_dict.keys())
    for key in range(k_min, k_max + 1):
        result[key] = prod_dict[key]
    return result


def range_query_dict_lin(k_min=randint(0, 100000), k_max=randint(0, 100000)):
    result = {}
    if k_min > k_max:
        k_min, k_max - k_max, k_min
    k_min = k_min if min(prod_dict.keys()) < k_min else min(prod_dict.keys())
    k_max = k_max if max(prod_dict.keys()) > k_max else max(prod_dict.keys())
    for key in prod_dict.keys():
        if k_min < key < k_max:
            result[key] = prod_dict[key]
    return result


# Пошук об'єктів
# print(tree.get(19896))  # Виведе 'red'
# print(tree.get(5, 'not found'))  # Виведе 'not found'

# # Видалення об'єктів
# del tree[86432]

# Перегляд усіх об'єктів
# for key, value in tree.items():
#     print(key, value)

print("Total range_query time for OOBTree:")
print(
    timeit.timeit(
        "range_query_dict()", setup="from __main__ import range_query_dict", number=100
    )
)

print("Total range_query time for Dict:")
print(
    timeit.timeit(
        "range_query_tree()", setup="from __main__ import range_query_tree", number=100
    )
)

print("Total range_query time for Dict linear:")
print(
    timeit.timeit(
        "range_query_dict_lin()",
        setup="from __main__ import range_query_dict_lin",
        number=100,
    )
)
