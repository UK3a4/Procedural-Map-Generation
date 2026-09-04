import matplotlib.pyplot as plt
import numpy as np




def heightmapCreator(seed, size):
    np.random.seed(seed)
    first_number = round(np.random.uniform(0.01, 1), 2)
    heightmap = np.empty((size, size))
    heightmap[0, 0] = first_number
    for r in range(size):
        for c in range(size):
            #first number at first row [0,0]
            if r == 0 and c == 0:
                continue
            elif r == 0 and c != 0:
                # first-last first row [1: ]
                heightmap[r, c] = heightmap[r, c - 1] * np.random.uniform(0.8, 1.2)
            #first column 
            elif r != 0 and c == 0:
                heightmap[r, c] = heightmap[r - 1, c] * np.random.uniform(0.8, 1.2)
            else:
                heightmap[r, c] = (heightmap[r, c - 1] + heightmap[r - 1, c]) / 2 * np.random.uniform(0.8, 1.2)
    return heightmap


def amplitude(amplitude, heightmap):
    heightmap = amplitude * heightmap
    return heightmap


def smoothHeightmap(heightmap):
    size = len(heightmap)
    smooth_heightmap = np.empty((size - 1, size - 1))
    for r in range(size - 1):
        for c in range(size - 1):
            a = (heightmap[r][c] + heightmap[r][c + 1] + heightmap[r + 1][c] + heightmap[r + 1][c + 1]) / 4
            smooth_heightmap[r][c] = a
    return smooth_heightmap



heightmap = heightmapCreator(3, 500)
heightmap = amplitude(1, heightmap)
smooth_heightmap = smoothHeightmap(heightmap)

plt.imshow(smooth_heightmap)
plt.show()
