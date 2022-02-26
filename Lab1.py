import math

from PIL import Image, ImageDraw

operation = int(input('operation:'))
original = Image.open("images/lab1/Screenshot_3.png")
draw = ImageDraw.Draw(original)
width = original.size[0]
height = original.size[1]
pix = original.load()


def averaging(imgWidth, imgHeight):
    for i in range(imgWidth):
        for j in range(imgHeight):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            draw.point((i, j), (S, S, S))


def summ(param, constant):
    result = param + constant
    if result > 255:
        return 255
    if result < 0:
        return 0
    return result


def mult(param, constant):
    result = param * constant
    if result > 255:
        return 255
    if result < 0:
        return 0
    return result


def log(param, maxValue):
    result = math.log(param / maxValue + 1) * 255
    if result > 255:
        return 255
    if result < 0:
        return 0
    return result


def pow(param, maxValue, g):
    result = math.pow(param / maxValue, g) * 255
    if result > 255:
        return 255
    if result < 0:
        return 0
    return result


def maxV(pix):
    maxValue = - 100
    for i in range(width):
        for j in range(height):
            if maxValue < pix[i, j][0]:
                maxValue = pix[i, j][0]
    return maxValue

if (operation == 1):
    averaging(width, height)
    const = int(input('const:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (int(summ(a, const)),
                                int(summ(b, const)),
                                int(summ(c, const))))

if (operation == 2):
    averaging(width, height)
    const = float(input('const:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (int(mult(a, const)),
                                int(mult(b, const)),
                                int(mult(c, const))))

if (operation == 3):
    averaging(width, height)
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))

if (operation == 4):
    averaging(width, height)
    maxValue = maxV(pix)
    const = float(input('const:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (int(log(a, const)),
                                int(log(b, const)),
                                int(log(c, const))))

if (operation == 5):
    averaging(width, height)
    maxValue = maxV(pix)
    const = float(input('const:'))
    gamma = float(input('gamma:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (int(pow(a, maxValue, gamma)),
                                int(pow(b, maxValue, gamma)),
                                int(pow(c, maxValue, gamma))))

original.save("images/lab1/Result.png")
del draw
