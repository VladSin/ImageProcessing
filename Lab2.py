import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

original = Image.open("images/lab2/Image.png")
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
    averageH = areaH / 256.0

    z = 0
    int_h = 0
    left = [0] * 256
    right = [0] * 256
    new = [0] * 256

    newList = []

    for j in range(255):
        left[j] = z
        int_h += listY[j]

        while int_h > averageH:
            int_h -= averageH
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


def bitPlaneSelection():
    return 4


# vars for histogram
listX = list(range(256))
listY = [0] * 256

# visualization histogram
visualization(convertData, listX, listY)

# equalization process
newConvertList = evaluation(width, height)

# visualization histogram
visualization(newConvertList, listX, listY)

convertImage = Image.new("L", original.size)
convertImage.putdata(newConvertList)
convertImage.save("images/lab2/convertImageHistogram.png")

# linear contrast
minValue = min(convertData)
maxValue = max(convertData)

lstNewLin = []
for i in convertData:
    lstNewLin.append(linearContrast(i, minValue, maxValue))

convertImage = Image.new("L", original.size)
convertImage.putdata(lstNewLin)
convertImage.save("images/lab2/convertImageAfterLinearContrast.png")

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []

for i in convertData:
    temp = []
    for j in range(8):
        if i % 2 == 0:
            temp.append(0)
        else:
            temp.append(255)
        i /= 2
    list1.append(temp[0])
    list2.append(temp[1])
    list3.append(temp[2])
    list4.append(temp[3])
    list5.append(temp[4])
    list6.append(temp[5])
    list7.append(temp[6])
    list8.append(temp[7])

convertImage = Image.new("L", original.size)
convertImage.putdata(list1)
convertImage.save("images/lab2/convertImage1.png")

convertImage = Image.new("L", original.size)
convertImage.putdata(list2)
convertImage.save("images/lab2/convertImage2.png")

convertImage = Image.new("L", original.size)
convertImage.putdata(list3)
convertImage.save("images/lab2/convertImage3.png")

convertImage = Image.new("L", original.size)
convertImage.putdata(list4)
convertImage.save("images/lab2/convertImage4.png")

convertImage = Image.new("L", original.size)
convertImage.putdata(list5)
convertImage.save("images/lab2/convertImage5.png")

convertImage = Image.new("L", original.size)
convertImage.putdata(list6)
convertImage.save("images/lab2/convertImage6.png")

convertImage = Image.new("L", original.size)
convertImage.putdata(list7)
convertImage.save("images/lab2/convertImage7.png")

convertImage = Image.new("L", original.size)
convertImage.putdata(list8)
convertImage.save("images/lab2/convertImage8.png")
