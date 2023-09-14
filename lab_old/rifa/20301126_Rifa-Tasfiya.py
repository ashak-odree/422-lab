def A_star(g, s, des, heu_g):
    global is_keyerror
    dist = {s: 0}
    priority_que = []
    track_prev = {}
    for v in g:  # Traversing based on g's keys
        if v != s:
            dist[v] = float('inf')  # making all the values of node inf in dist except source node.
            track_prev[v] = None  # making all the ancestors of node None in track_prev except source node.
        priority_que.append(v)

    while len(priority_que) != 0:
        d = {}
        for p in priority_que:
            d.update({p: dist[p] + heu_g[p]})  # Adding heuristic values
        min_dist = min(d, key=d.get)  # Finding current minimum distance node
        priority_que.remove(min_dist)  # Removed the minimum distance node
        for key, val in g[min_dist].items(): # Traversing the child of minimum distance node
            temp = dist[min_dist] + int(val) # Just tracking distance without heuristic values, it has been added on the outter loop.
            if temp < dist[key]:
                dist[key] = temp
                track_prev[key] = min_dist
    # return track_prev
    cost = dist.get(des)
    return (track_prev, cost)


def show_path(g, s, des, heu_g):
    x = A_star(g, s, des, heu_g)
    # print(x)
    curr = des
    path_list = []
    while curr != s:  # Backtracking
        try:
            path_list.insert(0, curr)
            curr = x[0][curr]  # x[0] detects the track_prev dictionary, [curr] defines the key of the dict.
        except Exception:
            print('NO PATH FOUND')
            return


    path_list.insert(0, s)
    print("Path: ", " -> ".join(path_list))
    print(f"Total distance: {x[1]} km")

is_keyerror = False
'''Reading the file'''
with open("input file1.txt", "r") as f:
    g = {}  # Graph
    heu_g = {}  # Graph containing all the heuristic values
    for line in f:
        line = line.split()
        u = line[0]
        hu = int(line[1])
        heu_g[u] = hu
        size = len(line)
        for i in range(2, size):
            if i % 2 == 0:
                v = line[i]
            else:
                w = line[i]
                if u not in g:
                    g[u] = {}
                g[u].update({v: w})


print(g)
print(heu_g)
source = input("Start node: ")
destination = input("Destination: ")

show_path(g, source, destination, heu_g)


