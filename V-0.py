import matplotlib.pyplot as plt
import numpy as np




def heightmapCreator(seed, size):
    np.random.seed(seed)
    heightmap = np.random.uniform(0.01, 1, (size, size)).round(2)
    return heightmap

def smoothHeightmap(heightmap):
    size = len(heightmap)
    smooth_heightmap = np.empty((size - 1, size - 1))
    for r in range(size - 1):
        for c in range(size - 1):
            a = (heightmap[r][c] + heightmap[r][c + 1] + heightmap[r + 1][c] + heightmap[r + 1][c + 1]) / 4
            smooth_heightmap[r][c] = a
    return smooth_heightmap



heightmap = heightmapCreator(1, 10)
smooth_heightmap = smoothHeightmap(heightmap)


plt.imshow(smooth_heightmap)
plt.show()
