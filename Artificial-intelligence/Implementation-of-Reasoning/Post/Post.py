from collections import deque

# Representasi graph kota
city_map = {
    'Jakarta': {
        'Kuala Lumpur': 1180,
        'Singapore': 1400
    },

    'Kuala Lumpur': {
        'Singapore': 350,
        'Bangkok': 1480,
        'Manila': 2700
    },

    'Singapore': {
        'Bangkok': 1430,
        'Ho Chi Minh': 1180
    },

    'Bangkok': {
        'Hanoi': 1800,
        'Yangon': 680
    },

    'Ho Chi Minh': {
        'Hanoi': 1700,
        'Manila': 1580
    },

    'Hanoi': {
        'Manila': 1760
    },

    'Yangon': {
        'Bangkok': 680
    },

    'Manila': {
        'Ho Chi Minh': 1580
    }
}


# Fungsi Breadth First Search
def breadth_first_search(start, goal, graph):

    # Queue menyimpan (kota, jalur)
    queue = deque([(start, [start])])

    # Menyimpan kota yang sudah dikunjungi
    explored = set()

    # Menyimpan urutan eksplorasi
    tracking_path = []

    while queue:

        # Ambil data paling depan dari queue
        current_city, path = queue.popleft()

        # Jika belum dikunjungi
        if current_city not in explored:

            tracking_path.append(current_city)
            explored.add(current_city)

            # Jika tujuan ditemukan
            if current_city == goal:
                return tracking_path, path

            # Ambil tetangga kota
            neighbors = graph.get(current_city, {})

            for neighbor in neighbors:

                if neighbor not in explored:

                    new_path = list(path)
                    new_path.append(neighbor)

                    queue.append((neighbor, new_path))

    return tracking_path, None


# Fungsi menghitung total jarak
def calculate_distance(path, graph):

    total = 0

    for i in range(len(path) - 1):

        city_from = path[i]
        city_to = path[i + 1]

        total += graph[city_from][city_to]

    return total


# EKSEKUSI PROGRAM

start_city = "Jakarta"
goal_city = "Manila"

tracking, solution = breadth_first_search(
    start_city,
    goal_city,
    city_map
)

print("=== HASIL BFS ===")
print(f"Kota Awal   : {start_city}")
print(f"Kota Tujuan : {goal_city}")

print("\nTracking Path:")
print(" -> ".join(tracking))

if solution:

    print("\nSolution Path:")
    print(" -> ".join(solution))

    total_distance = calculate_distance(solution, city_map)

    print(f"\nTotal Jarak: {total_distance} km")

else:
    print("Jalur tidak ditemukan.")