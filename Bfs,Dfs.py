from collections import deque

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, start_node):
    queue = deque()
    visited.add(start_node)
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    graph = {}
    visited_dfs = set()
    visited_bfs = set()

    n = int(input("Enter number of nodes: "))

    for _ in range(n):
        node = input("Enter name of node: ").strip()
        edges_count = int(input(f"Enter number of edges for node {node}: "))
        graph[node] = []
        for i in range(edges_count):
            neighbour = input(f"Enter edge {i+1} for node {node}: ").strip()
            graph[node].append(neighbour)

    start_node = input("Enter starting node: ").strip()

    print("\nThe following is DFS:")
    dfs(visited_dfs, graph, start_node)

    print("\nThe following is BFS:")
    bfs(visited_bfs, graph, start_node)

if __name__ == "__main__":
    main()
