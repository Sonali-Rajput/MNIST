from tkinter import BaseWidget
import cv2
import numpy as np


def image_BWresize(path):
    '''
    path: image path 
    change image to black and white 
    changing resolution to 28 x 28
    return reshaped numpy array of dimension 28x28x1
    '''
    #image = cv2.imread(path)
    #bwimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #bwimage_resize = cv2.resize(bwimage,(28,28))
    # if cv2.countNonZero(bwimage_resize) > ((28*28)//2):
    # Detect black line
    # bwimage_resize = cv2.bitwise_not(bwimage_resize) # OR #invert = 255 - image
    # else:

    # Detect white line

    #newImage = bwimage_resize.reshape(-1,28,28,1)

    #cv2.imshow("starting", bwimage_resize)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # return newImage

    image = cv2.imread(path)
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("a")
    ret, thresh = cv2.threshold(grey, 75, 255,
                                cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)
    print("b", contours)
    preprocessed_digits = []
    resized_digit = None
    print("c")
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        print("d")
        cv2.rectangle(image, (x, y), (x+w, y+h),
                      color=(0, 255, 0), thickness=2)

        digit = thresh[y:y+h, x:x+w]

        resized_digit = cv2.resize(digit, (18, 18))
        print("okay", resized_digit)

        padded_digit = np.pad(resized_digit, ((5, 5), (5, 5)),
                              "constant", constant_values=0)

        preprocessed_digits.append(padded_digit)
    print("e")
    inp = np.array(preprocessed_digits)
    inp.reshape(-1, 28, 28, 1)

    return inp
