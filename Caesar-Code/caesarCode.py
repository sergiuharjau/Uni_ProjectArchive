
def listToString(list1): 
  """This function takes a list and turns it into a string"""
  result=list1
  result="".join(result)
  return(result)

def stringToList(value):
  """This function takes a string and inputs it to a list"""
  list1=[]
  y=len(value)
  x=0
  while x<y:
    list1.append(value[x])
    x=x+1				
  return(list1)

def encryptionTool(string,key):
  """This function takes a string and a key and outputs the string as encrypted"""
  list1= stringToList(string)  #we take the string and turn it into a list 
  y=len(list1)
  x=0
  x2=0
  finalList=list1
  while x<y:   #this ensures that the index is never out of bounds (x is the length of its own list)
    for z in range (0,26): #this ensures that we work through every reference (a through z)
      if list1[x]==reference[z]: #we check every letter we have with the reference
        if (z+key)>25:  #when it finds a match, it checks for a runtime error (regarding index)
          key2=(z-25)+key -1
          finalList[x]=reference[key2]
        else:
          finalList[x]=reference[z+key] 
        break
      elif list1[x]==reference2[z]:
        if (z+key)>25:
          key2=(z-25)+key -1
          finalList[x]=reference2[key2]
        else:
          finalList[x]=reference2[z+key] 
        break
      elif list1[x]==" ":
        finalList.append(" ")
        break 
      else: 
        pass
    x=x+1
  result=listToString(finalList) #we take the list and make it a string
  return(result)

def decodingTool(string, key):
  """This function takes a string and a key, and returns the decrypted string"""
  list1= stringToList(string)
  y=len(list1)
  x=0
  x2=0
  finalList=list1
  while x<y:
    for z in range (0,26):
      if list1[x]==reference[z]:
        if (z-key)<0:
          key2=26-(key-z)
          finalList[x]=reference[key2]
        else:
          finalList[x]=reference[z-key] 
        break
      elif list1[x]==reference2[z]:
        if (z-key)<0:
          key2=26-(key-z)
          finalList[x]=reference2[key2]
        else:
          finalList[x]=reference2[z-key] 
        break
      elif list1[x]==" ":
        finalList.append(" ")
        break 
      else: 
        pass
    x=x+1
  result=listToString(finalList)
  return(result)

reference=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

reference2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

xy=1

while xy==1:
  decision=int(input(" \nTo encrypt, press 1. \nTo decrypt, press 0.\n"))
  if decision==1:
    value=input("What do you want to encrypt? \n")
    key=int(input("Choose a key from 1 through 26:\n"))
    message= encryptionTool(value,key)
    print(" \nYour encrypted message is: \n" +str(message) +" \n" )
    xy=int(input("Do you want to keep using this program?\n1-yes\n0-no\n"))
  elif decision==0:
    value=input("What do you want to decrypt? \n")
    key=int(input("Choose a key from 1 through 26:\n"))
    message= decodingTool(value, key)
    print(" \nYour decrypted message is: \n" + str(message) + " \n")
    xy=int(input("Do you want to keep using this program?\n1-yes\n0-no\n"))
  else:
    print("Please input a valid value.")







     

