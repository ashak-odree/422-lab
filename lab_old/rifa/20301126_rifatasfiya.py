import random
import math


def alphaBetaPruning(random_val, pos, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        return random_val[pos]
    if maximizingPlayer:  # True ---> Max
        maxEval = -math.inf
        for i in range(2):
            eval = alphaBetaPruning(random_val, pos * 2 + i, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  # Pruning
                break
        return maxEval
    else:     # False -- > Min
        minEval = math.inf
        for i in range(2):
            eval = alphaBetaPruning(random_val, pos * 2 + i, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if alpha >= beta:  # Pruning
                break
        return minEval


def printing_winner(my_id):
    copy_id = ""
    for i in my_id:
        if i == "0":
            copy_id += "8"
        else:
            copy_id += i
    my_id = copy_id  # Replaced all the zeros to one
    pointToWin = int(my_id[-2]+my_id[-1])  # Reverse of the last two digits of student ID
    max_point = int(pointToWin * 1.5)
    min_point = int(my_id[4])
    counting_shuffle = int(my_id[3])
    random_val = []
    for i in range(8):
      random_val.append(random.randint(min_point, max_point))
    #print(random_val)
    #random_val = [66, 74, 14, 73, 19, 26, 32, 40]

    points_achieved = alphaBetaPruning(random_val, 0, 3, -math.inf, math.inf, True)
    #print("points_achieved", points_achieved)

    print("------> Task 1")
    print(f"Generated 8 random points between the minimum and maximum point limits: {random_val}")
    print(f"Total points to win: {pointToWin}")
    print(f"Achieved point by applying alpha-beta pruning = {points_achieved}")
    if points_achieved >= pointToWin:
        print("The winner is Optimus Prime")
    else:
        print("The winner is Megatron")

    shuffle_list = []
    for i in range(counting_shuffle):
        random.shuffle(random_val)
        point_achieved = alphaBetaPruning(random_val, 0, 3, -math.inf, math.inf, True)
        shuffle_list.append(point_achieved)

    wining_times = 0
    for j in shuffle_list:
        if j >= pointToWin:
            wining_times += 1

    print("\n-----> Task-2")
    print("After the shuffle:")
    print(f"List of all points values from each shuffle: {shuffle_list}")
    print(f"The maximum value of all shuffles: {max(shuffle_list)}")
    print(f"Won  {wining_times} times out of {counting_shuffle} number of shuffles")


my_id = input("Enter your student ID: ") or "20301126"
#my_id = "25485465"
printing_winner(my_id)

