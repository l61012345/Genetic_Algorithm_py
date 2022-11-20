import math
import random

def initia_population(population_size, chromosome_length):
# initialize the population
    population = [[]]
    for i in range(population_size):
        indiv = []
        # random initialize one individual
        for j in range(chromosome_length):
            indiv.append(random.randint(0,1))
        population.append(indiv) # append to the population
    return population[1:]


def translation(population,gene_length):
# translate the genes into decimal value
    population_trans = [[]]
    for i in range(len(population)):
        indiv_trans = []
        for j in range(len(population[i])):
            gene_trans = population[i][j]*(math.pow(2,j)) # 如何几个一组求幂
            indiv_trans.append(gene_trans)
        population_trans.append(indiv_trans)
    return population_trans
           
           
def single_crossover(population,crossover_rate):
    chromesome_length = len(population[0])
    random.shuffle(population)
    for i in range(0,len(population)-1,2):
        if random.random()< crossover_rate:
            cross_point=random.randint(0,chromesome_length) # random generate the crossover point
            parent1=[]
            parent2=[]
            parent1.extend(population[i][0:cross_point])
            parent1.extend(population[i+1][cross_point:chromesome_length])
            
            parent2.extend(population[i+1][0:cross_point])
            parent2.extend(population[i][cross_point:chromesome_length])
            population[i]=parent1
            population[i+1]=parent2
        else:
            population[i]=population[i]
            population[i+1]=population[i+1]
    return population


# testing
m = initia_population(2, 10)
print(m)
m_d = single_crossover(m,0.9)
print('--')
print(m_d)
        