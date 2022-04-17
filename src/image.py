from tkinter import BaseWidget
import cv2
import numpy as np

def image_BWresize(path):
    '''
    path: image path 
    change image to black and white 
    changing resolution to 28 x 28
    return reshaped numpy array of dimension 28x28x1
    '''
    image = cv2.imread(path)
    bwimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    bwimage_resize = cv2.resize(bwimage,(28,28))
    newImage = bwimage_resize.reshape(-1,28,28,1)
    return newImage
