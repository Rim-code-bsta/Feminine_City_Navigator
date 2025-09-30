#🌸The Graph of a city made for women. A city that is feminine, safe and empowering 🌸.
import heapq
from collections import deque
import random

# 🌸City-graph🌸
city_graph = {
    "Home": ["Cafe", "Flower Shop" , "Yoga Studio"],
    "Cafe": ["Home", "Gallery" , "Library"],
    "Library": ["Cafe", "School" , "Tech Lab"],
    "Tech Lab": ["Library", "Gallery", "School"],
    "Gallery": ["Cafe", "Tech Lab", "Beauty Salon"],
    "School": ["Library", "Tech Lab", "Yoga Studio"],
    "Yoga Studio": ["Home", "School", "Flower Shop"],
    "Flower Shop": ["Home", "Yoga Studio", "Beauty Salon"],
    "Beauty Salon": ["Gallery", "Flower Shop"]
}

# 🌸Weighted_City-graph for Dijkstra (Weights indicate distances)🌸
city_graph_weighted = {
    "Home": {"Cafe": 2, "Flower Shop": 1, "Yoga Studio": 3},
    "Cafe": {"Home": 2, "Gallery": 2, "Library": 3},
    "Library": {"Cafe": 3, "School": 2, "Tech Lab": 4},
    "Tech Lab": {"Library": 4, "Gallery": 2, "School": 1},
    "Gallery": {"Cafe": 2, "Tech Lab": 2, "Beauty Salon": 3},
    "School": {"Library": 2, "Tech Lab": 1, "Yoga Studio": 3},
    "Yoga Studio": {"Home": 3, "School": 3, "Flower Shop": 2},
    "Flower Shop": {"Home": 1, "Yoga Studio": 2, "Beauty Salon": 2},
    "Beauty Salon": {"Gallery": 3, "Flower Shop": 2}
}

# 🌸Descriptions🌸
descriptions = {
    "Home": "Your cozy home, when the world quietens and you can finally hear yourself 🏡✨",
    "Cafe": "A spot to sip coffee and be grateful for the moment ☕💡",
    "Library": "Where stories bloom and knowledge fills every room 📚🌸",
    "Tech Lab": "Where women code, innovate, and make an impact 💻⚡",
    "Gallery": "Creativity on display in the form of art 🎨",
    "School": "Learning, curiosity, and empowerment 🏫💖",
    "Yoga Studio": "Relax and give your God-given body a break 🧘‍♀️🌿",
    "Flower Shop": "Beautiful roses waiting just for you 🌹💐",
    "Beauty Salon": "A place to feel beautiful and confident ✨💄"
}

#🌸Bonus: Random Mentors / Quotes for women🌸
bonus_messages = [
    "💡 Rihanna once said: 'There’s something so special about a woman who dominates in a man’s world. It takes a certain grace, strength, intelligence, fearlessness and the nerve to never take no for an answer'.",
    "🌸 Nancy Rathburn once said: 'A strong woman understands that the gifts such as logic, decisiveness, and strength are just as feminine as intuition and emotional connection. She values and uses all of her gifts'.",
    "✨ Gloria Steinem once said: 'Don’t think about making women fit the world — think about making the world fit women'.",
    "⚡ Ruth Bader Ginsburg once said: 'Women belong in all places where decisions are being made. It shouldn’t be that women are the exception.'",
    "🧘‍♀️ Reese Witherspoon once said:'I encourage women to step up. Don’t wait for somebody to ask you.'"
]

#🌸DFS🌸
def dfs(graph, start, end, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, path + [neighbor], visited)
            if result is not None:
                return result
    return None

#🌸BFS🌸
def bfs(graph, start, end):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

#🌸Dijkstra🌸
def dijkstra(graph, start, end):
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == end:
            return path, cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

#🌸Function that helps getting valid location with case-insensitive matching🌸
def get_location(prompt):
    while True:
        loc = input(prompt).strip()
        matches = [l for l in city_graph if l.lower() == loc.lower()]
        if matches:
            return matches[0]
        print("❌ Location not found. Please choose from:", ", ".join(city_graph.keys()))

