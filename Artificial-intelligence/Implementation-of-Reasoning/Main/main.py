from collections import deque

# 1. REPRESENTASI DATA (Graph Kota)
city_map = {
    'NewYork': {'Chicago': 1000, 'Toronto': 800, 'Denver': 1900},
    'Chicago': {'Denver': 1000},
    'Denver': {'LosAngeles': 1000, 'Houston': 1500, 'Urbana': 1000},
    'Houston': {'LosAngeles': 1500},
    'Toronto': {'LosAngeles': 1800, 'Chicago': 500, 'Calgary': 1500},
    'Calgary': {'LosAngeles': 1000} # Penambahan contoh koneksi
}

def breadth_first_search(start, goal, graph):
    # Frontier: Antrean untuk dikunjungi (Node, Jalur_saat_ini)
    queue = deque([(start, [start])])
    explored = set()
    tracking_path = [] # Untuk mencatat urutan kota yang diperiksa

    while queue:
        (current_node, path) = queue.popleft()
        
        if current_node not in explored:
            tracking_path.append(current_node)
            explored.add(current_node)

            # Cek apakah sudah sampai tujuan
            if current_node == goal:
                return tracking_path, path

            # Ambil tetangga kota tersebut
            neighbors = graph.get(current_node, {})
            for neighbor in neighbors:
                if neighbor not in explored:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
    
    return tracking_path, None

# --- EKSEKUSI PROGRAM ---
start_city = "NewYork"
goal_city = "LosAngeles"

track, solution = breadth_first_search(start_city, goal_city, city_map)

print("=== HASIL PENCARIAN RUTE ===")
print(f"Kota Asal   : {start_city}")
print(f"Kota Tujuan : {goal_city}")
print("-" * 30)
print(f"TRACKING PATH (Urutan Penjelajahan): \n{' -> '.join(track)}")
print("-" * 30)
if solution:
    print(f"SOLUTION PATH (Jalur Terbaik): \n{' -> '.join(solution)}")
else:
    print("Maaf, jalur tidak ditemukan.")