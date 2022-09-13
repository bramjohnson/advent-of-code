import time
fin = open("input.txt", "r").read().split("\n")
print(fin)

def graphify(undirected):
    graph = {}
    for connection in undirected:
        left = connection.split("-")[0]
        right = connection.split("-")[1]
        try:
            graph[left] += [right]
        except:
            graph[left] = [right]
        try:
            graph[right] += [left]
        except:
            graph[right] = [left]
    return graph

print((graphify(fin)))

def new_rules(graph):
    src = "start"
    dst = "end"
    paths = []
    
    # The first is the current node
    # The second is the visited nodes
    # The third is the current path taken
    # The fourth is if the path has already visited a small cave twice
    stack = [(src, [src], [src], False)]

    while stack:
        cur, visited, path, twiced = stack.pop()

        # If we have reached "end", let's call this path finished and drop it from the stack.
        if cur == dst:
            paths.append(path)
            continue

        for node in graph[cur]:
            # if the node is "start", skip it, we don't want to traverse that.
            if node == src:
                continue

            # if the node is a big cave, or it has not been visited, let's visit it.
            if node.isupper() or node not in visited:
                stack.append((node, visited + [node], path + [node], twiced))
                continue

            # if we have visited a small cave more than once, let's not continue.
            # This will drop any non-conforming paths from the stack as well :)
            if twiced: continue

            # if we haven't visited a small cave more than once, let's visit it.
            stack.append((node, visited, path + [node], True))

    return paths

#print(new_rules(graphify(fin)))
start = time.time()
print(str(len(new_rules(graphify(fin)))) + ": in " + str((time.time() - start) * 1000) + " ms!")


