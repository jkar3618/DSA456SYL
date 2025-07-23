import heapq

def dijkstra(graph, start, target):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    previous = {node: None for node in graph}
    

    unvisited = [(0, start)]
    
    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        
        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            return list(reversed(path)), distances[target]
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(unvisited, (distance, neighbor))
    
    return None

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}

test_cases = [
    ('A', 'F'),
    ('B', 'G')
]

# Test 1: Shortest path from A to F
path_af, distance_af = dijkstra(graph, 'A', 'F')
print("Shortest path from A to F:", path_af)
print("Distance from A to F:", distance_af)

# Test 2: Shortest path from B to G
path_bg, distance_bg = dijkstra(graph, 'B', 'G')
print("Shortest path from B to G:", path_bg)
print("Distance from B to G:", distance_bg)