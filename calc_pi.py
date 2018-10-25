import numpy as np 

m, n = 0, 0

max_it = 100000

while (n < max_it):

    np.random.seed(n)
    u1 = np.random.random()
    u2 = np.random.random()

    x = 2*u1
    y = 2*u2

    if (((x - 1)*(x - 1) + (y - 1)*(y - 1)) <= 1):
        m += 1
    
    n +=1

pi = 4.0*(m/n)
print(pi)