import os
import numpy as np
from skimage.io import imread, imsave
from skimage.util import crop

# assign directory
directory = "attachments/"
new_directory= "attachments-split/"

# iterate over files in
# that directory
list_of_image_paths = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and ".DS_Store" not in f:
        list_of_image_paths.append(f)

images = []

for image in list_of_image_paths:
    img = imread(image)
    """crop_width{sequence, int}
Number of values to remove from the edges of each axis. 
((before_1, after_1), … (before_N, after_N)) specifies unique 
crop widths at the start and end of each axis. ((before, after),) 
or (before, after) specifies a fixed start and end crop for every 
axis. (n,) or n for integer n is a shortcut for before = after = n 
for all axes."""
    image = image.replace('attachments/', '')
    cropped = crop(img, ((0, 512), (0, 512), (0,0)), copy=False)
    imsave(new_directory+image, cropped)

# SAVE WITH IMAGE NAME CORRECTLY!!!