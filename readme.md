# GeneticAlogrithm - Python Genetic Algorithm Libraries
## Functions
### `initial_population`  
random initialize the population with specified population size and chromosome length.  

```python
initia_population(
    population_size: 'int>0',
    chromosome_length: 'int>0'
)
```
   
| Args | | |
|:-|:-|:-|
|`population_size`| int>0 |The size of initial population.|
|`chromosome_length`|int>0|The length of chromosome for each individual.|

| Returns | | |
|:-|:-|:-|
|`population` | 2x list | The list of initial population |

### `translation`
Translate the genes into decimal value based on specified gene pattern.

```python
translation(
    population: 'list', 
    gene_pattern: 'list'
)
```
| Args | | |
|:-|:-|:-|
|`population`| 2x list  |The population to be translated.|
|`gene_pattern`| list | The gene pattern which contents the sequence number of breakpoints specilized to be a gene.<br>Sequence numbered as: [1,2,3,4,....]<br> i.e., gene_pattern=[2,6] will regard as: #1-#2 as a gene string, #3-#6 as another gene string.|

| Returns | | |
|:-|:-|:-|
|`population_trans` | 2x list | The list of population whose the genes for each individual are specified and stored in decimal value.|

### `evaluation`
Evaluate each indiv based on the sepecified fitness function.  

| Args | | |
|:-|:-|:-|
|`population_tran`| 2x list  |The population to be evaluated.|

**Notice**:  
Fitness function should be written and stored as:   
"fitness_func.py" in the same folder with this program.  

an example of fitness function:  
```python
def fitness_func(x):
    y= x[0] + x[1]+ pow((2*(x[2]))+(3*(x[3])),2)
    return float(y)
```

| Returns | | |
|:-|:-|:-|
|`fitness_norm` | list | The list of normalized fitness for each individual in current population. |
|`avg_fitness` | float | The average fitness of current population. |

### `selection`
Duplicate each individual to the intermediate population based on its fitness.

```python
selection(
    population: 'list', 
    fitness_norm: 'list'
)
```

| Args | | |
|:-|:-|:-|
|`population`| 2x list  |The population to be selected.|
|`fitness_norm` | list | The normalized fitness for every individual in the population. |

| Returns | | |
|:-|:-|:-|
|`population_inter` | 2x list | The list of  intermediate population. |

### `single_crossover`
Do the single crossover for paired individuls based on the crossover rate with following steps:
- Shuffle the individuals in the current population.
- Individual [i] will be paired with its neighbor [i+1]
  - For each paire, a crossover point will be randomly selected.
  - Exchange the segments after the crossover point.

```python
single_crossover(
    population: 'list',
    crossover_rate: '0<= float<= 1'
)
```



| Args | | |
|:-|:-|:-|
|`population`| 2x list  |The population to be crossovered.|
|`crossover_rate` | 0<=float<=1 | The rate of crossover. |

| Returns | | |
|:-|:-|:-|
|`population` | 2x list | The list of crossovered population. |
|`True` | Boolean value | Indicator, there is more than one individual in current population. |
|`False` |Boolean value | Indicator, there is only one individual in current population. | 

**Notice**:  
If there is only one individual in the current population, the individual may crossovered with a list consisting of 0s.   
This function will exam whether there is only one individual in current population. If there is only one indiv in current population, the function will return False and there will be a prompted warning "【Warning】only one indiv in current population". Otherwise, it will return True.  

### `mutation`
Do the mutation for individuls based on the mutation rate with following steps:
- For each individual, a mutation point will be randomly selected.
- The selected bit on the string will be inverted:  
  - If selected point is 1, it will change to be 0.
  - If selected point is 0, it will change to be 1.

```python
mutation(
    population: 'list',
    mutation_rate: '0<= float<= 1'
)
```

| Args | | |
|:-|:-|:-|
|`population`| 2x list  |The population to be mutated.|
|`mutation_rate` | 0<=float<=1 | The rate of mutation. |

| Returns | | |
|:-|:-|:-|
|`population` | 2x list | The list of mutated population. |

## Libraries used
- `math`  
- `random` 