from PIL import Image
import os 

class ImageManip():

	size = 32, 32 
	# 16,16       446 duplicates 
	count = 0 
	# 8,8         417 duplicates 
	clusterSize = 3 
	#9,9 smart reference: 576 total dupes, reduced to 207

	def __init__(self, filename):

		self.name = filename #filename	

		self.makeSmartReference(self.name) # creates self.2dArray 

		ImageManip.count += 1 

	def makeSmartReference(self, name):
		try:		
			control = Image.open(name)
		except OSError:
			print("Whoops. Os error at file " + name )

		left, upper, right, lower = control.getbbox() 

		lookAtX = int(right / 2 )
		lookAtY = int(lower / 2 )

		self.controlPixels = [[None] * 3 for i in range(3)]

		for i in range(lookAtX, lookAtX+3):
			for j in range(lookAtY, lookAtY+3):
				self.controlPixels[ i - lookAtX ] [ j - lookAtY ] = control.getpixel((i,j))

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

		likeliness = 0

		for i in range(clusterSize):
			for j in range(clusterSize):
				if self.controlPixels[i][j] == other.controlPixels[i][j]:
					likeliness += 1 

		return (round(likeliness/(9)*100,2)) 

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

		futureKeys = [] 
		print("Choose extensions:")
		while True:
			userInput = input("")
			if userInput == "stop":
				break
			futureKeys.append(userInput) 

		return futureKeys

	def findSubdirectories(path):
		"""Finds all subDirs from path. Returns their path in a list."""
		directories = [] 

		for root, dirs, files in os.walk(path):
			for directory in dirs: 
				directories.append(os.path.join(root,directory))

		return directories 
	
	def findFilenames(path, extensions):
		"""Finds all filenames with the extensions we want.
		Returns a dictionary, with the key being the directory."""
		filenames = {} 

		for root, dirs, files in os.walk(path):
			filenames[root] = files 
			
		return filenames 

	def createAllObjects(filenamesDict):
		dictElems = {}
		variableCount = 0

		for path in filenamesDict:
					# gets list of all file names in current directory 
			for filename in filenamesDict[path]: # work with each file name one by one 
				try: 
					exec("im" + str(variableCount) + " = ImageManip(os.path.join(path,filename))") 
						# makes sure we have a different variable name for every Class object 
					dictElems[os.path.join(path,filename)] = eval("im" + str(count))
						# every object is saved in a dict with the path(inc filename) as a key 
				except UnboundLocalError:
					print("File behaved weirdly. Skipping it.")

				variableCount += 1 

				print ("Creating all objects: " + str(variableCount))
					#shows progress  
		#	if variableCount > 500: 
		#		break #usually stops at the end of all subdirectories 
			
		return dictElems


	def compareAllObjects(listObjects):
		"""Applies checkAgainst() to all permutations of objects. """

		print("Starting Comparison") 

		keyOffset = 0 
		progress = 0
		duplicatesDict = {} 

		#for primaryKey in dictArrays:

		for primaryElement in listObjects: 

			progress += 1 
			print(str(round(progress / len(listObjects) * 100)) + str("%") ) 
			
			keyOffset += 1 #keeps track of how far along we are, we save N/2 cpu 
			behindCheck = keyOffset

		#	for secondKey in dictArrays:
			for secondaryElement in listObjects:

				if behindCheck > 0: #while we're behind, do nothing 
					behindCheck -= 1 
				else:
					im1 = primaryElement
					im2 = secondaryElement

					if im1.checkAgainst(im2) >= 70:
						if im1.name in duplicatesDict:
							duplicatesDict[im1.name].append(im2.name)
						else: 
							duplicatesDict[im1.name] = [im2.name]
						#print(im1.name + " egal cu " + im2.name)
						#input("")

		return duplicatesDict

	def checkEvenness(objectList):
		evenX = 0 
		evenY = 0 
		for object in objectList:
			if object.xAxis % 2 == 0:
				evenX += 1 
			if object.yAxis % 2 == 0:
				evenY += 1 

		print("All elements: " + str(ImageManip.count))
		print("Elements with even xAxis: " + str(evenX))
		print("Elements with even yAxis: " + str(evenY))

		return None 


def TestSmartReference():
	path = "/media/removable/Seagate Expansion Drive/Asus Laptop/Chestii"

	extensionList = ["jpg"]

	filenamesDict = ImageManip.findFilenames(path,extensionList)
	#print(filenamesDict)
	objectList = ImageManip.createAllObjects(filenamesDict)

	duplicatesDict = ImageManip.compareAllObjects(objectList)

	fileCount = 0 
	duplicateCount = 0

	for key in duplicatesDict:
		fileCount += 1 
		for duplicate in duplicatesDict[key]:
			duplicateCount += 1 

	print("Duplicates: " + str(duplicateCount+fileCount))
	print("We can reduce them to: " + str(fileCount))
	print("Total files: " + str(ImageManip.count))
	memorySave = (duplicateCount-fileCount) / (ImageManip.count) * 100
	print("Possible memory save: " + str(round(memorySave,2)) + "%")


TestSmartReference()

# full size: 0.11 alike 
# 512,512 : 0.086  
# 256,256 : 0.076 
# 128,128 : 0.022 alike 
# 64, 64  : 0.00 
# 96,96   : 0.039 alike 

#Iteration 1, no tweaks, size 8,8:
# 1380 files in 90s - 1 dp
# 1268 files in 60s - 5 dp 
# 1053 files in 41s - 123 dp
# 1115 files in 66s - 2dp
# 1015 files in 67s - 4 dp
# 1549 files in 80s - 206 dp
# 1033 files in 40s - 201 dp
# 1026 files in 40s - 14 dp
# 1023 files in 45s - 205 dp
# 1155 files in 36s - 497 dp 

# average files: 1160
# average time: 56s  
# files/second: ~20 files /s  
# over 10 tests 

#Iteration 2, changed dict to list, size 8,8:
# total files : 14310 
# total time  : 700s
# files/second: 20 files /s  lol 

