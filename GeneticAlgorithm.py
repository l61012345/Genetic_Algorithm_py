import math
import random


def initia_population(population_size: 'int>0',
                      chromosome_length: 'int>0') -> 'list':
    '''
    Function: 
    initialize the population

    Parameters:
    population_size - int > 0, the size of population
    chromosome_length - int > 0, the length of chromosome for each indiv

    Returns:
    population - list
    '''
    population = [[]]
    print('initializing the population')
    for i in range(population_size):
        indiv = []
        # random initialize one individual
        for j in range(chromosome_length):
            indiv.append(random.randint(0, 1))

        print('indiv:*', i, '   chromesome:', indiv)
        population.append(indiv)  # append to the population
    return population[1:]


def translation(population: 'list', gene_pattern: 'list', debug_print = True) -> 'list':
    '''
    Function:
    translate the genes into decimal value

    Parameters:
    population - two dimesion list
    gene_pattern - list, consisting the sequence number of breakpoint for each gene
                   sequence numbered as: [1,2,3,4,....]
                   i.e., gene_pattern=[2,6] will regard as: #1-#2 as a gene string, #3-#6 as another gene string
    debug_print - bool, whether to print the result

    Returns:
    population_trans - list
    '''
    population_trans = [[]]
    if debug_print == True:
        print('translation')
    for i in range(len(population)):
        indiv_trans = []
        string = []
        gene_trans = 0

        # divide corrsponding bits as a string of gene
        for k in range(len(gene_pattern)):
            string.append((''.join(
                str(population[i][gene_pattern[k - 1]:gene_pattern[k]]))
                           ).replace('[', '').replace(']', '').replace(
                               ',', '').replace(' ', ''))  # pattern：'[0 , 1]'

        # the 1st gene string
        string[0] = ''.join(
            str(population[i][0:gene_pattern[0]]).replace('[', '').replace(
                ']', '').replace(',', '').replace(' ', ''))

        # convert each string of gene to each decimal value of gene
        for m in range(len(string)):
            gene_trans = int(string[m], 2)
            indiv_trans.append(gene_trans)
        if debug_print == True:
            print('indiv:', i, '   chromosome:', indiv_trans)
        population_trans.append(indiv_trans)
    return population_trans[1:]


def evaluation(population_tran: 'list', debug_print = True) -> ['list', 'float']:
    '''
    Function:
    evaluate each indiv based on the fitness function.

    Parameters:
    population_tran - two dimension list
    debug_print - bool, whether to print the result

    Return:
    fitness_norm - list
    avg_fitness - float
    
    Notice:
    fitness function should be written and stored as: 
    "fitness_func.py" in the same folder with this program
    '''
    if debug_print == True:
        print('evaluation')
    from fitness_func import fitness_func as fitness_func  # load */fitness_func.py
    if debug_print == True:
        print('successfully load fitness function ')

    fitness = []
    fitness_norm = []
    for i in range(len(population_tran)):
        indiv_fitness = fitness_func(
            population_tran[i])  # calculate fitness function for each indiv
        if print == True:
            print('indiv:', i, '   fitness:', indiv_fitness)
        fitness.append(indiv_fitness)  # obtain the fitness list

    avg_fitness = sum(fitness) / float(len(fitness))  # calculate avg fitness
    print('average fitness:', avg_fitness)

    for j in range(len(fitness)):
        indiv_fitness_norm = fitness[j] / avg_fitness  # normalized fitness
        if debug_print == True:
            print('indiv:', j, '   normal fitness:', indiv_fitness_norm)
        fitness_norm.append(indiv_fitness_norm)
    return fitness_norm, avg_fitness


