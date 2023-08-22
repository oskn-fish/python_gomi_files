import numpy as np
import math
import matplotlib.pyplot as plt

X_MAX = 100
SAMPLE_SIZE = 10000
LAMBDA = 20

def sample_poisson(param: float, x_max: int, sample_size: int) -> list:
    # samples = np.random.randint(1,x_max+1, sample_size)
    samples = []
    # for _ in range(sample_size):
    while len(samples)<sample_size:
        x = np.random.randint(1, x_max)
        y = np.random.rand()
        if y < poisson_distoribution(param, x):
            samples.append(x)

    return samples

def poisson_distoribution(param:float, k: int) -> float:
    return np.exp(-param)*(param**k)/math.factorial(k)
    
    
if __name__ == "__main__":
    # samples = sample_poisson(LAMBDA, X_MAX, SAMPLE_SIZE)
    # plt.hist(samples)
    # plt.show()
    y = [poisson_distoribution(LAMBDA, k) for k in range(X_MAX)]
    plt.bar(range(X_MAX), y)
    plt.show()