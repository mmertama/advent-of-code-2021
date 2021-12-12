example0 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end
'''

example1 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
'''

example = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
'''


class Node:
    def __init__(self, name, node):
        self.state = 0
        self.name = name
        self.nodes = [node]
        self.visited = set()
        self.is_small = self.name.islower() and self.name != 'start' and self.name != 'end'

    def append(self, node):
        self.nodes.append(node)

    def __str__(self):
        return str(self.nodes)

    def reset(self, nodes, root):
        self.state = 0
        for c in self.nodes:
            child = nodes[c]
            if child.state != 0:
                child.reset(nodes, root)
        if self.name == root.name:
            self.state = 1


def parse_nodes(data):
    nodes = {}
    for ln in data:
        sep = ln.find('-')
        node0 = ln[sep + 1:]
        node1 = ln[:sep]
        if node0 in nodes:
            nodes[node0].append(node1)
        elif node1 != 'start':
            nodes[node0] = Node(node0, node1)
        if node1 in nodes:
            nodes[node1].append(node0)
        elif node0 != 'start':
            nodes[node1] = Node(node1, node0)
    return nodes


def get_paths(nodes, name):
    node = nodes[name]
    paths = []
    if name == 'end':
        paths.append(['end'])
        return paths
    if node.is_small:
        node.state = 1
    for child_name in node.nodes:
        child = nodes[child_name]
        if child_name == 'start':
            continue
        if child.is_small and child.state == 1:
            continue
        child_paths = get_paths(nodes, child_name)
        for cp in child_paths:
            paths.append([name] + cp)
    if node.is_small:
        node.state = 0
    return paths


def two_hits(nodes):
    for n in nodes:
        m = nodes[n]
        if m.is_small and m.state == 2:
            return True
    return False


def get_paths2(nodes, name):
    node = nodes[name]
    paths = []
    if name == 'end':
        paths.append(['end'])
        return paths
    if node.is_small:
        node.state += 1
    for child_name in node.nodes:
        child = nodes[child_name]
        if child_name == 'start':
            continue
        # We don't go if any small child is already having two passes
        if child.is_small and child.state != 0 and two_hits(nodes):
            continue
        child_paths = get_paths2(nodes, child_name)
        for cp in child_paths:
            paths.append([name] + cp)
    if node.is_small:
        node.state -= 1  # this makes sure that combined paths has a correct states. I think :-)
    return paths


def count_paths(data):
    nodes = parse_nodes(data)
    paths = get_paths(nodes, 'start')
    print("Paths:", len(paths))


def count_paths2(data):
    nodes = parse_nodes(data)
    paths = get_paths2(nodes, 'start')
    print("Paths x 2:", len(paths))


