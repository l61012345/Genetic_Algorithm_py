import math
import random


def initia_population(population_size: 'int>0', 
                      chromosome_length: 'int>0'):
    population = [[]]
    for i in range(population_size):
        indiv = []
        # random initialize one individual
        for j in range(chromosome_length):
            indiv.append(random.randint(0,1))
        population.append(indiv) # append to the population
    return population[1:]



def translation(population,
                gene_pattern):
# translate the genes into decimal value
# population [[0,1,0,1,0],[1,0,1,1,1],..]
# gene_pattern is an array consisting the sequence number of breakpoint for each gene
# sequence numbered as: [1,2,3,4,....]
# i.e., gene_pattern=[2,6] will regard as: #1-#2 as a gene string, #3-#6 as another gene string
    population_trans = [[]]
    for i in range(len(population)):
        indiv_trans = []
        string = []
        gene_trans = 0
        for k in range(len(gene_pattern)):
            # divide corrsponding bits as a string of gene
            # pattern：'[0 , 1]'
            # string.append(''.join(str(population[i][l]) for l in range(gene_pattern[k-1],gene_pattern[k])))
            string.append((''.join(str(population[i][gene_pattern[k-1]:gene_pattern[k]])))
                          .replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))
        # the 1st gene string
        string[0] = ''.join(str(population[i][0:gene_pattern[0]])
                            .replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))
        print(string)
         # convert each string of gene to each decimal value of gene
        for m in range(len(string)):
            gene_trans = int(string[m],2)
            indiv_trans.append(gene_trans)
        population_trans.append(indiv_trans)
    return population_trans[1:]


def evaluation(population_tran):
    from fitness_func import fitness_func
    # load */fitness_func.py
    fitness = []
    for i in range(len(population_tran)):
       indiv_fitness = fitness_func(population_tran[i]) # calculate fitness function for each indiv
       fitness.append(indiv_fitness) # obtain the fitness list
    return fitness


def selection(population,fitness):
    population_selected = [[]]
    total_fitness = sum(fitness)
    for i in range(len(population)):
        i =1
    return population_selected



def single_crossover(population,
                     crossover_rate: '0<= float<= 1'):
    chromesome_length = len(population[0])
    population_size = len(population)
    random.shuffle(population)
    for i in range(0,population_size-1,2):
        if random.random()< crossover_rate: # check each indiv with crossover rate
            cross_point=random.randint(0,chromesome_length-1) # random select the crossover point
            parent1=[]
            parent2=[]
            # for parent1, it combind with 0-cp for (i)th indiv and cp-final for (i+1)th indiv
            parent1.extend(population[i][0:cross_point])
            parent1.extend(population[i+1][cross_point:chromesome_length])
            # for parent2, it combind with 0-cp for (i+1)th indiv and cp-final for (i)th indiv
            parent2.extend(population[i+1][0:cross_point])
            parent2.extend(population[i][cross_point:chromesome_length])
            population[i]=parent1
            population[i+1]=parent2
        else:
            population[i]=population[i]
            population[i+1]=population[i+1]
    return population


def mutation(population,
             mutation_rate: '0<= float<= 1'):
    population_size = len(population)
    chromesome_length = len(population[0])
    for i in range(population_size-1):
        if random.random()< mutation_rate: # chech each indiv with mutation rate
            mutation_point=random.randint(0,chromesome_length-1) # random select the mutation point
            # if this element is 1, then change to be 0.
            if population[i][mutation_point]==1:
                population[i][mutation_point]=0
            else:
            # if this element is 0, then change to be 1.
                population[i][mutation_point]=1
        else:
            population[i]=population[i]


# testing
m = initia_population(4, 10)
print(m)
#m_d = single_crossover(m,0.9)
#print('--')
#print(m_d)
print('--')
m_c = translation(m,[2,4,10])
print(m_c)
        
print('--')
m_f = evaluation(m_c)
print(m_f)


    
