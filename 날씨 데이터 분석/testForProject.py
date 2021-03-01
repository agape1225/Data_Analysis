import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,6,7]
z = [0,9,10]

result = {}

for i in range(1910,2011,10):
    if i // 100 == 195:
        continue
    buff = []
    for j in range(i, i + 10):
        buff.append(j)
    result[i] = buff

print(result)
