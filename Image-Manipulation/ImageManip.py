from PIL import Image
import os 

class ImageManip():


	def __init__(self, name):

		self.name = name 
		self.xAxis = 0 
		self.yAxis = 0 

		self.size = 256 , 256 

		self.makeReference(self.name, self.size) # creates self.2dArray 

		pass 

	def makeReference(self, name, size):
		"""Makes 2d array of all the pixels. """
		
		control = Image.open(name) 
		control.thumbnail(size)

		left, upper, right, lower = control.getbbox() 
		#print(str(left) + " " + str(right))
		#print(str(upper) + " " + str(lower))
		self.controlPixels = [[None] * lower for i in range(right)] #creating 2d array 

		for i in range(left, right): #same sizes so it should not matter
			for j in range(upper, lower):
				#print(str(i) + " " + str(j)) 
				self.controlPixels[i][j]=control.getpixel((i,j)) #populating array 

		self.xAxis = right 
		self.yAxis = lower 

	def checkAgainst(self, other):

		if self.xAxis < other.xAxis:
			xAxis = self.xAxis 
		else:
			xAxis = other.xAxis 

		if self.yAxis < other.yAxis:
			yAxis = self.yAxis
		else:
			yAxis = other.yAxis 

		likeliness = 0

		for i in range(xAxis):
			for j in range(yAxis):
				if self.controlPixels[i][j] == other.controlPixels[i][j]:
					likeliness += 1 

		return (round(likeliness/(xAxis*yAxis)*100,2)) 

	def findExtensions(path):
		"""Returns dictionary of most seen extensions in certain path."""
		extensionDict = {} 

		for filename in os.listdir(path): #returns list of all files in path 
			
			trigger = False 
			extension = ""

			for character in filename:
				if character == "." or trigger == True:
					extension += character 
					trigger = True 

			if extension in extensionDict:
				extensionDict[extension] += 1 
			else:
				extensionDict[extension] = 1 

		return (extensionDict)


im1 = ImageManip("c1.jpg")
im2 = ImageManip("c1.jpg")

print(im1.checkAgainst(im2))
print(im2.checkAgainst(im1))

print(ImageManip.findExtensions(os.getcwd()))

# full size: 0.11 alike 
# 512,512 : 0.086  
# 256,256 : 0.076 
# 128,128 : 0.022 alike 
# 64, 64  : 0.00 
# 96,96   : 0.039 alike 