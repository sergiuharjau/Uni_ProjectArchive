from PIL import Image
import os 

class ImageManip():
#I've had better class names 
	size = 64, 64 #reduce every image to approx 64,64 pixels

	count = 0 

	clusterSize = 2 #using clusters of 2*2 pixels 

	offSet = 4 #3 clusters, offset by 4 pixels 

	def __init__(self, filename):

		self.name = filename #filename	

		self.makeSmartReference(self.name) # creates self.2dArray 

		ImageManip.count += 1 

	def makeSmartReference(self, name):
	
		try:		
			control = Image.open(name)
		except OSError:
			print("Whoops. Os error at file " + name )

		control.thumbnail(ImageManip.size)
		
		left, upper, right, lower = control.getbbox() 

		lookAtX = int( (right - ImageManip.clusterSize) / 2 ) 
		lookAtY = int( (lower - ImageManip.clusterSize) / 2 )
				#fancy maths to make sure we're not off bounds 
		self.constructArray(lookAtX, lookAtY, control, 1)

		lookAtX += ImageManip.offSet
		lookAtY += ImageManip.offSet

		self.constructArray(lookAtX, lookAtY, control, 2)

		lookAtX -= 2 * ImageManip.offSet # so we're 1 offSet behind the original lookAtX 
		lookAtY -= 2 * ImageManip.offSet

		self.constructArray(lookAtX , lookAtY, control, 3)

	def constructArray(self, lookAtX, lookAtY, control, integer):
		"""Takes as input the necessary variables, and constructs a self. 2Darray"""
		exec("self.controlPixels" + str(integer) + " = [[None] * ImageManip.clusterSize for i in range(ImageManip.clusterSize)]")

		for i in range(lookAtX, lookAtX+ImageManip.clusterSize):
			for j in range(lookAtY, lookAtY+ImageManip.clusterSize):
				try:
					exec("self.controlPixels"+ str(integer) + "[ i - lookAtX ] [ j - lookAtY ] = control.getpixel((i,j))")
				except IndexError:
					print("This image: " + self.name + " is way too tiny.")
					input("")

	def makeReference(self, name, size):
		"""Makes 2d array of all the pixels. """
		try:
			control = Image.open(name) 
		except OSError:
			print("Whoops. Os error at file " + name)

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
		"""Functions that compares two objects"""
		likeliness = 0

		for i in range(ImageManip.clusterSize):
			for j in range(ImageManip.clusterSize):
				if self.controlPixels1[i][j] == other.controlPixels1[i][j]:
					likeliness += 0.33
				if self.controlPixels2[i][j] == other.controlPixels2[i][j]:
					likeliness += 0.33
				if self.controlPixels3[i][j] == other.controlPixels3[i][j]:
					likeliness += 0.33
		return (round(likeliness/(ImageManip.clusterSize**2)*100,2)) 

	def findCurrentExtensions(path):
		"""Returns list of all extensions in certain path."""
		extensionList = []

		for filename in os.listdir(path): #returns list of all files in path 
			
			trigger = False 
			extension = ""

			for character in filename:
				if character == "." or trigger == True:
					extension += character 
					trigger = True 

			if (extension not in extensionList) and (extension != ""):
				extensionList.append(extension)

		return extensionList

	def findAllExtensions(path):
		"""Finds all extensions in path and subdirectories, returns list. """
		extensionList = [] 

		for root, dirs, files in os.walk(path):
			for element in ImageManip.findCurrentExtensions(root):
				if element not in extensionList:
					extensionList.append(element)

		return extensionList

	def filterExtensions(extensions):
		"""Filters extensions according to the user's needs."""
		futureKeys = [] 
		print("Choose extensions:")
		while True:
			userInput = input("")
			if userInput == "stop":
				break
			futureKeys.append(userInput) 

		return futureKeys
	
	def findFilenames(path, extensions):
		"""Finds all filenames with the extensions we want.
		Returns a dictionary, with the key being the directory."""
		filenames = {} 

		for root, dirs, files in os.walk(path):
			goodFiles = [] 
			for filename in files: 
				for ext in extensions:
					if ext in filename: 
						goodFiles.append(filename)

			filenames[root] = goodFiles
			
		return filenames 

	def createAllObjects(filenamesDict):
		listElems = []
		variableCount = 0

		for path in filenamesDict:
					# gets list of all file names in current directory 
			for filename in filenamesDict[path]: # work with each file name one by one 
				try: 
					exec("im" + str(variableCount) + " = ImageManip(os.path.join(path,filename))") 
						# makes sure we have a different variable name for every Class object 
					listElems.append(eval("im" + str(variableCount)))
						# every object is saved in a dict with the path(inc filename) as a key 
				except UnboundLocalError:
					print("File behaved weirdly. Skipping it.")

				variableCount += 1 

				print ("Creating all objects: " + str(variableCount))
					#shows progress  
			#	if variableCount > 5000: 
			#		break #usually stops at the end of all subdirectories 
			
		return listElems


	def compareAllObjects(listObjects):
		"""Applies checkAgainst() to all permutations of objects. """

		print("Starting Comparison") 

		keyOffset = 0 
		progress = 0
		duplicatesDict = {} 

		for primaryElement in listObjects: 

			progress += 1 
			print(str(round(progress / len(listObjects) * 100)) + str("%") ) 
			
			keyOffset += 1 #keeps track of how far along we are, we save N/2 cpu 
			behindCheck = keyOffset

			for secondaryElement in listObjects:

				if behindCheck > 0: #while we're behind, do nothing 
					behindCheck -= 1 
				else:
					im1 = primaryElement
					im2 = secondaryElement

					if im1.checkAgainst(im2) >= 90:
						if im1.name in duplicatesDict:
							duplicatesDict[im1.name].append(im2.name)
						else: 
							duplicatesDict[im1.name] = [im2.name]
						#print(im1.name + " egal cu " + im2.name)
						#input("")

		return duplicatesDict


def TestSmartReference():
	path = "/media/removable/Seagate Expansion Drive/Asus Laptop/Chestii"
	
	extensionList = ["jpg"]

	filenamesDict = ImageManip.findFilenames(path,extensionList)
	#print(filenamesDict)
	objectList = ImageManip.createAllObjects(filenamesDict)

	duplicatesDict = ImageManip.compareAllObjects(objectList)

	uniqueFileCount = 0 
	duplicateCount = 0

	for key in duplicatesDict:
		uniqueFileCount += 1 
		for duplicate in duplicatesDict[key]:
			duplicateCount += 1 

	print("Duplicates: " + str(duplicateCount+uniqueFileCount))
	print("We can reduce them to: " + str(uniqueFileCount))
	print("Total files: " + str(ImageManip.count))
	memorySave = (duplicateCount-uniqueFileCount) / (ImageManip.count) * 100
	print("Possible memory save: " + str(round(memorySave,2)) + "%")


if __name__ == "__main__":
	TestSmartReference()