import GeneticAlgorithm as GA
# testing
m = GA.initia_population(20, 10)
print(m)

#print('--')
#m_d = GA.single_crossover(m,0.6)
#print(m_d)

print('--')
m_c = GA.translation(m,[2,4,7,10])
print(m_c)
        
print('--')
'''
def fitness_func(x):
    y= x[0] + x[1]+ x[2]+ x[3]
    return y
'''

m_f,avg_fitness = GA.evaluation(m_c)
print(m_f)

'''
print('--')
m_i = GA.selection(m, m_f)
print(m_i)

print('--')
m_m = GA.mutation(m,0.7)
print(m_m)
'''