def selection(population: 'list', fitness_norm: 'list') -> 'list':
    '''
    Function:
    produce the indiv to the intermediate population based on its fitness.

    Parameters:
    population - two dimension list
    fitness_norm - list, the normalized fitness for every indiv in the population

    Return:
    population_inter - two dimension list
    individual_number - int, number of unique indiv. in each population
    '''
    population_inter = [[]]
    print('selection')

    for i in range(len(population)):
        # based on the integer part of the fitness, copy to the intermediate population
        copy_times = 0
        for j in range(int(fitness_norm[i])):
            population_inter.append(population[i])
            copy_times = copy_times + 1
            print('indiv:*', i, '   normal fitness:', fitness_norm[i],
                  '   Copy times:', copy_times)
        # based on the fraction part of the fitness, extra chance of production
        if random.random() < (fitness_norm[i] - int(fitness_norm[i])):
            population_inter.append(population[i])
            copy_times = copy_times + 1
            print('indiv:*', i, '   normal fitness:', fitness_norm[i],
                  '   Copy times:', copy_times, '   extra')
        else:
            print('indiv:*', i, '   normal fitness:', fitness_norm[i],
                  '   No extra copy')
        # number of unique indiv. in each population
        individual_number = len(list(set([tuple(t) for t in population_inter[1:]])))
    return population_inter[1:], individual_number


def single_crossover(population: 'list',
                     crossover_rate: '0<= float<= 1') -> ['list', 'bool']:
    '''
    Function:
    do the single crossover based on the crossover rate.

    Parameters:
    population - two dimension list
    crossover_rate - 0<=float<=1, the rate of crossover. 

    Return:
    population - two dimension list
    True or False - bool value
                    if there is only one indiv in current population, the function will return False
                    otherwise, it will return True
    '''
    chromesome_length = len(population[0])
    population_size = len(population)
    if population_size == 1:  # check whether there is only one indiv in the population
        print('【Warning】only one indiv in current population')
        return population, False
    else:
        print('single crossover   crossover rate:', crossover_rate)

        random.shuffle(population)
        print('shuffle')

        for i in range(0, population_size - 1, 2):
            if random.random(
            ) < crossover_rate:  # check each indiv with crossover rate
                print('========')
                print('indiv:', i, '   chromosome:', population[i],
                      '   crossovered: yes')
                print('indiv:', i + 1, '   chromosome:', population[i + 1],
                      '   crossovered: yes')
                cross_point = random.randint(
                    0,
                    chromesome_length - 1)  # random select the crossover point
                parent1 = []
                parent2 = []

                # for parent1, it combind with 0-cp for (i)th indiv and cp-final for (i+1)th indiv
                parent1.extend(population[i][0:cross_point])
                parent1.extend(population[i +
                                          1][cross_point:chromesome_length])

                # for parent2, it combind with 0-cp for (i+1)th indiv and cp-final for (i)th indiv
                parent2.extend(population[i + 1][0:cross_point])
                parent2.extend(population[i][cross_point:chromesome_length])
                population[i] = parent1
                population[i + 1] = parent2

                print('---after crossover---')
                print('indiv:', i, '   chromosome:', population[i],
                      '   crossovered: yes')
                print('indiv:', i + 1, '   chromosome:', population[i + 1],
                      '   crossovered: yes')

            else:
                # keep origin
                population[i] = population[i]
                population[i + 1] = population[i + 1]
                print('========')
                print('indiv:', i, '   chromosome:', population[i],
                      '   crossovered: not')
                print('indiv:', i + 1, '   chromosome:', population[i + 1],
                      '   crossovered: not')
        return population, True


def mutation(population: 'list', mutation_rate: '0<= float<= 1') -> 'list':
    '''
    Function:
    do the mutation based on the mutation rate.

    Parameters:
    population - two dimension list
    mutation_rate - 0<=float<=1, the rate of crossover. 

    Return:
    population - two dimension list
    '''
    population_size = len(population)
    chromesome_length = len(population[0])
    print('mutation  mutation rate:', mutation_rate)

    for i in range(population_size):
        if random.random(
        ) < mutation_rate:  # chech each indiv with mutation rate
            mutation_point = random.randint(
                0, chromesome_length - 1)  # random select the mutation point
            print('indiv:', i, '   chromosome:', population[i],
                  '   mutated: yes', '   mutation point:', mutation_point)

            # if this element is 1, then change to be 0.
            if population[i][mutation_point] == 1:
                population[i][mutation_point] = 0
            else:
                # if this element is 0, then change to be 1.
                population[i][mutation_point] = 1
            print('---after mutation---')
            print('indiv:', i, '   chromosome:', population[i],
                  '   mutated: yes')
            print('========')
        else:
            population[i] = population[i]
            print('indiv:', i, '   chromosome:', population[i],
                  '   mutated: not')
            print('========')
    return population