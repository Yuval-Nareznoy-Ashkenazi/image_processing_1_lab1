from matplotlib import pyplot as plt
import numpy as np
import rawpy
import imageio


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    image = np.empty((1376, 960), np.uint16)
    image = open('title.raw')
    with rawpy.imread('title.raw') as raw:
        rgb = raw.postprocess()
    imageio.imsave('default.tiff', rgb)
    plt.imshow(image)

