import numpy as np
import cv2
import processImages
import os 

list_of_file_names = ['Equilateral_Triangle.png', 'Isoceles_Right_Angle_Triangle.png']



for i in range(len(list_of_file_names)):
    
    img = cv2.imread(list_of_file_names[i], cv2.IMREAD_COLOR)
    
    # plt.subplot(121),plt.imshow(img),plt.title('Input')
    # plt.subplot(122),plt.imshow(dst),plt.title('Output')
    # plt.show()
    #     
                
    newpath = list_of_file_names[i][:-4]    
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    os.chdir(newpath)
    a = 'm' + list_of_file_names[i] 
    cv2.imwrite(a, new_img) 
    

    os.chdir('..')

