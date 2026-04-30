import random
from ai_pkg import Graph, Node, Problem, argmax_random_tie

city_map = Graph(
    {
        "Sibiu": {
            "Fagaras": 99, "Rimnicu": 80, "Craiova": 175,
            "Pitesti": 177, "Bucharest": 278
        },
        "Fagaras": {
            "Sibiu": 99, "Rimnicu": 81, "Pitesti": 82,
            "Bucharest": 211, "Craiova": 220
        },
        "Rimnicu": {
            "Sibiu": 80, "Fagaras": 81, "Pitesti": 97,
            "Craiova": 146, "Bucharest": 198
        },
        "Pitesti": {
            "Rimnicu": 97, "Fagaras": 82, "Craiova": 138,
            "Bucharest": 101, "Sibiu": 177
        },
        "Craiova": {
            "Sibiu": 175, "Rimnicu": 146, "Pitesti": 138,
            "Bucharest": 152, "Fagaras": 220
        },
        "Bucharest": {
            "Fagaras": 211, "Pitesti": 101, "Craiova": 152,
            "Rimnicu": 198, "Sibiu": 278
        }
    },
    directed=False
)


distances = {}

class TSPProblem(Problem):
    def generate_neighbour(self, state):
        neighbour_state = state[:]
        left = random.randint(0, len(neighbour_state) - 1)
        right = random.randint(0, len(neighbour_state) - 1)
        if left > right:
            left, right = right, left
        neighbour_state[left:right+1] = list(reversed(neighbour_state[left:right+1]))
        return neighbour_state

    def actions(self, state):
        return [self.generate_neighbour]

    def result(self, state, action):
        return action(state)

    def path_cost(self, state):
        cost = 0
        for i in range(len(state) - 1):
            current_city = state[i]
            next_city = state[i + 1]
            cost += distances[current_city][next_city]
        cost += distances[state[-1]][state[0]]  
        return cost

    def value(self, state):
        return -1 * self.path_cost(state)  

def hill_climbing(problem):
    def find_neighbors(state, number_of_neighbors=100):
        neighbors = []
        for _ in range(number_of_neighbors):
            new_state = problem.generate_neighbour(state)
            neighbors.append(Node(new_state))
        return neighbors

    current = Node(problem.initial)
    while True:
        neighbors = find_neighbors(current.state)
        if not neighbors:
            break
        neighbor = argmax_random_tie(neighbors, key=lambda node: problem.value(node.state))
        if problem.value(neighbor.state) <= problem.value(current.state):
            break
        current = neighbor
    return current.state

if __name__ == '__main__':
    all_cities = []
    cities_graph = city_map.graph_dict
    for city_1 in cities_graph.keys():
        distances[city_1] = {}
        if city_1 not in all_cities:
            all_cities.append(city_1)
        for city_2 in cities_graph.keys():
            if city_1 == city_2:
                distances[city_1][city_2] = 0
            elif cities_graph.get(city_1).get(city_2) is not None:
                distances[city_1][city_2] = cities_graph.get(city_1).get(city_2)
            else:
                distances[city_1][city_2] = float('inf')  

    random.shuffle(all_cities)  
    problem = TSPProblem(initial=all_cities.copy())

    best_path = hill_climbing(problem)
    print("Best path found:", best_path)
    print("Path cost:", problem.path_cost(best_path))