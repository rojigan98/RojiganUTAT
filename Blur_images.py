import cv2
import random
import Master_Transform_Code
'''blurs 42 x 42 images '''
#NEED TO UPDATE THIS FUNCTION
def addnoise(img):
    img_m = Master_Transform_Code.crop_image(img)
    img_m = cv2.resize(img_m,(42,42),0)
    blur = cv2.GaussianBlur(img_m,(5,5),0)
    
    #cv2.resize(img, (42,42), interpolation = cv2.INTER_AREA)
    blur = cv2.resize(blur, (img_m.shape[1],img_m.shape[0]), interpolation = cv2.INTER_AREA)
    
    noise = cv2.imread("Background.png")
    noise = cv2.resize(noise, (blur.shape[1],blur.shape[0]), interpolation = cv2.INTER_AREA)
    
    make_random_white(noise)
    
    for i in range(0, noise.shape[0]):
     for j in range(0, noise.shape[1]):
        blur[i,j] = blur[i,j] * noise[i,j]
    
    new = blur + img_m
    
    
    
    
    threshold(new)
    cv2.imwrite('blurred.png',new)
    return new
    
''' Turns greys into blacks '''
def threshold(image):
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if (image[i,j][0] != 0 and image[i,j][0] != 255):
                for x in range(3): 
                    (image[i,j])[x] = 255
    return
    
'''puts random white spots on the background.png'''
def make_random_white(image):
    
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):            
            x = random.randint(0, 1)
            if (x == 0):
                image[i,j] = random.randint(0,1)
                
                
    return





            
                
        
if __name__ == '__main__':
    
    
    image = cv2.imread("Equilateral_Triangle.png", cv2.IMREAD_COLOR)
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    image = addnoise(image)
    cv2.imshow('new_image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()