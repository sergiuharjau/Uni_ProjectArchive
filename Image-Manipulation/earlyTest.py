from PIL import Image


im = Image.open("easy.png")
size = 32 , 32  
im.thumbnail(size)
im.save("thumbnail version", "PNG")

data = list(im.getdata())

im2 = Image.open("different2.png")
im2.thumbnail(size)
im2.save("different version2" , "PNG")

data2 = list(im2.getdata())

print(data2)

count = 0 

for element in data2:
	print (element)
	count += 1

print(count) 

totalP1 = 0 
totalP2 = 0 
totalP3 = 0 
totalTuples = 0 

for i in range(len(data)):

	firstP1, firstP2, firstP3 = data[i]

	secondP1, secondP2, secondP3 = data2[i]

	if firstP1 == secondP1:
		totalP1 += 1 

	if firstP2 == secondP2:
		totalP2 += 1

	if firstP3 == secondP3: 
		totalP3 += 1 

	totalTuples += 1  

p1Percent = totalP1/ (totalTuples )
p2Percent = totalP2/ (totalTuples ) # 1 is 100% 
p3Percent = totalP2/ (totalTuples ) 

if (p1Percent > .75 and p2Percent > .75 and p3Percent >.75):
	print("They're basically the same")

print (p1Percent)
print (p2Percent)
print (p3Percent)

print (totalTuples * 3) 