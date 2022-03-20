from PIL import Image
from math import *

original = Image.open("./img_5.jpg")
convertData = original.convert("L").getdata()


def putDataAndSave(datas, path, size):
    convertImage = Image.new("L", size)
    convertImage.putdata(datas)
    convertImage.save(path)


def calculateFilter(mask, data, image, board):
    filterData = []
    for j in range(image.size[0]):
        for i in range(image.size[1]):
            pixel = 0
            for mask_j in range(len(mask)):
                for mask_i in range(len(mask[mask_j])):
                    try:
                        pixel -= data[(j - floor(len(mask) / 2) + mask_j) * image.size[0] + i - floor(
                            len(mask[mask_j]) / 2) + mask_i] * mask[mask_j][mask_i]
                    except IndexError:
                        pixel -= data[j * image.size[0] + i] * mask[mask_j][mask_i]
            if abs(pixel) > board:
                filterData.append(255)
            else:
                filterData.append(0)
    return filterData


lst_mask_point = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
lineFilterData = calculateFilter(lst_mask_point, convertData, original, int(0.7 * max(convertData)))
putDataAndSave(lineFilterData, "images/lab5/image_points.jpg", original.size)


lst_mask_line_horz = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
lst_line_horz_filt = []

lst_mask_move = [[0, -1, 0], [0, 1, 0], [0, 0, 0]]
lst_line_move = []

im = Image.open("./image3.jpg")
px = im.convert("L")
px_1 = px.copy()
px1 = px_1.load()
for i in range(px.size[0]):
    for j in range(px.size[1]):
        pixel = 0
        for mask_i in range(len(lst_mask_line_horz)):
            for mask_j in range(len(lst_mask_line_horz[mask_i])):
                try:
                    pixel -= px1[i - floor(len(lst_mask_line_horz) / 2) + mask_i, j - floor(
                        len(lst_mask_line_horz[mask_i]) / 2) + mask_j] * lst_mask_line_horz[mask_i][mask_j]
                except IndexError:
                    pixel -= px1[i, j] * lst_mask_line_horz[mask_i][mask_j]
        if abs(pixel) > 400:
            px1[i, j] = (255)
        else:
            px1[i, j] = (0)
px_1.save("./image_lines_horz.jpg")

original = Image.open("./image6.jpg")
px = original.convert("L")
px_1 = px.copy()
px1 = px_1.load()

lst_mask_kirsh = [[3, 3, 3], [3, 0, 3], [-5, -5, -5]]
lst_line_horz_filt = []

for i in range(px.size[0]):
    for j in range(px.size[1]):
        pixel = 0
        for mask_i in range(len(lst_mask_kirsh)):
            for mask_j in range(len(lst_mask_kirsh[mask_i])):
                try:
                    pixel -= px1[i - floor(len(lst_mask_kirsh) / 2) + mask_i, j - floor(
                        len(lst_mask_kirsh[mask_i]) / 2) + mask_j] * lst_mask_kirsh[mask_i][mask_j]
                except IndexError:
                    pixel -= px1[i, j] * lst_mask_kirsh[mask_i][mask_j]
        if abs(pixel) > 600:
            px1[i, j] = (255)
        else:
            px1[i, j] = (0)

px_1.save("./image_kirsh.jpg")
