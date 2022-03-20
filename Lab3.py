from math import *
import matplotlib.pyplot as plt
from PIL import Image

original = Image.open("images/lab3/finger2.png")
widthImage = original.size[0]
heightImage = original.size[1]
convertData = original.convert("L").getdata()

listX = list(range(256))
listY = [0] * 256

def visualization(data, valuesX, valuesY):
    for i in data:
        valuesY[i] += 1
    plt.stem(valuesX, valuesY)
    plt.show()


def putDataAndSave(datas, path, size):
    convertImage = Image.new("L", size)
    convertImage.putdata(datas)
    convertImage.save(path)


def calculate(data, value):
    calculateData = []
    for i in data:
        if i < value:
            calculateData.append(0)
        else:
            calculateData.append(255)
    return calculateData


def histogramFunction(data, border, eps):
    while True:
        count1 = 0
        count2 = 0
        m1 = 0
        m2 = 0

        for j in data:
            if j >= border:
                m1 += j
                count1 += 1
            else:
                m2 += j
                count2 += 1

        newBorder = int(1 / 2 * (m1 / count1 + m2 / count2))
        if abs(newBorder - border) > eps:
            border = newBorder
        else:
            break
    print("Border Hist = ", border)
    return border


def gradientFunction(data, width, height):
    sumGrad = 0
    sum = 0

    for j in range(height):
        for i in range(width):
            Gm = 0
            Gn = 0
            if i + 1 == width:
                Gm = data[j * height + i] - data[j * height + i - 1]
            elif i - 1 < 0:
                Gm = data[j * height + i + 1] - data[j * height + i]
            else:
                Gm = data[j * height + i + 1] - data[j * height + i - 1]

            if j + 1 == height:
                Gn = data[j * height + i] - data[(j - 1) * height + i]
            elif j - 1 < 0:
                Gn = data[(j + 1) * height + i] - data[j * height + i]
            else:
                Gn = data[(j + 1) * height + i] - data[(j - 1) * height + i]

            if abs(Gm) > abs(Gn):
                sumGrad += Gm
                sum += data[j * height + i] * Gm
            else:
                sumGrad += Gn
                sum += data[j * height + i] * Gn

    border = int(sum / sumGrad)
    print("Border Grad = ", border)
    return border


def otsuFunction(data):
    global sigma
    length = len(data)
    histogramData = [0] * 256
    p = []
    mK = []
    mG = 0

    for i in data:
        histogramData[i] += 1

    for k in range(256):
        temp = 0
        temp_1 = 0
        for i in range(k + 1):
            temp += histogramData[i] / length
            temp_1 += i * histogramData[i] / length
        p.append(temp)
        mK.append(temp_1)
        mG += k * histogramData[k] / length

    sigmaMax = 0
    border = 0
    for k in range(256):
        if (p[k] * (1 - p[k])) == 0:
            sigma = 0
        else:
            sigma = (pow(mG * p[k] - mK[k], 2) / (p[k] * (1 - p[k])))

        if sigma > sigmaMax:
            border = k
            sigmaMax = sigma
    print("Border Otsu = ", border)
    return border


# calculate resultHistogramImage
visualization(convertData, listX, listY)
borderHistogram = histogramFunction(convertData, 150, 5)
calculatedData = calculate(convertData, borderHistogram)
putDataAndSave(calculatedData, "images/lab3/resultHistogramImage.jpg", original.size)

# calculate resultGradientImage
borderGradient = gradientFunction(convertData, widthImage, heightImage)
calculatedData = calculate(convertData, borderGradient)
putDataAndSave(calculatedData, "images/lab3/resultGradientImage.jpg", original.size)

# calculate resultOtsuImage
borderOtsu = otsuFunction(convertData)
calculatedData = calculate(convertData, borderOtsu)
putDataAndSave(calculatedData, "images/lab3/resultOtsuImage.jpg", original.size)
