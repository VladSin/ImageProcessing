from math import *
from PIL import Image

original = Image.open("images/lab4/house.png")
convertData = original.convert("L").getdata()


def putDataAndSave(datas, path, size):
    convertImage = Image.new("L", size)
    convertImage.putdata(datas)
    convertImage.save(path)


def configurationCoefficient(matrix):
    coefficient = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            coefficient += matrix[i][j]
    return coefficient


def calculateFilter(mask, coefficient, data, image, isLaplasian):
    filterData = []
    for j in range(image.size[1]):
        for i in range(image.size[0]):

            pixel = 0
            if isLaplasian:
                pixel = data[j * image.size[1] + i]

            for mask_j in range(len(mask)):
                for mask_i in range(len(mask[mask_j])):
                    if not isLaplasian:
                        try:
                            pixel += data[(j - floor(len(mask) / 2) + mask_j) * image.size[1] + i - floor(
                                len(mask[mask_j]) / 2) + mask_i] * mask[mask_j][mask_i]
                        except IndexError:
                            pixel += data[j * image.size[1] + i] * mask[mask_j][mask_i]
                    else:
                        try:
                            pixel -= data[(j - floor(len(mask) / 2) + mask_j) * image.size[1] + i - floor(
                                len(mask[mask_j]) / 2) + mask_i] * mask[mask_j][mask_i]
                        except IndexError:
                            pixel -= data[j * image.size[1] + i] * mask[mask_j][mask_i]

            if not isLaplasian:
                pixel /= coefficient
            filterData.append(int(pixel))
    return filterData


maskData = [[1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]

maskGaussData = [[1, 4, 1],
                 [4, 12, 4],
                 [1, 4, 1]]

maskLaplasData = [[0, 0, -1, 0, 0],
                  [0, -1, -2, -1, 0],
                  [-1, -2, 16, -2, -1],
                  [0, -1, -2, -1, 0],
                  [0, 0, -1, 0, 0]]

weightMedianData = [[0, 2, 0],
                    [1, 3, 1],
                    [0, 2, 0]]

# Line Filter
maskCoefficient = configurationCoefficient(maskData)
lineFilterData = calculateFilter(maskData, maskCoefficient, convertData, original, False)
putDataAndSave(lineFilterData, "images/lab4/ResultLineFilterImage.jpg", original.size)

# Gauss Filter
gaussCoefficient = configurationCoefficient(maskGaussData)
gaussFilterData = calculateFilter(maskGaussData, gaussCoefficient, convertData, original, False)
putDataAndSave(gaussFilterData, "images/lab4/ResultGaussFilterImage.jpg", original.size)

# Laplasian Filter
laplasCoefficient = configurationCoefficient(maskLaplasData)
laplasFilterData = calculateFilter(maskLaplasData, laplasCoefficient, convertData, original, True)
putDataAndSave(laplasFilterData, "images/lab4/ResultLaplasFilterImage.jpg", original.size)

# Non-sharp masking
maskNonSharp = []
for i in range(original.size[1] * original.size[0]):
    maskNonSharp.append(convertData[i] - lineFilterData[i])
nonSharpFilter = []
for i in range(original.size[1] * original.size[0]):
    nonSharpFilter.append(convertData[i] + int(maskNonSharp[i]))
putDataAndSave(nonSharpFilter, "images/lab4/ResultNonSharpMaskingImage.jpg", original.size)

# Weight Median Filter
medianCoefficient = configurationCoefficient(weightMedianData)
medianWeightFilterData = calculateFilter(weightMedianData, medianCoefficient, convertData, original, False)
putDataAndSave(medianWeightFilterData, "images/lab4/ResultWeightMedianFilterImage.jpg", original.size)

# Other Median Filter
windowX = 3
windowY = 3
medianFilterData = []
medianMinFilterData = []
medianMaxFilterData = []

for j in range(original.size[1]):
    for i in range(original.size[0]):
        temp = []
        for mask_j in range(windowY):
            for mask_i in range(windowX):
                try:
                    temp.append(convertData[(j - floor(windowY / 2) + mask_j) * original.size[1] + i - floor(
                        windowX / 2) + mask_i])
                except IndexError:
                    temp.append(convertData[(j) * original.size[1] + i])
        temp.sort()
        medianFilterData.append(temp[floor(windowX * windowY / 2)])
        medianMaxFilterData.append(temp[-1])
        medianMinFilterData.append(temp[0])

putDataAndSave(medianFilterData, "images/lab4/ResultMedianFilterImage.jpg", original.size)
putDataAndSave(medianMaxFilterData, "images/lab4/ResultMedianMaxFilterImage.jpg", original.size)
putDataAndSave(medianMinFilterData, "images/lab4/ResultMedianMinFilterImage.jpg", original.size)
