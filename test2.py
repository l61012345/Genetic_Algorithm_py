import GeneticAlgorithm as GA
import matplotlib.pyplot as plt

m = GA.initia_population(10, 10)
avg_fitness = 1
epoches = 0
fitness = []
flag = True

while avg_fitness<1200:
    print('======Round:',epoches,'==============')
    m_t = GA.translation(m,[2,4,7,10])
    m_f,avg_fitness = GA.evaluation(m_t)
    m = GA.selection(m, m_f)
    m,flag = GA.single_crossover(m,0.8)
    m = GA.mutation(m,0.1)
    fitness.append(avg_fitness)
    epoches = epoches + 1
    if epoches == 1000:
        break
    elif flag == False:
        break
    
print('finish')
print('=============================')
print('epoches:   ', epoches)
print('max fitness:   ', max(fitness))
print('winners:')
print(m)
plt.plot(fitness)
plt.show()