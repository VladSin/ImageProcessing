from PIL import Image, ImageDraw

import Lab1

operation = int(input('operation:'))
original = Image.open("images/Screenshot_1.png")
draw = ImageDraw.Draw(original)
width = original.size[0]
height = original.size[1]
pix = original.load()


def vis():
    return 1


def ecv():
    return 2


def cnt():
    return 3


def bit():
    return 4


if (operation == 1):
    Lab1.averaging(width, height)
    const = int(input('const:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]

if (operation == 2):
    Lab1.averaging(width, height)
    const = float(input('const:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]

if (operation == 3):
    Lab1.averaging(width, height)
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]

if (operation == 4):
    Lab1.averaging(width, height)
    const = float(input('const:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
