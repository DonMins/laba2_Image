import  cv2
import numpy as np
import matplotlib.pyplot as plt


def threshold_processing(img, threshold):
    p = img.shape
    width = p[1]
    height = p[0]

    for i in range(height):
        for j in range(width):
            if (img[i, j] > threshold):
                img[i, j] = 255
            else:
                img[i, j] = 0

    return img


def linear_contrast(img,minY,maxY):
    p = img.shape
    width = p[1]
    height = p[0]
    vals = img.flatten()
    minX = min(vals)
    maxX = max(vals)
    print("исхо", minX)
    print("исх макс", maxX)

    for i in range(height):
        for j in range(width):
            img[i, j] = ((img[i, j] - minX) / (maxX - minX)) * (maxY - minY) + minY

    return img

def image_preparation(img, brightness_range):
    p = img.shape
    width = p[1]
    height = p[0]
    for i in range(height):
        for j in range(width):
            if ((img[i, j] > brightness_range[0]) and (img[i, j] <= brightness_range[1])):
                img[i, j] = 255
            else:
                img[i, j] = 0
    return img



if __name__ == '__main__':

    img = cv2.imread("rab2.jpg",0)
    img2 = cv2.imread("girl.jpg",0)
    cv2.imshow('Input image',img)

    vals = img.flatten()
    plt.hist(vals, bins = range(256))
    plt.show()

    cv2.imshow('Threshold processing', threshold_processing(img,195))

    img = cv2.imread("rab2.jpg",0)

    cv2.imshow('Image preparation', image_preparation(img, [195,255]))

    # cv2.imshow('linear_contrast', linear_contrast(img2,0,255))
    # img3 = linear_contrast(img2, 0, 255)
    # vals = img3.flatten()
    # plt.hist(vals, bins = range(256))
    # plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

