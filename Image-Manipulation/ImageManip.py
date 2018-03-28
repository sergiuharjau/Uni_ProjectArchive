from PIL import Image
import os 

class ImageManip():

	size = 24, 24 
	# 16,16       446 duplicates 
	count = 0 
	# 8,8         417 duplicates 

	def __init__(self, filename):

		self.name = filename #filename

		self.xAxis = 0 
		self.yAxis = 0 	

		self.makeReference(self.name, ImageManip.size) # creates self.2dArray 

		ImageManip.count += 1 

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
			firstTime = True 

			for filename in files:
				for ext in extensions:
					
					if ext in filename:				
						if firstTime == True:
							filenames[root] = [] #root, which is this directory's path  

						filenames[root].append(filename)

						firstTime = False  
		return filenames 

	def createAllObjects(filenamesDict):
		listElems = [] 
		variableCount = 0

		for path in filenamesDict:
		#	os.chdir(path)  #not needed 

			filenames = filenamesDict[path] # gets list of all file names in current directory 

			for filename in filenames: # work with each file name one by one 
				try: 
					exec("im" + str(variableCount) + " = ImageManip(os.path.join(path,filename))") 
						# makes sure we have a different variable name for every Class object 
				#	dictElems[os.path.join(path,filename)] = eval("im" + str(count))
					listElems.append(eval("im" + str(variableCount))) #trying a list 
						# every object is saved in a dict with the path(inc filename) as a key 
				except UnboundLocalError:
					print("File behaved weirdly. Skipping it.")

				variableCount += 1 

				#print ("Creating all objects: " + str(round(variableCount / 1000 * 100)) + str("%"))
					#shows progress  
		#	if variableCount > 500: 
		#		break #usually stops at the end of all subdirectories 
			
		return listElems

	def compareAllObjects(listObjects):
		"""Applies checkAgainst() to all permutations of objects. """

		print("Ready to compare " + str(ImageManip.count) + " objects?")
	
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

					if im1.checkAgainst(im2) > 70:
						if im1.name in duplicatesDict:
							duplicatesDict[im1.name].append(im2.name)
						else: 
							duplicatesDict[im1.name] = [im2.name]
						#print(im1.name + " egal cu " + im2.name)
						#input("")

		return duplicatesDict



def TestProgram():
	path = "/media/removable/Seagate Expansion Drive/Asus Laptop/Chestii"

	extensionsList = ["jpg"]

	filenamesDict = ImageManip.findFilenames(path,extensionsList)

	#print(filenamesDict)

	dictArrays = ImageManip.createAllObjects(filenamesDict)

	duplicatesDict = ImageManip.compareAllObjects(dictArrays)

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

	return (ImageManip.count)

testSize = 1
totalFiles = 0 

for i in range(testSize):
	print("\n\n\n\nTests Left " + str(testSize - i)) 
	totalFiles += TestProgram() 

print("Files tested: " + str(totalFiles))

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

