from PIL import Image
import numpy as np

def carveSeam(start, pixels):
    x = start
    newPixels = np.empty((1, len(pixels[0]) - 1, 3))

    for row in pixels:
        row = np.array(row)
        mid = row[x]
        left = row[x - 1]
        right = row[x + 1]

        lDiff = findDiff(mid, left)
        rDiff = findDiff(mid, right)

        if lDiff > rDiff:
            newRow = np.array([np.delete(row, x, 0)])
            x = x - 1
        if lDiff < rDiff:
            newRow = np.array([np.delete(row, x, 0)])
            x = x + 1

        newPixels = np.concatenate((tuple(newPixels), tuple(newRow)))
    
    print(newPixels.shape)
    return newPixels

def findDiff(p1, p2):
    diff = 0

    for value in range(len(p1)):
        diff += abs(p1[value] - p2[value])

    return diff

def main():
    image = Image.open('img/flowers.jpg')
    pix = np.asarray(image)

    carvedPix = carveSeam(200, pix)
    image2 = Image.fromarray((carvedPix * 255).astype(np.uint8))
    image2.show()

if __name__ == "__main__":
    main()