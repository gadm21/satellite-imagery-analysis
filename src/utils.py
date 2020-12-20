

import numpy as np
from sklearn import cluster 
from osgeo import gdal, gdal_array 
import os 
import matplotlib.pyplot as plt
import cv2
from skimage import exposure 
#import geopandas as gpd
from PIL import Image


gdal.UseExceptions()
gdal.AllRegister()


TIF_path = r'C:\Users\gad\Desktop\UN ESCWA\satellite\LandSat8\zayed_12_19_2020\LC08_L1TP_177039_20201219_20201219_01_RT'
results_path = 'results'


def list_tifs(path= TIF_path):
    all_files = os.listdir(path) 
    return [os.path.join(path, file) for file in all_files if file[-3:].lower()=='tif'] 

def read_tif(path):
    return gdal.Open(path, gdal.GA_ReadOnly) 

def get_band(band_num, crop_part=None, normalize=True, equalize=True):
    tifs = list_tifs() 
    tif = Image.open(tifs[band_num-1]) 
    if crop_part is not None :
        tif = tif.crop(crop_part)
    image = np.array(tif) 
    #if normalize: image = ((image.astype(np.float32) / np.max(image) )*65535).astype(np.uint16)
    if normalize: image = ((image.astype(np.float32) / np.max(image) )*255).astype(np.uint8)
    if equalize : image = exposure.equalize_hist(image) 

    return image

def kmean_cluster(band):
    X = band.reshape((-1, 1))

    kmeans = cluster.KMeans(n_clusters=8) 
    kmeans.fit(X) 

    return kmeans.labels_.reshape((band.shape))


def show_image(image):
    cv2.imshow('r', image) 
    cv2.waitKey(0) 
    cv2.destroyWindow('r')

def show_image2(image):
    plt.imshow(image, cmap='hsv')
    plt.show()


def save_image(path, image):
    path += '.jpg'
    cv2.imwrite(path, image) 

def save_image2(path, image):
    path += '.png'
    plt.imsave(path, image, cmap='coolwarm')