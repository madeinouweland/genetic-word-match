import random
import string

target = "FRIEDRICHSHAGEN"
target_length = len(target)
mutate_rate = .1 / target_length

steps = 0
initial_population_count = 50

population = [''.join(random.choice(string.ascii_uppercase) for x in range(target_length)) for y in range(initial_population_count)]
print('original population', len(population), population)


def calculate_word_fitness(word):
    score = 0
    for i in range(target_length):
        if target[i] == word[i]:
            score = score + 1
    return score / target_length


def create_mating_pool(population):
    pool = []
    for p in population:
        fitness = int(calculate_word_fitness(p) * 100)
        if (fitness > 2):
            for f in range(fitness):
                pool.append(p)
    return pool


def mate(parent_pool):
    parent1 = random.choice(parent_pool)
    parent2 = random.choice(parent_pool)
    split_index = random.randint(0, target_length - 1)

    child = ""
    for i in range(target_length):
        if random.random() < mutate_rate:
            gene = random.choice(string.ascii_uppercase)  # mutate gene
        elif i <= split_index:
            gene = parent1[i]  # take gene from parent 1
        else:
            gene = parent2[i]  # take gene from parent 2

        child = child + gene
    return child


while 1:
    average = sum([calculate_word_fitness(p) for p in population]) / len(population)
    new_population = []
    for p in population:
        pool = create_mating_pool(population)
        child = mate(pool)
        print(f'step {steps}, {child}, avg: {average}')
        new_population.append(child)
        if child == target:
            exit()
    population = new_population
    population = [p for p in population if calculate_word_fitness(p) > 0]
    steps = steps + 1
