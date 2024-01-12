
#%%
import math
import numpy as np
import matplotlib.pyplot as plt

TIME_STEP  = 10000
INDICES = [1, 2, 3, 4, 5, 6]

#%%
_p = 1.0-np.power(0.1, INDICES)
_p = _p.reshape((len(INDICES), 1))
p = _p*np.ones((len(INDICES), TIME_STEP))
_x = np.arange(TIME_STEP).reshape((1,TIME_STEP))
x = _x*np.ones((len(INDICES), TIME_STEP))
x = np.transpose(x)
x = np.transpose(x)
y = np.power(p, x)
        

# %%
yoko = np.arange(TIME_STEP)
for i in range(len(y)):
    plt.plot(yoko, y[i])
# %%
plt.show()
# %%
