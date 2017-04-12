import cv2
import random
import Master_Transform_Code
'''blurs 40 x 40 images '''
#NEED TO UPDATE THIS FUNCTION
#USE CIRCULAR DILATE
#AND ADD SPACE ON THE SIDES SO THAT THE DILATE DOESNT GET CUT OFF 
'''input image is assumed to already be cropped and of proper size'''
def addnoise(image):

    #img_m = Master_Transform_Code.crop_image(img)
    #img_m = cv2.resize(img_m,(42,42),0)
    #Blur is to get gray pixels
    blur = cv2.GaussianBlur(image,(5,5),0)
    
    #cv2.resize(img, (42,42), interpolation = cv2.INTER_AREA)
    #blur = cv2.resize(blur, (img_m.shape[1],img_m.shape[0]), interpolation = cv2.INTER_AREA)
    
    noise = cv2.imread("Background.png", cv2.IMREAD_COLOR)
    noise = cv2.resize(noise, (blur.shape[1],blur.shape[0]), interpolation = cv2.INTER_AREA)
    
    #noise = Master_Transform_Code.crop_image(noise)
    
    make_random_white(noise)
    
    for i in range(0, noise.shape[0]):
     for j in range(0, noise.shape[1]):
        blur[i,j] = blur[i,j] * noise[i,j]
    
    
    #NEED TO DILATE HERE
    #new = blur + img_m
    
    new = blur + image
    
    
    
    threshold(new)
    cv2.imshow('before dilation',new)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    new = Master_Transform_Code.crop_image(new)
    cv2.imwrite('before_dilation.png', new)
    new = cv2.dilate(new,(3,3),iterations = 1)
    cv2.imwrite('after_dilation.png',new)
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
                #image[i,j] = random.randint(0,1)
                a = random.randint(0,1)
                for k in range(3):
                    image[i,j][k] = a
                
    return





            
                
        
if __name__ == '__main__':
    
    
    image = cv2.imread("Equilateral_Triangle.png", cv2.IMREAD_COLOR)
    image = Master_Transform_Code.crop_image(image)
    image = cv2.resize(image,(40,40),0)
    
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    image1 = addnoise(image)
    
    cv2.imshow('after dilation',image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()