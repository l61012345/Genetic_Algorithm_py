# fitness_function.py
def fitness_func(x):
    y= x[0] + x[1]+ pow((2*(x[2]))+(3*(x[3])),2)

    return float(y)
