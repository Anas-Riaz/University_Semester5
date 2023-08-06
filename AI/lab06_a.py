import itertools
def tsp(list_of_nodes):
    start = 1
    cities = list(range(2, len(list_of_nodes)+ 1))
    permutations = itertools.permutations(cities)
    min_cost = float('inf')
    best_permutations = None
    for perm in permutations:
        cost = 0
        current_city = start
        for city in perm:
            cost += list_of_nodes[current_city - 1][city - 1]
            current_city = city
        cost += list_of_nodes[current_city - 1][start - 1]
        if cost < min_cost:
            min_cost = cost
            best_permutations = (start,) + perm + (start,)
    return best_permutations, min_cost
graph = [
    [1, 0, 2, 5],
    [6, 5, 8, 4],
    [7, 8, 3, 1],
    [1, 8, 9, 0]
]
print(tsp(graph))
