
#%%
#matplotlib inline
import matplotlib.pyplot as plt

DLTs = [231, 893, 2044, 3097, 3613, 5084, 8149, 12845, 15957, 18322, 14422, 9438, 4329, 1293, 257, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

plt.bar(list(range(len(DLTs))), DLTs)

# %%
average = 0
for i in range(len(DLTs)):
    average += DLTs[i]*i
average = average/sum(DLTs)
print(average)    

# %%
len(DLTs)
# %%
sum(DLTs)
# %%
[DLT/sum(DLTs) for DLT in DLTs]
# %%
import math
sqrt = [math.sqrt(i) for i in range(1, 10001)]
log_sqrt = [math.sqrt(math.log(i)) for i in range(1, 10001)]
fig, ax = plt.subplots()
ax.plot(sqrt)
ax.plot(log_sqrt)
ax.legend()
plt.show()

# %%
log_sqrt
# %%
culmutive = []
for i in range(len(DLTs)):
    culmutive.append(sum(DLTs[0:1+i])/sum(DLTs))
    
    print(f"{i=}, {(sum(DLTs[0:1+i])/sum(DLTs))=}")
# %%
fig, ax = plt.subplots()
ax.plot(culmutive)
plt.show()

# %%
