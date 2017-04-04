import cv2
def addnoise(img):
    blur = cv2.GaussianBlur(img,(5,5),0)
    noise = cv2.imread("Background.png")







if __name__ == '__main__':
    image = cv2.imread("Equilateral_Triangle.png", cv2.IMREAD_COLOR)
    image = addnoise(image)
