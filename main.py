from PIL import Image
import numpy as np
from copy import deepcopy
import random

def carveSeam(start, pixels):
    x = start
    lpixels = pixels.tolist()
    newPixels = []

    for row in lpixels:
        mid = row[x]
        left = row[x - 1]
        right = row[x + 1]

        lDiff = findDiff(mid, left)
        rDiff = findDiff(mid, right)

        if lDiff > rDiff:
            newRow = deepcopy(row)
            del newRow[x]
            x = x - 1
        if lDiff < rDiff:
            newRow = deepcopy(row)
            del newRow[x]
            x = x + 1
        else:
            num = random.randint(0, 1)
            if num == 0:
                newRow = deepcopy(row)
                del newRow[x]
                x = x - 1
            if num == 1:
                newRow = deepcopy(row)
                del newRow[x]
                x = x + 1
 
        newPixels += [newRow]

    pixArr = np.array(newPixels)
    return pixArr

def showSeam(start, pixels):
    x = start
    lpixels = pixels.tolist()
    newPixels = []

    for row in lpixels:
        mid = row[x]
        left = row[x - 1]
        right = row[x + 1]

        lDiff = findDiff(mid, left)
        rDiff = findDiff(mid, right)

        if lDiff > rDiff:
            newRow = deepcopy(row)
            newRow[x] = [255, 0, 0]
            x = x - 1
        if lDiff < rDiff:
            newRow = deepcopy(row)
            newRow[x] = [255, 0, 0]
            x = x + 1
        else:
            num = random.randint(0, 1)
            if num == 0:
                newRow = deepcopy(row)
                newRow[x] = [255, 0, 0]
                x = x - 1
            if num == 1:
                newRow = deepcopy(row)
                newRow[x] = [255, 0, 0]
                x = x + 1
 
        newPixels += [newRow]

    pixArr = np.array(newPixels)
    return pixArr

def findDiff(p1, p2):
    diff = 0

    for value in range(len(p1)):
        diff += abs(p1[value] - p2[value])

    return diff

def main():
    # open image and define two different RGB arrays
    image = Image.open('img/flowers.jpg')
    pix = np.asarray(image)
    spix = np.asarray(image)

    
    for i in range(int(len(pix[0]) / 12)):
        pix = showSeam((i * 10) , pix)
        spix = carveSeam((i * 10) , spix)

    image2 = Image.fromarray((pix).astype(np.uint8))
    image3 = Image.fromarray((spix).astype(np.uint8))
    image2.show()
    image3.show()

if __name__ == "__main__":
    main()