#🌸 Remove a location 🌸
def remove_location(location):
    if location not in city_graph:
        print("❌ Location not found in the city.")
        return
    for neighbor in city_graph[location]:
        city_graph[neighbor].remove(location)
    del city_graph[location]
    for neighbor in list(city_graph_weighted[location].keys()):
        del city_graph_weighted[neighbor][location]
    del city_graph_weighted[location]
    if location in descriptions:
        del descriptions[location]
    print(f"🗑️ {location} has been removed from the city.")

#🌸 Remove a connection 🌸
def remove_connection(loc1, loc2):
    if loc1 not in city_graph or loc2 not in city_graph:
        print("❌ One or both locations not found in the city.")
        return

    removed = False
    if loc2 in city_graph[loc1]:
        city_graph[loc1].remove(loc2)
        removed = True
    if loc1 in city_graph[loc2]:
        city_graph[loc2].remove(loc1)
        removed = True
    if loc2 in city_graph_weighted[loc1]:
        del city_graph_weighted[loc1][loc2]
        removed = True
    if loc1 in city_graph_weighted[loc2]:
        del city_graph_weighted[loc2][loc1]
        removed = True

    if removed:
        print(f"🗑️ Connection between {loc1} and {loc2} removed.")
    else:
        print(f"❌ No connection exists between {loc1} and {loc2}.")

#🌸Function that helps in printing paths with bonus messages🌸
def print_path(path, algorithm_name):
    if not path:
        print(f"❌ No path found using {algorithm_name}.")
        return
    print(f"\n✨ {algorithm_name} Path:")
    for loc in path:
        print(f"💡 {loc} — {descriptions[loc]}")
        if random.random() < 0.4:
            print(random.choice(bonus_messages))

#🌸Main Interactive CLI🌸
def main():
    print("🌸 Welcome to the Feminine City Navigation System! 🌸")
    print("Explore, relax, and see where the paths may take you :)\n")
    
    while True:  # Allow multiple travels
        while True:
            action = input("🌟 Do you want to add, remove, or continue exploring? (add/remove/continue) ").lower()
            if action == "add":
                new_location = input("🏡 Name of the new location: ").strip()
                if new_location in city_graph:
                    print("❌ Location already exists!")
                    continue
                city_graph[new_location] = []
                city_graph_weighted[new_location] = {}
                descriptions[new_location] = input(f"Add a description for {new_location}: ")
                print(f"✨ {new_location} added! Connect it to existing locations next.")
                while True:
                    connection = input("Connect to which location? (type 'done' when finished) ")
                    if connection.lower() == "done":
                        break
                    matches = [l for l in city_graph if l.lower() == connection.lower()]
                    if matches:
                        conn = matches[0]
                        city_graph[new_location].append(conn)
                        city_graph[conn].append(new_location)
                        while True:
                            try:
                                w = int(input(f"Distance/cost between {new_location} and {conn}? "))
                                break
                            except ValueError:
                                print("❌ Please enter a valid integer.")
                        city_graph_weighted[new_location][conn] = w
                        city_graph_weighted[conn][new_location] = w
                    else:
                        print("❌ Location not found in the city, try again please!")
            elif action == "remove":
                choice = input("Do you want to remove a 'location' or a 'connection'? ").lower()
                if choice == "location":
                    loc = get_location("Enter the location name to remove: ")
                    remove_location(loc)
                elif choice == "connection":
                    loc1 = get_location("Enter first location: ")
                    loc2 = get_location("Enter second location: ")
                    remove_connection(loc1, loc2)
                else:
                    print("❌ Invalid choice.")
            elif action == "continue":
                break
            else:
                print("❌ Invalid option. Please type add/remove/continue.")
        
        start = get_location("🌸 Where shall our feminine journey begin today? ")
        end = get_location("✨ Where do you want to go, wild visitor? ")
        
        dfs_path = dfs(city_graph, start, end)
        bfs_path = bfs(city_graph, start, end)
        dijkstra_path, dijkstra_cost = dijkstra(city_graph_weighted, start, end)
        
        print_path(dfs_path, "DFS")
        print_path(bfs_path, "BFS")
        print_path(dijkstra_path, "Dijkstra")
        if dijkstra_path:
            print(f"🏆 Total Cost: {dijkstra_cost}")
        
        again = input("\n🌸 Do you want to explore another path? (yes/no) ").lower()
        if again != "yes":
            print("💖 Thank you for exploring the Feminine City! 🌸")
            break

if __name__ == "__main__":
    main()
