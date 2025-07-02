import random

def initialize_population(population_size, board_size):
    return [[random.randint(0, board_size-1) for _ in range(board_size)] for _ in range(population_size)]

def fitness(chromosome):
    clashes = 0
    for i in range(len(chromosome)):
        for j in range(i + 1, len(chromosome)):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                clashes += 1
    return clashes

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = random.randint(0, len(chromosome) - 1)
    return chromosome

def genetic_algorithm(population_size, board_size, generations, mutation_rate):
    population = initialize_population(population_size, board_size)

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x))
        new_population = []

        for i in range(0, population_size, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

        if fitness(population[0]) == 0:
            print("Solution found in generation:", generation)
            return population[0]

    print("No solution found.")
    return None

if __name__ == "__main__":
    population_size = 100
    board_size = 8
    generations = 1000
    mutation_rate = 0.1

    solution = genetic_algorithm(population_size, board_size, generations, mutation_rate)
    print("Solution:", solution)
