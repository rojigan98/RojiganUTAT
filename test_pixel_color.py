import cv2
WIDTH = 525 
HEIGHT = 519
SCALE_FACTOR = 1.1


  
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



image = cv2.imread("Equilateral_Triangle.png", cv2.IMREAD_COLOR)


print(image[HEIGHT - 1,  WIDTH - 1]) 

l_img = cv2.imread("Background.png", cv2.IMREAD_COLOR)
s_img = image

parameters = (find_limiting_p(image))


bg = cv2.imread("Background.png", cv2.IMREAD_COLOR)

a1 = parameters[0][1][0]
a2 = parameters[0][1][1]

b1 = parameters[0][0][0]
b2 = parameters[0][0][1]

dimm = max(parameters[1][0],parameters[1][1])



new_bg = cv2.resize(bg, (int((int(b2) - int(b1))),int((int(a2) - int(a1)))), interpolation = cv2.INTER_LINEAR)


final = cv2.resize(bg, (int(dimm * SCALE_FACTOR), int(dimm * SCALE_FACTOR)), interpolation = cv2.INTER_LINEAR) 



new_bg = image[int(a1):int(a2), int(b1):int(b2)]   #yoffset:yoffset + zz, xoffset: xoffset + zzz


new_new_bg = cv2.resize(bg, (int((int(b2) - int(b1)) * SCALE_FACTOR),int((int(a2) - int(a1)) * SCALE_FACTOR)), interpolation = cv2.INTER_LINEAR)

## horizontal, vertical

hdm = int((int(b2) - int(b1)) * SCALE_FACTOR)
vdm = int((int(a2) - int(a1)) * SCALE_FACTOR)

hoff = (hdm - (int(b2) - int(b1))) // 2
voff = (vdm - (int(a2) - int(a1)))// 2

cv2.imshow("original", image)
cv2.waitKey(0)
cv2.imshow("new", new_bg)
cv2.waitKey(0) 
# [0 0 0] is black
# [255 255 255] is white 

cv2.imshow("new_new", new_new_bg)
cv2.waitKey(0)

new_new_bg[voff:voff + int(a2) - int(a1), hoff:hoff + int(b2) - int(b1)] = new_bg 

cv2.imshow("new_new", new_new_bg)
cv2.waitKey(0)



print(parameters)

print("") 




            
                
