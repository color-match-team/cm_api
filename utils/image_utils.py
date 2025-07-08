import numpy as np
#import matplotlib.pyplot as plt

import cv2
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

def pallette(image_uploaded, n_colors):
    image = cv2.imread(image_uploaded)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(image.shape)
    r, c = image.shape[:2]
    out_r = 120
    image = cv2.resize(image, (int(out_r*float(c)/r), out_r))
    print(type(image))
    pixels = image.reshape((-1, 3))
    #print(pixels.shape)
    #print(image.shape)

    km = KMeans(n_clusters=int(n_colors))
    km.fit(pixels)

    colors = np.asarray(km.cluster_centers_, dtype='uint8')
    return list(map(tuple, colors))


print(pallette("testing_images/zushi.jpg", 2))