import heapq 

def create_weighted_graph_dict(edges):
    
    graph = {}
    for node1, node2, weight in edges:
        # Initialize nodes if they don't exist
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        
        # undirectional graph
        graph[node1][node2] = weight
        graph[node2][node1] = weight
    return graph

def dijkstra(graph, start_node):
    
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    
    
    priority_queue = [(0, start_node, [start_node])]
    
    shortest_paths = {} 
    
    while priority_queue:
        current_distance, current_node, current_path = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        if current_node not in shortest_paths or current_distance < distances[current_node]:
             shortest_paths[current_node] = current_path
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                new_path = current_path + [neighbor] # Extend the path
                heapq.heappush(priority_queue, (distance, neighbor, new_path))
                
    return distances, shortest_paths


def find_best_stopover(graph, start_city, end_city, excluded_stopovers=input("Enter excluded stopovers (comma-separated): ").split(',')):
    
    if start_city not in graph or end_city not in graph:
        print(f"Error: Start city '{start_city}' or end city '{end_city}' not found in graph.")
        return None, float('infinity'), None

    if excluded_stopovers is None:
        excluded_stopovers = []

    distances_from_start, paths_from_start = dijkstra(graph, start_city)

    best_stopover = None
    min_total_distance = float('infinity')
    overall_best_path = []

    for stopover_city in graph:
       
        if stopover_city == start_city or stopover_city == end_city:
            continue

        # check to see if its a stopover I don't want
        if stopover_city in excluded_stopovers:
            print(f"Skipping '{stopover_city}' as a stopover (excluded).")
            continue

        # Check to see if theres a path from start to the stopover city and from there to the end city
        if distances_from_start[stopover_city] == float('infinity'):
            continue

        distances_from_stopover, paths_from_stopover = dijkstra(graph, stopover_city)

        
        if end_city not in distances_from_stopover or distances_from_stopover[end_city] == float('infinity'):
            continue

        total_distance = distances_from_start[stopover_city] + distances_from_stopover[end_city]

        if total_distance < min_total_distance:
            min_total_distance = total_distance
            best_stopover = stopover_city
            
            path_to_stopover = paths_from_start[stopover_city]
            path_from_stopover_to_end = paths_from_stopover[end_city][1:] 
            overall_best_path = path_to_stopover + path_from_stopover_to_end

    return best_stopover, min_total_distance, overall_best_path

# used the help of AI to write all the edges

