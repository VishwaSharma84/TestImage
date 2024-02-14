from PIL import Image
import requests
from io import BytesIO
import zipfile
import pathlib 
import random
import os



def data_extraction():
    glioma_tumor_images = os.listdir(os.path.join(os.getcwd(),"BrainTumorData\Training\glioma"))
    meningioma_tumor_images = os.listdir(os.path.join(os.getcwd(),"BrainTumorData\Training\meningioma"))
    no_tumor_images = os.listdir(os.path.join(os.getcwd(),"BrainTumorData\Training\\tumor"))
    pituitory_tumor_images = os.listdir(os.path.join(os.getcwd(),"BrainTumorData\Training\pituitary"))
    path = pathlib.Path(os.path.join(os.getcwd(),"BrainTumorData\Training"))

    return path,glioma_tumor_images,meningioma_tumor_images,no_tumor_images,pituitory_tumor_images

    
data_extraction()