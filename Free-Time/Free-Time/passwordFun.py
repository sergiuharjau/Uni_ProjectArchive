def readPasswords():
	f1 = open("linkedin_passwords.txt", "r")
	bigList = f1.readlines() 
	
	i = 0 
	
	naughtyDict = {}
	
	percent = 1 
	
	for element in bigList[100:]:
		if len(bigList) % percent == 1:
			print (percent / len(bigList) * 100)
		for element2 in bigList[100:]: 
			if i == 0:
				pass
			else: 
				if element == element2:
					print("Found two! " + element + " " + element2)
					input("")
			i += 1 
		i = 0 
		percent += 1 
		
	return naughtyDict

dictionary = readPasswords()

maxValue = 1 

for key in dictionary:
	if dictionary[key] > maxValue:
		maxValue = dictionary[key]
		
		
print (maxValue)