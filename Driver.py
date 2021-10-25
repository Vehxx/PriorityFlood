from noise import snoise2
from PIL import Image
import numpy as np

from PriorityFlood import PriorityFlood


def create_noise_map():
    noise_map = [[0 for x in range(1024)] for y in range(1024)]
    octaves = 32
    frequency = 16.0 * octaves

    for i in range(len(noise_map)):
        for j in range(len(noise_map[0])):
            noise_map[i][j] = snoise2(i / frequency, j / frequency, octaves)

    return noise_map


if __name__ == '__main__':
    # create the initial dem
    dem = create_noise_map()

    # run priority flood on the dem
    pf = PriorityFlood(dem)
    pf.flood()
    dem = pf.get_dem()

    # format it to be turned into an image
    dem = np.array(dem)
    dem += 1
    dem *= 127
    dem = np.uint8(dem)

    # create the image and save to a file
    image = Image.fromarray(dem, "L")
    image.save("out/filled.png")
