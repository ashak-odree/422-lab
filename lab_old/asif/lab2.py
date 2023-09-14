import math
import random

id = '28381838'
minimum_point = int(id[4])
maximum_point = id[7] + id[6]
maximum_point = int(maximum_point)
maximum_point_no = int(maximum_point)*1.5
list_of_all_points_to_win = []


def algo(list_of_all_points_to_win):
    grand_parent = {}
    parent = {}

    beta = math.inf
    alpha = -math.inf
    steps = True
    child = []
    for i in range(len(list_of_all_points_to_win)):
        child.append(list_of_all_points_to_win[i])
        if len(child) == 2:
            if steps is True and len(parent) != 2:
                for j in child:
                    if alpha <= j:
                        alpha = j

                if len(parent) == 0:
                    parent[alpha] = {"alpha": -math.inf, "beta": alpha}
                    alpha = -math.inf
                    beta = alpha

                else:
                    parent[alpha] = alpha
                    steps = False

            if steps is False:
                minimum = min(parent)
                parent = {}
                grand_parent[minimum] = {"alpha": minimum, "beta": math.inf}

                alpha = minimum
                beta = math.inf
                steps = True

            child = []

    return max(grand_parent)
def winner(grand_parent,maximum_point):
    if math.ceil(grand_parent) >= math.ceil(maximum_point):
        return "The winner is Optimus Prime"
    else:
        return "the Winner is Megatron"

for i in range(len(id)):
    list_of_all_points_to_win.append(random.randint(minimum_point, int(maximum_point)))

print(f"""
Generated {len(list_of_all_points_to_win)} random points between the minimum and maximum point limits: 
{list_of_all_points_to_win}
Total points to win: {math.ceil(maximum_point)}
Achieved point by applying alpha-beta pruning = {algo(list_of_all_points_to_win)}
{winner(algo(list_of_all_points_to_win),maximum_point)}
""")
count=0
max_value_of_all_shaffles=[]
for i in range(int(id[3])):
    random.shuffle(list_of_all_points_to_win)
    max_point=algo(list_of_all_points_to_win)
    max_value_of_all_shaffles.append(max_point)
    if maximum_point<=max_point:
        count+=1

print(f"""
After the shuffle:
List of all points values from each shuffles: {max_value_of_all_shaffles}
The maximum value of all shuffles: {max(max_value_of_all_shaffles)}
Won {count} times out of {len(max_value_of_all_shaffles)} number of shuffles 
""")


