import random


def crossover(p1, p2):
    if random.random() < prob_crossover:
        pointCrossover = random.randint(0, t - 1)  # Randomly generating the index value between 0 to t-1 for mutation
        c1 = p1[:pointCrossover] + p2[pointCrossover:]
        c2 = p2[:pointCrossover] + p1[pointCrossover:]
    else:
        c1, c2 = p1, p2
    return c1, c2


def mutation(chro):  # 1 0 1  0 1 1 1
    i = random.randint(0, t - 1)  # Randomly generating the index value between 0 to t-1 for mutation
    if random.random() < prob_mutation:
        point = random.randint(0, 1)
        chro[i] = point
    return chro

"""Providing the fitness value where zero is the fittest."""
def fitness_function(chro): # 1 0 1  0 1 1 1
    b = 0 # balance
    for i in range(t):
        if chro[i] == 1:
            if lst_trans[i][0] == 'l':  # If lend then subtract from the total balance
                b = b - lst_trans[i][1]
            else:
                b = b + lst_trans[i][1]  # If deposit then add to the total balance
    return abs(b)



'''create parents. Genarating ramdom population.'''
def generate_population(t):
    population = []
    for i in range(population_size):
        chro = []
        for j in range(t):  # [1,0, 1,0 ,1, 1, 0]  #t=7
            chro.append(random.randint(0, 1))
        population.append(chro)
    return population


def generate_fittest_output():
    global did_printed
    population = generate_population(t)
    goal = 0
    #print(population)
    for g in range(iteration_threshold):  # Took random value as an iteration threshold = 1000
        fitness_lst = []
        for chro in population:
            fitness_lst.append(fitness_function(chro))

        sorted_lst = sorted(fitness_lst)
        p1 = sorted_lst[0]  # Selected the first fittest parent
        p2 = sorted_lst[1]  # Selected the second fittest parent
        p1_idx = fitness_lst.index(p1)  # Collecting the index value for tracking the population
        p2_idx = fitness_lst.index(p2)  # Collecting the index value for tracking the population
        par1 = population[p1_idx]  # Tracking that value of population for which we got best fittest parent
        par2 = population[p2_idx]
        offspring_lst = []
        off1, off2 = crossover(par1, par2)
        ch1 = mutation(off1)
        ch2 = mutation(off2)
        offspring_lst.extend([ch1, ch2])
        population = offspring_lst

        fitness_lst2 = []  # finding fitness for the new population after doing mutation and crossover
        for i in population:
            fitness_lst2.append(fitness_function(i))
        fittest = min(fitness_lst2)
        best_index = fitness_lst2.index(fittest)
        fittest_chro = population[best_index]

        if fittest == 0:
            if sum(fittest_chro) != 0: # [0 0 0 0 0 0 0]
                for k in fittest_chro:
                    print(k, end=" ")
                did_printed = True
                break


def read_file():
    global lst_trans, t
    with open("task.txt") as f:
        t = int(f.readline())  # Total number of deposit and lend
        for i in range(t):
            line = f.readline().split()
            lst_trans.append((line[0], int(line[1])))
        # print(lst_trans)


# --------------------> Driver Code
population_size = 4
prob_crossover = 0.9
prob_mutation = 0.01
iteration_threshold = 1000    # 1 0 1
lst_trans = []  # lst_trans = [('l', 120), ('l', 289), ('d', 475), ('l', 195), ('d', 6482), ('l', 160), ('d', 935)]
t = 0  # Total number of deposit and lend
did_printed = False
read_file()
generate_fittest_output()
if not did_printed:
    print(-1)



# print(lst_trans)
# print()
#print(generate_population(t))

# [('l', 120), ('l', 289), ('d', 475), ('l', 195), ('d', 6482), ('l', 160), ('d', 935)]
# print(t)
