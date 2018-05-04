import cv2
import os, os.path
import numpy as np
import cv2
import scipy.misc

def load_dir(dir_path = "images/"): 
    """
        load all images from directory
    """
    print("-loading images from %s"%(dir_path))
    image_path_list = []
    valid_image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]
    image_list = []
    label_list = []
    for file in os.listdir(dir_path):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        label_list.append(int(file[0]))
        image_path_list.append(os.path.join(dir_path, file))
    
    for imagePath in image_path_list:
        image = cv2.imread(imagePath)
        if image is None:
            print ("Error loading: " + imagePath)
        else:
            image_list.append(image)
    
    return image_list,label_list,image_path_list


def load_img(img_path = "images/"):
    """
        load one image
    """
    image = cv2.imread(img_path)
    return image


def write_img(img,path,ok,filterapply):
    x = path.split('/')
    realpath="result";
    for i in range(0,len(x)-2):
        realpath=x[i]+"/"+realpath
    if ok==1 :
        realpath=realpath+"/Org_"+x[-1]
    else:
        realpath=realpath+"/"+filterapply+"_"+x[-1]
        
    scipy.misc.imsave(realpath,img)
