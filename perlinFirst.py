import numpy as np
from random import randint
from perlin_numpy import (
    generate_perlin_noise_2d
)

seed = randint(0, 5000)

np.random.seed(seed)
noise = generate_perlin_noise_2d((15, 15), (1, 1))

maxList = []
minList = []

layer_9 = []
layer_8 = []
layer_7 = []
layer_6 = []
layer_5 = []
layer_4 = []
layer_3 = []
layer_2 = []
layer_1 = []
layer0 = []
layer1 = []
layer2 = []
layer3 = []
layer4 = []
layer5 = []
layer6 = []
layer7 = []
layer8 = []
layer9 = []

for i in range(len(noise)):
    for j in range(i):
        noise[i][j] = noise[i][j] * 10
        if noise[i][j] < 0 and noise[i][j] > -1:
            noise[i][j] = 0
        if noise[i][j] == -9:
            layer_9.append(1)
        else:
            layer_9.append(0)
        if noise[i][j] == -8:
            layer_8.append(1)
        else:
            layer_8.append(0)
        if noise[i][j] == -7:
            layer_7.append(1)
        else:
            layer_7.append(0)
        if noise[i][j] == -6:
            layer_6.append(1)
        else:
            layer_6.append(0)
        if noise[i][j] == -5:
            layer_5.append(1)
        else:
            layer_5.append(0)
        if noise[i][j] == -4:
            layer_4.append(1)
        else:
            layer_4.append(0)
        if noise[i][j] == -3:
            layer_3.append(1)
        else:
            layer_3.append(0)
        if noise[i][j] == -2:
            layer_2.append(1)
        else:
            layer_2.append(0)
        if noise[i][j] == -1:
            layer_1.append(1)
        else:
            layer_1.append(0)
        if noise[i][j] == 0:
            layer0.append(1)
        else:
            layer0.append(0)
        if noise[i][j] == 1:
            layer1.append(1)
        else:
            layer1.append(0)
        if noise[i][j] == 2:
            layer2.append(1)
        else:
            layer2.append(0)
        if noise[i][j] == 3:
            layer3.append(1)
        else:
            layer3.append(0)
        if noise[i][j] == 4:
            layer4.append(1)
        else:
            layer4.append(0)
        if noise[i][j] == 5:
            layer5.append(1)
        else:
            layer5.append(0)
        if noise[i][j] == 6:
            layer6.append(1)
        else:
            layer6.append(0)
        if noise[i][j] == 7:
            layer7.append(1)
        else:
            layer7.append(0)
        if noise[i][j] == 8:
            layer8.append(1)
        else:
            layer8.append(0)
        if noise[i][j] == 9:
            layer9.append(1)
        else:
            layer9.append(0)
    maxList.append(max(noise[i]))
    minList.append(min(noise[i]))
        
noise = np.trunc(noise)

print(int(max(maxList)), int(min(minList)))
    
print(noise)
print("Seed :", seed)