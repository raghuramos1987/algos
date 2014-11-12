
finish = 0
class Node:

    def __init__(self, data, edges, finish=-1):
        self.data = data
        self.edges = edges
        self.marked = False
        self.finish = finish

    def __str__(self):
        string = "data: {}, finish: {}, edges: {}"
        edge_str = ""
        for edge in self.edges:
            edge_str += str(edge.data) + ','
        return string.format(self.data, self.finish, edge_str)

    def __eq__(self, other):
        if type(other) == int:
            return self.data == other
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)

    def __lt__(self, other):
        return self.finish < other.finish

def reverse_graph(nodes):
    node_map = {node.data: Node(node.data, []) for node in nodes}
    for node in nodes:
        for ed in node.edges:
            node_map[ed.data].edges.append(node_map[node.data])
    return node_map

def DFS(node, with_finish=False):
    stack = [node]
    global finish
    fin_stack = []
    size = 0
    while stack:
        node = stack.pop()
        fin_stack.append(node)
        if not node.marked:
            node.marked = True
            size += 1
            for edge in node.edges:
                if edge.marked:
                    continue
                else:
                    stack.append(edge)
                    #DFS(edge, with_finish)
    if with_finish:
        while fin_stack:
            node = fin_stack.pop()
            finish += 1
            node.finish = finish
    return size

def construct_graph(file_handle):
    node_map = {}
    node_map_rev = {}
    for line in file_handle.xreadlines():
        x, y = map(int, line.split())
        if not x in node_map:
            node_map[x] = Node(x, [])
            node_map_rev[x] = Node(x, [])
        if not y in node_map:
            node_map[y] = Node(y, [])
            node_map_rev[y] = Node(y, [])
        node_map[x].edges.append(node_map[y])
        node_map_rev[y].edges.append(node_map_rev[x])
    return node_map, node_map_rev

if __name__ == '__main__':
    fh = open('SCC.txt')
    node_map, node_map_rev = construct_graph(fh)
    for node in node_map_rev.values():
        if node.marked:
            continue
        DFS(node, True)
    for k, v in node_map_rev.iteritems():
        node_map[k].finish = v.finish
    node_list = sorted(node_map.values())
    node_set = set(node_map.values())
    scc = []
    count = 0
    while node_list:
        node = node_list.pop()
        while node_list and node.marked:
            node = node_list.pop()
        n = DFS(node)
        scc.append(n)
    print scc
