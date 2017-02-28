'''Title: Master_Transform_Code.py  
Author: Rojigan Gengatharan and whoever blessed that rotate_image code
NOTES: Only works for images of 525 length and 519 width, these are the global 
constants. Requires the file names in the list shown at the beginning of the code
to be present and requires a "Background.png" file which is a image of 
525 length and 519 width and colour is the same as the background of the images
you are using. For example, A black background would mean Backgroud.png would
have to be the colour black
Also requires processImages.py with the rotate_image function'''



##MAKE WIDE AND FAT SHAPEStt

import numpy as np
import cv2
import processImages
import os 
ROTATION_AMOUNT = 12
LENGTH = 525 
WIDTH = 519


def compress_img(image, compression_amount):
    '''image is simply the opencv image file
    compression_amount is how much you want the file to be compressed, For 
    example, a compression_amount of 2 indicates you want the horizontal size of the 
    new image to be 1/2 of what it was originally (everything else stays the same)'''
    

    dim = (LENGTH//compression_amount, WIDTH)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
    l_img = cv2.imread("Background.png", cv2.IMREAD_COLOR)
    s_img = resized
    
    x_offset= LENGTH // 2 - s_img.shape[1]//2
    y_offset= WIDTH // 2 - s_img.shape[0]//2
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

    return l_img
    
    
    
def rotate_img(image, rot_amount):
    '''image is simply the opencv image file
    rotation_amount is how much you want the file to be rotated, For 
    example, a rotation_amount of 12 means you want to rotate the image 12 
    degrees CCW'''
    new_img = processImages.rotate_image(image, rot_amount)
    return new_img
    
    
    


list_of_file_names = ['Equilateral_Triangle.png', 'Isoceles_Right_Angle_Triangle.png']


for i in range(len(list_of_file_names)):
    
    img = cv2.imread(list_of_file_names[i], cv2.IMREAD_COLOR)
    newpath = list_of_file_names[i][:-4]  
    background = cv2.imread("Background.png", cv2.IMREAD_COLOR)  
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    os.chdir(newpath)
    cv2.imwrite("Background.png", background) 
    # new_imgs = [new_img]
     
    for j in range(1,31):
        new_img = rotate_img(img, j*12)
        # new_imgs.extend(new_img)
        
        for k in range(2, 5):
            
            new_new_img = compress_img(new_img, k)
            a = str(i) + 'th_shape' + str(j*12) + 'rot' + str(k) + 'squish_.png'
            cv2.imwrite(a, new_new_img) 
    

    os.chdir('..')



    
    
    