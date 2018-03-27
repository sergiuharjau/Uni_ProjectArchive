from PIL import Image
import os 

class ImageManip():

	size = 8, 8 
	count = 0 

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
							filenames[root] = [] 

						filenames[root].append(filename)

						firstTime = False  
		return filenames 

	def saveAllArrays(filenamesDict):
		dictArrays = {} 
		count = 0

		for path in filenamesDict:
			os.chdir(path)

			filenames = filenamesDict[path]

			for filename in filenames:
				"""
				try: 
					referenceImage = ImageManip(filename)
					dictArrays[os.path.join(path, filename)] = referenceImage.controlPixels 
				except UnboundLocalError: 
					print("File behaved weirdly. Skipping it.")
				"""
				try: 
					exec("im" + str(count) + " = ImageManip(filename)")
					dictArrays[os.path.join(path,filename)] = eval("im" + str(count))
				except UnboundLocalError:
					print("File behaved weirdly. Skipping it.")

				count += 1 

				print (str(round(count / 500 * 100)) + str("%"))

			if count > 1000: 
				break
			
		return dictArrays

	def compareAllArrays(dictArrays):
		keyOffset = 0 
		progress = 0 
		print("Ready to compare " + str(ImageManip.count) + " objects?")
		input("")
		duplicatesDict = {} 

		for primaryKey in dictArrays:
			progress += 1 
			print(str(round(progress / len(dictArrays) * 100)) + str("%") ) 
			keyOffset += 1 #keeps track of how far along we are, we save N/2 cpu 
			i = keyOffset

			for secondKey in dictArrays:
				if i > 0: #while we're behind, do nothing 
					i -= 1 
				else:
					im1 = dictArrays[primaryKey]
					im2 = dictArrays[secondKey]
					if im1.checkAgainst(im2) > 70:
						if os.path.join(primaryKey,im1.name) in duplicatesDict:
							duplicatesDict[os.path.join(primaryKey,im1.name)].append(os.path.join(secondKey,im2.name))
						else: 
							duplicatesDict[os.path.join(primaryKey,im1.name)] = [os.path.join(secondKey,im2.name)]

		return duplicatesDict




path = "/media/removable/Seagate Expansion Drive/Asus Laptop/Chestii"

extensionsList = ["jpg"]

filenamesDict = ImageManip.findFilenames(path,extensionsList)

#print(filenamesDict)

dictArrays = ImageManip.saveAllArrays(filenamesDict)

duplicatesDict = ImageManip.compareAllArrays(dictArrays)

fileCount = 0 
duplicateCount = 0

for key in duplicatesDict:
	fileCount += 1 
	for duplicate in duplicatesDict[key]:
		duplicateCount += 1 

print("Duplicates: " + str(duplicateCount+fileCount))
print("We can reduce them to: " + str(fileCount))
print("Total files: " + str(ImageManip.count))
print("Possible memory save: " + str((duplicateCount -fileCount) / (ImageManip.count) * 100) + "%")
"""
copyDictionaries = {} 

for path in filenamesDict:

	os.chdir(path)

	filenames = filenamesDict[path] 

	for i in range(len(filenames)):

		referenceImage = ImageManip(filenames[i])
		count = 0
		print(filenames[i])

		for j in range(i+1,len(filenames)): 
			comparedImage = ImageManip(filenames[j])

			percentage = referenceImage.checkAgainst(comparedImage)

			#print(filenames[i] + " and " + filenames[j] + " " + str(percentage) + "%") 

			if percentage == 100:
				if filenames[i] in copyDictionaries:
					copyDictionaries[filenames[i]].append(filenames[j])
					count += 1  
				else:
					copyDictionaries[filenames[i]] = [filenames[j]]

		print(count)			
		if count > 0: 
			print(copyDictionaries)
		
"""

# full size: 0.11 alike 
# 512,512 : 0.086  
# 256,256 : 0.076 
# 128,128 : 0.022 alike 
# 64, 64  : 0.00 
# 96,96   : 0.039 alike 

#Iteration 1, no tweaks:
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
# average speed: 56s  
# over 10 tests 