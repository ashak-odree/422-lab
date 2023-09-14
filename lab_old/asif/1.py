adjacency_list = {}
heuristic1 = {}
with open("C:\Users\User\Desktop\Input_file.txt") as f:
    lines = [line.strip() for line in f]
for i in lines:
    li = list(i.split(" "))
    heuristic1[li[0]] = int(li[1])
    t = []
    for j in range(0, len(li[2::]) - 1, 2):
        x = (li[2::][j], int(li[2::][j + 1]))
        t.append(x)
    adjacency_list[li[0]] = t
# print(adjacency_list)
# print(heuristic1)
# ----------------------------------------------------
start = "Arad"
goal = "Bucharest"
current_node = start
lst = []
parent_to_child = {}
for i in heuristic1:
    parent_to_child[i] = [0]  # final path er jonne call dibo gg
closed_paths = []

while True:
    if len(lst) == 0:
        """normally first node append in parent and close path"""
        for i in adjacency_list[start]:
            total_value = heuristic1[i[0]] + i[1]
            lst.append((i[0], total_value))
            parent_to_child[i[0]] = [start, i[1]]
            closed_paths.append(start)
    else:
        current_node = lst.pop(0)
        if current_node[0] == goal:
            break
        elif len(lst) == 0:
            print("No path found")
            break

        closed_paths.append(current_node[0])
        current_node_name = current_node[0]
        current_node_value = current_node[1]
        total_value = 0
        for i in adjacency_list[current_node_name]:  # checking and creating lists
            if i[0] not in closed_paths:
                total_value = heuristic1[i[0]] + i[1] + parent_to_child[current_node_name][1]
                ok = 0
                """checking if it is smaller then-other nodes"""
                for check in range(len(lst)):  # removing shorter paths
                    if i[0] in lst[check] and total_value < lst[check][1]:
                        lst[check] = (i[0], total_value)
                        ok += 1
                """checking if it is greater then-other nodes... if ok is 0 that means that node is greater then 
                other node in [lst] """
                if ok == 0:
                    p = 0
                    for k in range(len(lst)):
                        """if that already in lst than I don't append 
                        I don't want to check If it is smaller or not cos I check it previously
                        """
                        if i[0] in lst[k]:
                            p += 1
                    if p == 0:
                        lst.append((i[0], total_value))
                parent_to_child[i[0]] = [current_node_name, i[1] + parent_to_child[current_node_name][1]]

    lst.sort(key=lambda x: x[1])

# print(parent_to_child)
# print(closed_paths)
# print(lst)
# -------------------print statement--------------------------------

if len(lst)!=0:
    first_node=start
    last_node=goal
    paths=[goal]
    while last_node!=first_node:
      last_node=parent_to_child[last_node][0]
      paths.append(last_node)

    print("Paths:",'-> '.join(paths))
    print("Total distance:",parent_to_child[goal][1],"KM")