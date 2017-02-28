import cv2
LENGTH = 525 
WIDTH = 519
 
image = cv2.imread("Equilateral_Triangle.png")

dim = (LENGTH//2, WIDTH)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


cv2.imshow("original", image)
cv2.waitKey(0)



# s_img = cv2.imread("blue_square.png")
l_img = cv2.imread("Background.png")
s_img = resized

print(s_img.shape)
x_offset= LENGTH // 2 - s_img.shape[1]//2
y_offset= WIDTH // 2 - s_img.shape[0]//2
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
cv2.imshow("resize", l_img)
cv2.waitKey(0)


