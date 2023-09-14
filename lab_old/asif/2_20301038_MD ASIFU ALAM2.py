import random
from random import randrange

all = {}
dic_for_all = {}
player_name = []
all_attempt = []
with open("data.txt", "r") as f:
    file = f.readlines()
    point = file[0].split()
    player = int(point[0])
    total_point = int(point[1])
    for i in range(1, len(file)):
        x, y = file[i].split()
        player_name.append(x)
        all[x] = y


def know_score(arr, all):
    total = 0
    for i in range(len(arr)):
        if arr[i] == "1":
            total += int(all[player_name[i]])
    return total


def binary_make(count):
    x = bin(count)[2:].zfill(player)
    x = list(str(x))
    return x


def fitness_function(totalpoint, all, dic_for_all):
    count = 1
    while totalpoint != know_score(binary_make(count), all):
        count += 1
        add = str("".join(binary_make(count)))
        dic_for_all[add] = know_score(binary_make(count), all)
        all_attempt.append(add)
        if "0" not in binary_make(count + 1):
            print(-1)
            break
    # print(dic_for_all)
    return str("".join(binary_make(count)))


print(fitness_function(total_point, all, dic_for_all))


def crossover(total_point, all_attempt):
    final_ans = 0
    done = []
    while total_point != final_ans:
        first = random.choices(all_attempt)
        second = random.choices(all_attempt)
        s = [first, second]
        if s not in done:
            i = random.randint(0, player)
            first1 = first[:i] + second[i::]
            second1 = second[:i] + second[i::]
            # print(first1,second1)
            if know_score(list(first1[0]), all) == total_point:
                final_ans += know_score(first1[0], all)
                return first1[0]
            if know_score(list(second1[0]), all) == total_point:
                final_ans += know_score(second1[0], all)
                return second1[0]
            s = [first1, second1]
            done.append(s)


print(crossover(total_point, all_attempt))


def mutation(total_point, all_attempt, mutation_threshold):
    done2 = []
    total_score = 0
    while total_point != total_score:
        mutation_value = round(random.random(), 1)
        if mutation_value == mutation_threshold:
            content = random.choices(all_attempt)
            content = list(content[0])
            random_index = randrange(len(content))
            if content[random_index] not in done2:
                if content[random_index] == "0":
                    content[random_index] = "1"
                    done2.append(content)
                    # print(content)
                    total_score = know_score(content, all)
                    if total_score == total_point:
                        return total_score
                else:
                    content[random_index] = "0"
                    done2.append(content)
                    total_score = know_score(content, all)
                    if total_score == total_point:
                        return total_score


print(mutation(total_point, all_attempt, .3))
