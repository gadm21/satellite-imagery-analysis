

from utils import * 
from functools import reduce


def read_and_cluster():
    tifs = list_tifs(results_path)

    dataset = read_tif(tifs[0]) 

    band = dataset.GetRasterBand(1).ReadAsArray() 


    clustered = kmean_cluster(band) 
    print("got the cluster")
    save_image(os.path.join(results_path, 'clustered'), clustered)
    print("saved cluster of shape:{}".format(clustered.shape) )

    show_image(clustered) 



def get_and_save_rgb_image():
    
    rgb = np.array([get_band(5, crop_part=(2000, 2000, 5000, 5000)),
                    get_band(4, crop_part=(2000, 2000, 5000, 5000)),
                    get_band(3, crop_part=(2000, 2000, 5000, 5000))])
    rgb = np.moveaxis(rgb, 0, -1) 

    save_image(os.path.join(results_path, 'real'), rgb)


def get_and_save_gray_image():
    
    for band in range(1, 12):
        print("getting band:", band) 
        rgb = np.array([get_band(band, normalize=False, equalize=False)])
        rgb = np.moveaxis(rgb, 0, -1)
        
        save_image2(os.path.join(results_path, 'real_'+str(band)), rgb)


get_and_save_gray_image()


