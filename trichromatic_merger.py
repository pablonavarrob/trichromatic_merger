import rawpy
import imageio
import multiprocessing as mp
import numpy as np
import glob
import sys
import time
import os

start = time.time()

# folder_path = '/Users/pabnb/Desktop/Film 1/'
# folder_path = sys.argv[1]
# file_name = sys.argv[2]
file_name = 'gold_200'
folder_path = '/Users/pabnb/Desktop/Film 1'
filenames = sorted([file for file in glob.glob(folder_path + '/*.RAF')])
save_folder = 'Gold 200 - Python Linearization'
os.mkdir('./' + save_folder)

PARAMS_CONVERSION = {
    'demosaic_algorithm' : rawpy.DemosaicAlgorithm(3),
    'no_auto_bright' : True,
    'output_bps' : 16,
    'gamma' : (1, 1),
    'output_color' : rawpy.ColorSpace(0),
    'user_wb' : [1, 1, 1, 1],
    'four_color_rgb' : True,
    # 'median_filter_passes': 3
} 

# Processing for loop
i = 0
for path_red, path_green, path_blue in zip(filenames[0::3], filenames[1::3], filenames[2::3]):
    with rawpy.imread(path_red) as raw:
        red = raw.postprocess(**PARAMS_CONVERSION)

    with rawpy.imread(path_green) as raw:
        green = raw.postprocess(**PARAMS_CONVERSION)

    with rawpy.imread(path_blue) as raw:
        blue = raw.postprocess(**PARAMS_CONVERSION)

    merged_frames = np.zeros(red.shape)
    merged_frames[:, :, 0] = red[:, :, 0]
    merged_frames[:, :, 1] = green[:, :, 1]
    merged_frames[:, :, 2] = blue[:, :, 2]

    i += 1
    print(i)
    imageio.imsave('/Users/pabnb/Desktop/' +
                   save_folder + file_name + 'frame_{}.tiff'.format(i), merged_frames.astype('uint16'))

end = time.time()
print('Linearization of {} frames took {} seconds'.format(
    int(len(filenames)/3), end-start))
