import os
import cv2
import math
import numpy as np
import thread
import time

def rotate_image(image, angle):
    #calculates the length of the diagonal (PYTHAGORAS)
    diagonal = int(math.sqrt(pow(image.shape[0], 2) + pow(image.shape[1], 2)))
    #calculates the difference between the length of the diagonal and the horizontal (offset_x) or the vertical (offset_y)
    offset_x = (diagonal - image.shape[0])/2
    offset_y = (diagonal - image.shape[1])/2
    
    #dtype = unsigned integer (8-bit?) 
    dst_image = np.zeros((diagonal, diagonal, 3), dtype='uint8')
    
    #not really center? or am I just tripping 
    image_center = (diagonal/2, diagonal/2)

    R = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    dst_image[offset_x:(offset_x + image.shape[0]), \
            offset_y:(offset_y + image.shape[1]), \
            :] = image
    dst_image = cv2.warpAffine(dst_image, R, (diagonal, diagonal), flags=cv2.INTER_LINEAR)

    # Calculate the rotated bounding rect
    x0 = offset_x
    x1 = offset_x + image.shape[0]
    x2 = offset_x
    x3 = offset_x + image.shape[0]

    y0 = offset_y
    y1 = offset_y
    y2 = offset_y + image.shape[1]
    y3 = offset_y + image.shape[1]

    corners = np.zeros((3,4))
    corners[0,0] = x0
    corners[0,1] = x1
    corners[0,2] = x2
    corners[0,3] = x3
    corners[1,0] = y0
    corners[1,1] = y1
    corners[1,2] = y2
    corners[1,3] = y3
    corners[2:] = 1
    
    c = np.dot(R, corners)
    
    x = int(c[0,0])
    y = int(c[1,0])
    left = x
    right = x
    up = y
    down = y

    for i in range(4):
        x = int(c[0,i])
        y = int(c[1,i])
        if (x < left): left = x
        if (x > right): right = x
        if (y < up): up = y
        if (y > down): down = y
    h = down - up
    w = right - left

    cropped = np.zeros((w, h, 3), dtype='uint8')
    #rip his code, put an if here to account for the error
    if (up >= 0 and left >= 0):
        cropped[:, :, :] = dst_image[left:(left+w), up:(up+h), :]
    elif (up < 0 and left >= 0):
        cropped[:,:,:] = dst_image[left:(left + w), 0:h, :]
    elif (left < 0 and up >= 0):
        cropped[:,:,:] = dst_image[0:w, up:(up + h), :]
    else:
        cropped[:,:,:] = dst_image[0:w,0:h,:]
    return cropped
    
def getRotationsPlusMinus(angle, image):
    rotated1 = rotate_image(image, angle - 15)
    rotated1 = cv2.resize(rotated1, (40, 40), interpolation = cv2.INTER_CUBIC)
    
    rotated2 = rotate_image(image, angle)
    rotated2 = cv2.resize(rotated2, (40, 40), interpolation = cv2.INTER_CUBIC)
    
    rotated3 = rotate_image(image, angle + 15)
    rotated3 = cv2.resize(rotated3, (40, 40), interpolation = cv2.INTER_CUBIC)
    
    return (rotated1, rotated2, rotated3)

# Script parameters
directory = "/homes/w/wusihan1/UAV/FontDatabase/English/Fnt"
outputDirectory = "/homes/w/wusihan1/UAV/processedFontDB/"

# Stores the existing classes
D = {}

# Numbers
D["001"] = "0"
D["002"] = "1"
D["003"] = "2"
D["004"] = "3"
D["005"] = "4"
D["006"] = "5"
D["007"] = "6"
D["008"] = "7"
D["009"] = "8"
D["010"] = "9"

# Capital Case
D["011"] = "A"
D["012"] = "B"
D["013"] = "C"
D["014"] = "D"
D["015"] = "E"
D["016"] = "F"
D["017"] = "G"
D["018"] = "H"
D["019"] = "I"
D["020"] = "J"
D["021"] = "K"
D["022"] = "L"
D["023"] = "M"
D["024"] = "N"
D["025"] = "O"
D["026"] = "P"
D["027"] = "Q"
D["028"] = "R"
D["029"] = "S"
D["030"] = "T"
D["031"] = "U"
D["032"] = "V"
D["033"] = "W"
D["034"] = "X"
D["035"] = "Y"
D["036"] = "Z"

# Inverted mapping
charToIndex = {v : (int(k)-1) for k, v in D.iteritems()}

imagePaths = []
for x in os.walk(directory):
    # Last 3 characters of the folder name corresponds to the number
    folderName = x[0].split('/')[-1]
    ID = folderName[-3:]
    if ID in D:
        paths = [x[0] + "/" + name for name in x[2]]
        imagePaths.extend(paths)
    
# Do outputs
# Name is formatted like so: <classIndex>_<character>_<rotationIndex>_<datasetIndex>.png
# Class index is the most relevant and is for training the neural net
rotationInterval = 10
i = 0
for imagePath in imagePaths:
    # Get image name
    name = imagePath.split("/")[-1]
    ID = name[3:6]
    
    # Read and resize immediately
    image = cv2.imread(imagePath)
    
    # Invert colours
    image = 255 - image
    
    character = D[ID]
    
    if i % 1200 == 0:
        print "outputting " + character + " " + str(i)
    
    # 0 degrees
    first, second, third = getRotationsPlusMinus(0, image)
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+0) + "_" + character + "_" + str(0) + "_" + str(i) + ".png", first)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+0) + "_" + character + "_" + str(0) + "_" + str(i) + ".png", second)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+0) + "_" + character + "_" + str(0) + "_" + str(i) + ".png", third)
    i = i + 1
    
    # 90 degrees
    first, second, third = getRotationsPlusMinus(90, image)
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+1) + "_" + character + "_" + str(1) + "_" + str(i) + ".png", first)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+1) + "_" + character + "_" + str(1) + "_" + str(i) + ".png", second)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+1) + "_" + character + "_" + str(1) + "_" + str(i) + ".png", third)
    i = i + 1
    
    # 180 degrees
    first, second, third = getRotationsPlusMinus(180, image)
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+2) + "_" + character + "_" + str(2) + "_" + str(i) + ".png", first)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+2) + "_" + character + "_" + str(2) + "_" + str(i) + ".png", second)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+2) + "_" + character + "_" + str(2) + "_" + str(i) + ".png", third)
    i = i + 1
    
    # 270 degrees
    first, second, third = getRotationsPlusMinus(90, image)
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+3) + "_" + character + "_" + str(3) + "_" + str(i) + ".png", first)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+3) + "_" + character + "_" + str(3) + "_" + str(i) + ".png", second)
    i = i + 1
    cv2.imwrite(outputDirectory + str(charToIndex[character]*4+3) + "_" + character + "_" + str(3) + "_" + str(i) + ".png", third)
    i = i + 1

