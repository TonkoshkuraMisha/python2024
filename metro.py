class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist
        v1.links.append(self)
        v2.links.append(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    @property
    def nodes(self):
        return self.v1, self.v2


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if not any((link.v1 == l.v1 and link.v2 == l.v2) or (link.v1 == l.v2 and link.v2 == l.v1) for l in self._links):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        paths = []
        visited = set()

        def dfs(current, end, path, links):
            if current == end:
                paths.append((list(path), list(links)))
                return
            visited.add(current)
            for link in current.links:
                next_v = link.v2 if link.v1 == current else link.v1
                if next_v not in visited:
                    path.append(next_v)
                    links.append(link)
                    dfs(next_v, end, path, links)
                    path.pop()
                    links.pop()
            visited.remove(current)

        dfs(start_v, stop_v, [start_v], [])
        shortest_path = min(paths, key=lambda x: sum(link.dist for link in x[1]), default=None)
        return shortest_path if shortest_path else ([], [])


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))  # 8 связей
print(len(map_metro._vertex))  # 7 вершин
path = map_metro.find_path(v1, v6)
print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
