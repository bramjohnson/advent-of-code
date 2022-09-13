cl = open("input.txt", "r").read().split("\n")
tl = open("test.txt", "r").read().split("\n")

key_words = ["start", "end"]

def graphify(ls):
    def add_to_graph(key, add, graph):
        if key == "end":
            return graph
        elif key in graph:
            if add != "start":
                graph[key] = sorted(graph[key] + [add])
                return graph
            else:
                return graph
        else:
            if add != "start":
                graph[key] = [add]
                return graph
            else:
                return graph

    graph = {}
    for connection in ls:
        left = connection.split("-")[0]
        right = connection.split("-")[1]
        graph = add_to_graph(left, right, graph)
        graph = add_to_graph(right, left, graph)
    return graph

def all_paths(graph):
    def update_visited(node, visited):
        if node == node.upper(): return visited
        else: return visited + [node]
            
    def find_paths(cur, visited):
        if cur == "end":
            return [["end"]]
        paths = []
        for connection in [x for x in graph[cur] if x not in visited]:
            for path in find_paths(connection, update_visited(cur, visited)):
                paths.append([cur] + path)
        return paths
    return find_paths("start", [])

def new_rules(graph):
    def update_visited(node, visited):
        if node == node.upper(): return visited
        else: return visited + [node]
            
    def find_paths(cur, visited, twiced):
        if cur == "end":
            return [["end"]]
        paths = []
        for connection in [x for x in graph[cur] if x not in visited]:
            if connection == connection.lower() and not twiced and connection != "end":
                for path in find_paths(connection, visited, True):
                    paths.append([cur] + path)
            for path in find_paths(connection, update_visited(connection, visited), twiced):
                paths.append([cur] + path)
        return paths
    return find_paths("start", [], False)

def visit_small(path):
    return any([x == x.lower() for x in path[1:-1]])

#print(graphify(tl))
print(new_rules(graphify(tl)))
#print(len([x for x in all_paths(graphify(cl)) if visit_small(x)]))