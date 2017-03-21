import cv2
 
# load the image and show it
# image = cv2.imread("Equilateral_Triangle.png")
# 
# dim = (100, 400)
# 
# resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
# cv2.imshow("resized", resized)
# cv2.waitKey(0)
# 


bigimage = cv2.imread("red_square.png") 
lilimage = cv2.imread("blue_square.png")

s_img = cv2.imread("Equilateral_Triangle.png")
l_img = cv2.imread("Background.png")


x_offset= 0
y_offset= 0
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
cv2.imshow("ON TOP", l_img)
cv2.waitKey(0)