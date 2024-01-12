import math
sum = 0
for i in range(1, 7):
    sum += math.comb(12-i, i-1)
    print(math.comb(12-i, i-1))
print("----")
print(sum)