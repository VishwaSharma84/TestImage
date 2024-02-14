from data_extraction import data_extraction
from PIL import Image
import requests
from io import BytesIO
import zipfile
import pathlib 
import random
import os


def data_visualization():
    path,glioma_tumor_images,meningioma_tumor_images,no_tumor_images,pituitory_tumor_images = data_extraction()

    def open_random_image(path):
        # Get a list of all files in the folder
        all_files = os.listdir(path)
        random_image_file = random.choice(all_files)
        image_path = os.path.join(path, random_image_file)
        image = Image.open(image_path)
        return image
    
    glioma_tumor_image = open_random_image(os.path.join(os.getcwd(),"BrainTumorData\Training\glioma"))
    meningioma_tumor_image = open_random_image(os.path.join(os.getcwd(),"BrainTumorData\Training\meningioma"))
    no_tumor_image = open_random_image(os.path.join(os.getcwd(),"BrainTumorData\Training\\tumor"))
    pituitory_tumor_image = open_random_image(os.path.join(os.getcwd(),"BrainTumorData\Training\pituitary"))
    glioma_tumor_image.save('glioma_tumor.jpg')
    meningioma_tumor_image.save('meningioma_tumor.jpg')
    no_tumor_image.save('no_tumor.jpg')
    pituitory_tumor_image.save('pituitory_tumor.jpg')
    
    return path,glioma_tumor_images,meningioma_tumor_images,no_tumor_images,pituitory_tumor_images

data_visualization()
