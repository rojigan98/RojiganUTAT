import numpy as np
import cv2
import processImages
import os 
ROTATION_AMOUNT = 12


#Load image

list_of_file_names = ['Equilateral_Triangle.png', 'Isoceles_Right_Angle_Triangle.png']



for i in range(len(list_of_file_names)):
    
    img = cv2.imread(list_of_file_names[i], cv2.IMREAD_COLOR)
    
    new_img = processImages.rotate_image(img, 12)
        
        
    newpath = list_of_file_names[i][:-4]    
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    os.chdir(newpath)
    
    new_imgs = [new_img]
    
    for j in range(1,31):
        new_img = processImages.rotate_image(img, j*12)
        new_imgs.extend(new_img)
        a = str(i) + '_' + str(j*12) + '_.png'
        cv2.imwrite(a, new_img) 
    

    os.chdir('..')







# img = cv2.imread('Equilateral_Triangle.png', cv2.IMREAD_COLOR)
# 
# new_img = processImages.rotate_image(img, 12)
#     
# 
# 
# #do it for all base images, not one at a time, so far the 0 in the line a = ....., indicates that it only works with equilateral triangle, so it puts them all into one folder search up how to modify folders and stuff in python
# 
# 
# new_imgs = [new_img]
# 
# for i in range(1,31):
#     new_img = processImages.rotate_image(img, i*12)
#     new_imgs.extend(new_img)
#     a = '0_' + str(i*12) + '_.png'
#     cv2.imwrite(a, new_img) 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#     