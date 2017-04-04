'''Title: Master_Transform_Code.py  
Author: Rojigan Gengatharan and the writer of the processImages.py code
NOTES: Only works for images of 525 length and 519 width, these are the global 
constants. Requires the file names in the list shown at the beginning of the code
to be present and requires a "Background.png" file which is a image of 
525 width and 519 height and colour is the same as the background of the images
you are using. For example, A black background would mean Backgroud.png would
have to be the colour black
Also requires processImages.py with the rotate_image function'''



##MAKE WIDE SHAPES

import numpy as np
import cv2
import processImages
import os 
ROTATION_AMOUNT = 12
#LENGTH = 525 
#WIDTH = 519
WIDTH = 525 
HEIGHT = 519
SCALE_FACTOR = 1.1
DIMENSION = 40
        
                        
def compress_img(image, compression_amount):
    '''image is simply the opencv image file
    compression_amount is how much you want the file to be compressed, For 
    example, a compression_amount of 2 indicates you want the horizontal size of the 
    new image to be 1/2 of what it was originally (everything else stays the same)'''
    

    dim = (WIDTH//compression_amount, HEIGHT)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    
    l_img = cv2.imread("Background.png", cv2.IMREAD_COLOR)
    s_img = resized
    
    x_offset= WIDTH// 2 - s_img.shape[1]//2
    y_offset= HEIGHT // 2 - s_img.shape[0]//2
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
    image = crop_image(l_img)
    
    res = cv2.resize(image, (WIDTH, HEIGHT), interpolation = cv2.INTER_LINEAR) 
    return res
    
    
    
    
def crop_image(image):
    '''Crops image to a constant scale factor, i.e the shape will take up 1/scale_factor X 100% of the final image'''
    l_img = cv2.imread("Background.png", cv2.IMREAD_COLOR)
    s_img = image
    
    parameters = (find_limiting_p(image))
    
    
    bg = cv2.imread("Background.png", cv2.IMREAD_COLOR)
    
    a1 = parameters[0][1][0]
    a2 = parameters[0][1][1]
    
    b1 = parameters[0][0][0]
    b2 = parameters[0][0][1]
    
    dimm = max(parameters[1][0],parameters[1][1])
    
    
    
    new_bg = cv2.resize(bg, (int((int(b2) - int(b1))),int((int(a2) - int(a1)))), interpolation = cv2.INTER_AREA)
    
    final_dim = int(dimm * SCALE_FACTOR)
    
    final = cv2.resize(bg, (final_dim, final_dim), interpolation = cv2.INTER_LINEAR) 
    
    
    new_bg = image[int(a1):int(a2), int(b1):int(b2)]   #yoffset:yoffset + zz, xoffset: xoffset + zzz
    
    
    new_new_bg = cv2.resize(bg, (final_dim,final_dim), interpolation = cv2.INTER_LINEAR)

    
    ## horizontal, vertical

    
    hoff = (final_dim - (int(b2) - int(b1))) // 2
    voff = (final_dim - (int(a2) - int(a1)))// 2
    new_new_bg[voff:voff + int(a2) - int(a1), hoff:hoff + int(b2) - int(b1)] = new_bg 
    return new_new_bg 
    
def find_limiting_p(image):
    minC = WIDTH - 1
    minR = HEIGHT - 1
    maxC = 0
    maxR = 0
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if (image[i,j])[1] == 0:
                continue
            if i < minR:
                minR = i
            if j < minC:
                minC = j
            if j > maxC:
                maxC = j
            if i > maxR:
                maxR = i
                
    return ((minC, maxC), (minR, maxR)), ((maxC - minC),(maxR -  minR)) 
    
    



def rotate_img(image, rot_amount):
    '''image is simply the opencv image file
    rotation_amount is how much you want the file to be rotated, For 
    example, a rotation_amount of 12 means you want to rotate the image 12 
    degrees CCW'''
    new_img = processImages.rotate_image(image, rot_amount)
    return new_img
    
    
    
if __name__ == '__main__':
    
            
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
            
            for k in range(1, 5):
                
                new_new_img = compress_img(new_img, k)
                new_new_img = cv2.resize(new_new_img, (DIMENSION,DIMENSION), interpolation = cv2.INTER_AREA)
    
                a = str(i) + 'th_shape' + str(j*12) + 'rot' + str(k) + 'squish_.png'
                cv2.imwrite(a, new_new_img) 
        
    
        os.chdir('..')
    
    
    
        
        
        