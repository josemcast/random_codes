import numpy as np 
import os 
import matplotlib.pylab as plt

x, y = [350], [350]

def random_walk(n_steps):
    
    plt.scatter(x[-1] + np.random.choice([-1, 1], p=[1/3, 2/3]), y[-1] + np.random.choice([-1, 1], p=[1/3, 2/3]))
    for _ in range(n_steps):
        
        x[-1] = x[-1] + np.random.choice([-1, 1], p=[1/3, 2/3])
        y[-1] = y[-1] + np.random.choice([-1, 1], p=[1/3, 2/3])
        plt.scatter(x[-1], y[-1])
        plt.pause(0.05)


random_walk(1000)
plt.show()
