import math

x = 3
y = 4

px_y = [[0.5, 0.25, 0.25],[0.8, 0, 0.2]]
pxy = [[0.25, 0.125, 0.125], [0.4, 0, 0.1]]

hxy = 0

for i in range(y):
    for j in range(x):
        hxy += (-math.log2(px_y[i][j]))*pxy[i][j]
    
print(hxy)
