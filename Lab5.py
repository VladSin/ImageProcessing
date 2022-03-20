from PIL import Image
from math import *

original = Image.open("images/lab5/image6.jpg")
originalImage = original.convert("L")
convertData = original.convert("L").getdata()


def putDataAndSave(datas, path, size):
    convertImage = Image.new("L", size)
    convertImage.putdata(datas)
    convertImage.save(path)


def calculateFilter1(mask, data, image, board):
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


def calculateFilter2(mask, data, board, path):
    copyData = data.copy()
    filterData = copyData.load()
    for i in range(data.size[0]):
        for j in range(data.size[1]):
            pixel = 0
            for mask_i in range(len(mask)):
                for mask_j in range(len(mask[mask_i])):
                    try:
                        pixel -= filterData[i - floor(len(mask) / 2) + mask_i, j - floor(
                            len(mask[mask_i]) / 2) + mask_j] * mask[mask_i][mask_j]
                    except IndexError:
                        pixel -= filterData[i, j] * mask[mask_i][mask_j]
            if abs(pixel) > board:
                filterData[i, j] = 255
            else:
                filterData[i, j] = 0
    return copyData.save(path)

# Для обнаружения точек
maskPoint = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
lineFilterData = calculateFilter1(maskPoint, convertData, original, int(0.7 * max(convertData)))
putDataAndSave(lineFilterData, "images/lab5/ResultPointFilterImage.jpg", original.size)

# Для обнаружения линий
maskLineHorz = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
calculateFilter2(maskLineHorz, originalImage, 400, "images/lab5/ResultLineFilterImage.jpg")

# Для обнаружения краев
maskKirsh = [[3, 3, 3], [3, 0, 3], [-5, -5, -5]]
calculateFilter2(maskKirsh, originalImage, 600, "images/lab5/imageKirshFilter.jpg")

