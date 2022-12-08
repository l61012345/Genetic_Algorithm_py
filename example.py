import Adaptive_GeneticAlgorithm as GA
import matplotlib.pyplot as plt

m = GA.initia_population(10, 10)
avg_fitness = 1
epoches = 0
fitness = []
flag = True

def fitness_func(x):
    y= x[0] + x[1]+ pow((2*(x[2]))+(3*(x[3])),2)
    return float(y)

while (epoches<3 & flag == True):
    print('======Round:',epoches,'==============')
    m_t = GA.translation(m,[2,4,7,10])
    m_nf, m_f, avg_fitness, max_fitness = GA.evaluation(m_t, fitness_func)
    print(m_f)
    print(m)
    m,number = GA.selection(m, m_nf)
    m,flag = GA.adaptive_single_crossover(m,m_f,max_fitness,avg_fitness)
    print(m)
    m = GA.mutation(m,0.1)
    fitness.append(avg_fitness)
    epoches = epoches + 1
    
print('finish')
print(epoches)
print(m)
plt.plot(fitness)
plt.show()