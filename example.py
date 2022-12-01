import GeneticAlgorithm as GA
import matplotlib.pyplot as plt

m = GA.initia_population(10, 10)
avg_fitness = 1
epoches = 0
fitness = []

while (avg_fitness<42) or (avg_fitness == 0):
    print('======Round:',epoches,'==============')
    m_t = GA.translation(m,[2,4,7,10])
    m_f,avg_fitness = GA.evaluation(m_t)
    m = GA.selection(m, m_f)
    m = GA.single_crossover(m,0.8)
    m = GA.mutation(m,0.1)
    fitness.append(avg_fitness)
    epoches = epoches + 1
    
print('finish')
print(epoches)
print(m)
plt.plot(fitness)
plt.show()