import cv2
import random
import Master_Transform_Code
'''blurs 40 x 40 images '''
#NEED TO UPDATE THIS FUNCTION
#USE CIRCULAR DILATE
#AND ADD SPACE ON THE SIDES SO THAT THE DILATE DOESNT GET CUT OFF
#DONT FORGET TO THRESHOLD IMAGES AT THE END
#Dilate more - Davis
'''input image is assumed to already be cropped and of proper size'''
def addnoise(image):



    circular_Kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

    #High scale factor is to make sure none of the noise is cropped out
    image = Master_Transform_Code.crop_image(image,1.4)
    cv2.imshow("2", image)
    cv2.waitKey(0)
    #Blur is to get gray pixels
    #See what happens if you use rectangular kernel here and circular kernel elsewhere
    #GaussianBlur vs Blur? Blur replaces all the pixels of a kernel with the average value of that kernel
    #This creates grey pixels near the edges of the shape, (Also in the shape, but these will be addressed later)
    blur = cv2.GaussianBlur(image,(5,5),0)
    #(5,5) was used originallzy and it was cv2.GaussianBlur(image,(5,5),0)

    #Creating the noise like this is satisfactory, for now at least
    noise = cv2.imread("Background.png", cv2.IMREAD_COLOR)
    noise = cv2.resize(noise, (int(blur.shape[1]) ,int (blur.shape[0])), interpolation = cv2.INTER_AREA)
    make_random_white(noise)

    #blur = blur*noise, this line makes it so that all black pixels will stay black and only the gray pixels 
    #will be affected, i.e. some of the gray pixels will become black due to the random noise, will be addressed in next
    #section of code

    for i in range(0, noise.shape[0]):
        for j in range(0, noise.shape[1]):
            blur[i,j] = blur[i,j] * noise[i,j]



    #Add the modified blur to the original image, grey + white = white, grey + black = grey, black + white = white
    new = cv2.add(blur,image)
    #new = blur + image <-- original line


    #need to make all greys white
    threshold(new)

    cv2.imshow('before dilation',new)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #if i use scale_factor of 1.1 then resize to 40 x 40 then the noise gets cut off, if i use scale factor of 1.2 then resize to 40 x 40 then the triangle will appear a bit smaller
    cv2.imwrite('before_dilation.png', new)
    rip = cv2.dilate(new,circular_Kernel,iterations = 1)
    
    rez = Master_Transform_Code.crop_image(rip, 1.2)
    rez = cv2.resize(rez, (40,40), interpolation = cv2.INTER_AREA)
    threshold(rez)
    cv2.imwrite('after_dilation.png',rez)
    
    return rez

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
                    image[i,j][k] = a * 255

    return








if __name__ == '__main__':


    imgg = cv2.imread("Equilateral_Triangle.png", cv2.IMREAD_COLOR)
    image = Master_Transform_Code.crop_image(imgg,1.2)
    image = cv2.resize(image,(40,40),interpolation = cv2.INTER_AREA)

    cv2.imshow('original image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image1 = addnoise(image)

    cv2.imshow('after dilation',image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#check if the original imgg is preserved should be big with big borders
    #normal imgg is preserved
    cv2.imwrite("normal_image.png", imgg)

    cv2.imwrite("blurred_image.png", image1)