edges = [
    
    ('dubai', 'vancouver', 11724),
    ('dubai', 'tokyo', 12090),
    ('vancouver', 'tokyo', 7597),
    ('dubai', 'london', 5470.25),
    ('london', 'tokyo', 9559.36),

    # --- Connections involving New York (NYC) ---
    ('dubai', 'new york', 11040),
    ('london', 'new york', 5570),
    ('tokyo', 'new york', 10840),
    ('vancouver', 'new york', 3900),
    ('paris', 'new york', 5830),
    ('sydney', 'new york', 16000),

    # --- Connections involving Paris ---
    ('dubai', 'paris', 5250),
    ('london', 'paris', 345),
    ('tokyo', 'paris', 9715),
    ('singapore', 'paris', 10300),

    # --- Connections involving Sydney ---
    ('dubai', 'sydney', 12050),
    ('london', 'sydney', 17015),
    ('tokyo', 'sydney', 7820),
    ('vancouver', 'sydney', 12510),
    ('singapore', 'sydney', 6300),

    # --- Connections involving Singapore ---
    ('dubai', 'singapore', 5830),
    ('london', 'singapore', 10850),
    ('tokyo', 'singapore', 5320),

    # --- Connections involving Kozhikode ---
    ('dubai', 'kozhikode', 2695),
    ('kozhikode', 'london', 7670),
    ('kozhikode', 'singapore', 3450),
    ('kozhikode', 'tokyo', 7500),
    ('kozhikode', 'paris', 7480),

    # --- GCC Countries and their connections (excluding Abu Dhabi) ---
    ('dubai', 'muscat', 350),      # Oman
    ('dubai', 'manama', 485),      # Bahrain
    ('dubai', 'kuwait city', 855),
    ('dubai', 'doha', 380),
    ('dubai', 'riyadh', 875),
    ('dubai', 'jeddah', 1700),
    # Removed: ('dubai', 'abu dhabi', 115)

    # Removed all connections directly involving 'abu dhabi':
    # ('abu dhabi', 'doha', 320),
    # ('abu dhabi', 'riyadh', 810),
    # ('abu dhabi', 'muscat', 390),
    # ('kozhikode', 'abu dhabi', 2500),

    ('doha', 'riyadh', 490),
    ('kuwait city', 'riyadh', 785),
    ('manama', 'riyadh', 420),
    ('manama', 'kuwait city', 350),
    ('jeddah', 'riyadh', 850),

    ('kozhikode', 'muscat', 1500),
    ('kozhikode', 'doha', 2800),


    # --- Azerbaijan, Georgia, Turkey (Baku, Tbilisi, Istanbul) ---
    ('dubai', 'baku', 1760),
    ('dubai', 'tbilisi', 2060),
    ('dubai', 'istanbul', 2970),

    ('london', 'istanbul', 2495),
    ('paris', 'istanbul', 2250),
    ('frankfurt', 'istanbul', 1900),
    ('rome', 'istanbul', 1370),
    ('madrid', 'istanbul', 2740),

    ('baku', 'tbilisi', 450),
    ('baku', 'istanbul', 1745),
    ('tbilisi', 'istanbul', 1300),

    ('kozhikode', 'istanbul', 4900),

    # --- Main European Countries (Frankfurt, Rome, Madrid) ---
    ('london', 'frankfurt', 635),
    ('london', 'rome', 1435),
    ('london', 'madrid', 1260),

    ('paris', 'frankfurt', 475),
    ('paris', 'rome', 1105),
    ('paris', 'madrid', 1050),

    ('frankfurt', 'rome', 965),
    ('frankfurt', 'madrid', 1445),

    ('rome', 'madrid', 1360),

    ('new york', 'frankfurt', 6200),
    ('new york', 'rome', 6900),
    ('new york', 'madrid', 5760),

    # --- Johannesburg, Cairo, Beijing, Mumbai, Bangkok, Rio de Janeiro, Toronto, Los Angeles ---

    # Connections for Johannesburg
    ('dubai', 'johannesburg', 7100),
    ('london', 'johannesburg', 9000),
    ('cairo', 'johannesburg', 6200),
    ('singapore', 'johannesburg', 8700),

    # Connections for Cairo
    ('dubai', 'cairo', 2420),
    ('london', 'cairo', 3500),
    ('paris', 'cairo', 3200),
    ('istanbul', 'cairo', 1200),
    ('rome', 'cairo', 2150),
    ('kozhikode', 'cairo', 4100),
    ('riyadh', 'cairo', 1600),

    # Connections for Beijing
    ('dubai', 'beijing', 5800),
    ('tokyo', 'beijing', 2100),
    ('singapore', 'beijing', 4400),
    ('london', 'beijing', 8150),
    ('new york', 'beijing', 11000),

    # Connections for Mumbai
    ('dubai', 'mumbai', 1930),
    ('kozhikode', 'mumbai', 950),
    ('singapore', 'mumbai', 3900),
    ('london', 'mumbai', 7200),
    ('frankfurt', 'mumbai', 6300),
    ('riyadh', 'mumbai', 2800),

    # Connections for Bangkok
    ('dubai', 'bangkok', 4890),
    ('singapore', 'bangkok', 1430),
    ('tokyo', 'bangkok', 4600),
    ('sydney', 'bangkok', 7500),
    ('london', 'bangkok', 9500),
    ('mumbai', 'bangkok', 3000),

    # Connections for Rio de Janeiro
    ('new york', 'rio de janeiro', 7900),
    ('london', 'rio de janeiro', 9280),
    ('madrid', 'rio de janeiro', 8100),
    ('dubai', 'rio de janeiro', 12000),

    # Connections for Toronto
    ('london', 'toronto', 5700),
    ('new york', 'toronto', 550),
    ('vancouver', 'toronto', 3350),
    ('paris', 'toronto', 6000),

    # Connections for Los Angeles
    ('tokyo', 'los angeles', 8800),
    ('sydney', 'los angeles', 12000),
    ('london', 'los angeles', 8700),
    ('new york', 'los angeles', 3950),
    ('vancouver', 'los angeles', 1700),
    ('dubai', 'los angeles', 13390),
    ('vancouver', 'calgary', 685), # Canadian domestic
    ('toronto', 'calgary', 2700), # Canadian domestic
    ('new york', 'calgary', 3200),
    ('london', 'calgary', 7000),
    ('dubai', 'calgary', 10300), # Very long, usually direct or 1 stop
    ('tokyo', 'calgary', 7500),
    ('los angeles', 'calgary', 1200), # US/Canada cross-border
]

weighted_graph = create_weighted_graph_dict(edges)

print("--- Weighted Graph Structure ---")
for city, connections in weighted_graph.items():
    print(f"  {city}: {connections}")
print("-" * 40)

start_city_route = input("Enter the starting city: ")
end_city_route = input("Enter the destination city: ")

print(f"\n--- Analysis for path from {start_city_route} to {end_city_route} with one stopover ---")

# get direct distance
direct_path_distance = weighted_graph.get(start_city_route, {}).get(end_city_route)
if direct_path_distance is not None:
    print(f"Direct flight distance ({start_city_route} to {end_city_route}): {direct_path_distance:.2f} km")
else:
    print(f"No direct flight found from {start_city_route} to {end_city_route}.")

# finding stopover path
best_stopover_city, total_distance_with_stopover, full_path = find_best_stopover(
    weighted_graph, start_city_route, end_city_route
)

if best_stopover_city:
    print(f"\nBest stopover for {start_city_route} to {end_city_route} (one stop):")
    print(f"  Stopover city: {best_stopover_city}")
    print(f"  Total distance via stopover: {total_distance_with_stopover:.2f} km")
    print(f"  Optimal path: {' -> '.join(full_path)}")
else:
    print(f"\nNo valid single-stopover path found from {start_city_route} to {end_city_route}.")

print("\n" + "=" * 40)

