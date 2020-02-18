
def getInput():
    x = []
    y = []
    label = []
    for line in open("mapInput.txt").readlines():
        values = line[:-1].split(",")
        y.append(values[0]) #webots is reversed
        x.append(values[1])
        label.append(values[2])

    return x, y, label


if __name__ == "__main__":
    
    xList, yList, labelList = getInput()

    result = ""
    i=0
    for x, y, label in zip(xList, yList, labelList):
        if label == " 3": 
            colour = "blue"
        else:
            colour = "yellow"
        translation = str(round(float(x),2)) + " -0.3 " + str(round(float(y),2))
        name = "cone" + colour + str(i)
        content = f'\n\ttranslation {translation}\n\tname "{name}"\n\tcolor "{colour}"\n'
        fullString = "FsCone {" + content + "}\n"
        i+=1
        result += fullString 

    open("result.txt", "w").write(result)