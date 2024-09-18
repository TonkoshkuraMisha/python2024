import networkx as nx
from collections import Counter
import random


def restore_list(slices):
    # Шаг 1: Найдем все уникальные числа и их частоты
    unique_numbers = set()
    frequency = Counter()

    for slc in slices:
        unique_numbers.update(slc)
        frequency.update(slc)

    # Шаг 2: Построим ориентированный граф
    graph = nx.DiGraph()
    graph.add_nodes_from(unique_numbers)

    for slc in slices:
        for i in range(2):
            graph.add_edge(slc[i], slc[i + 1])

    # Проверка на циклы в графе
    try:
        topological_order = list(nx.topological_sort(graph))
    except nx.NetworkXUnfeasible:
        # Граф содержит цикл. Найдем сильно связанные компоненты (SCC).
        scc = list(nx.strongly_connected_components(graph))
        print(f"Обнаружены циклы, сильно связанные компоненты: {scc}")

        # Разрешаем циклы, случайным образом выбирая порядок для чисел из циклов
        for component in scc:
            if len(component) > 1:
                for node in component:
                    # Удаляем циклические связи
                    successors = list(graph.successors(node))
                    for succ in successors:
                        if succ in component:
                            graph.remove_edge(node, succ)

        # Пробуем снова после удаления циклов
        topological_order = list(nx.topological_sort(graph))

    # Шаг 3: Проверим частоты и восполним числа, если нужно
    result = []
    used = Counter()

    for num in topological_order:
        while used[num] < frequency[num]:
            result.append(num)
            used[num] += 1

    return result


# Пример с кортежами
reels1 = [(80,15,2),(4,6,20),(2,5,20),(5,15,7),(2,2,7),(2,7,7),(25,25,25),(4,2,2),(80,6,2),
          (20,2,4),(80,20,6),(4,4,4),(15,6,4),(80,80,80),(80,2,15),(80,25,2),(2,6,6),(15,6,25),
          (20,7,7),(2,2,2)]
result = restore_list(reels1)
print(result)
