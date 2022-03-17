import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

original = Image.open("images/lab2/Bird.jpg")
draw = ImageDraw.Draw(original)
width = original.size[0]
height = original.size[1]
convertData = original.convert("L").getdata()


def visualization(data, valuesX, valuesY):
    for i in data:
        valuesY[i] += 1
    plt.stem(valuesX, valuesY)
    plt.show()


def evaluation(widthImage, heightImage):
    areaH = widthImage * heightImage
    argH = areaH / 256.0

    z = 0
    intH = 0
    left = [0] * 256
    right = [0] * 256
    new = [0] * 256
    newList = []

    for j in range(255):
        left[j] = z
        intH += listY[j]

        while intH > argH:
            intH -= argH
            z += 1

        right[j] = z
        new[j] = int((right[j] + left[j]) / 2.0)

    for i in convertData:
        if left[i] == right[i]:
            newList.append(left[i])
        else:
            newList.append(new[i])
    return newList


def linearContrast(param, minValue, maxValue):
    return int(((param - minValue) / (maxValue - minValue)) * (255 - 0) + 0)


def putDataAndSave(datas, path, size):
    convertImage = Image.new("L", size)
    convertImage.putdata(datas)
    convertImage.save(path)


# starting values for histogram
listX = list(range(256))
listY = [0] * 256

# Visualization histogram
visualization(convertData, listX, listY)
putDataAndSave(convertData, "images/lab2/convertImageAfterConversion.png", original.size)

# Equalization process and visualization histogram
newConvertData = evaluation(width, height)
visualization(newConvertData, listX, listY)
putDataAndSave(newConvertData, "images/lab2/convertImageAfterEqualization.png", original.size)

# Linear contrast
minValue = min(convertData)
maxValue = max(convertData)

listAfterLinearContrast = []
for i in convertData:
    listAfterLinearContrast.append(linearContrast(i, minValue, maxValue))
putDataAndSave(listAfterLinearContrast, "images/lab2/convertImageAfterLinearContrast.png", original.size)

# Selecting bit planes
bitPlane1 = []
bitPlane2 = []
bitPlane3 = []
bitPlane4 = []
bitPlane5 = []
bitPlane6 = []
bitPlane7 = []
bitPlane8 = []

for i in convertData:
    temp = []
    for j in range(8):
        if i % 2 == 0:
            temp.append(0)
        else:
            temp.append(255)
        i /= 2
    bitPlane1.append(temp[0])
    bitPlane2.append(temp[1])
    bitPlane3.append(temp[2])
    bitPlane4.append(temp[3])
    bitPlane5.append(temp[4])
    bitPlane6.append(temp[5])
    bitPlane7.append(temp[6])
    bitPlane8.append(temp[7])

putDataAndSave(bitPlane1, "images/lab2/convertImage1.png", original.size)
putDataAndSave(bitPlane2, "images/lab2/convertImage2.png", original.size)
putDataAndSave(bitPlane3, "images/lab2/convertImage3.png", original.size)
putDataAndSave(bitPlane4, "images/lab2/convertImage4.png", original.size)
putDataAndSave(bitPlane5, "images/lab2/convertImage5.png", original.size)
putDataAndSave(bitPlane6, "images/lab2/convertImage6.png", original.size)
putDataAndSave(bitPlane7, "images/lab2/convertImage7.png", original.size)
putDataAndSave(bitPlane8, "images/lab2/convertImage8.png", original.size)
