
def makeTable(x,y):
  """Function that makes a times table of size x,x"""
  print("\n")
  for i in range(-1,x+1):  #starts at -1 because we need a special case (-1)
    if i==-1:   #special case, prints the first row of numbers and the delimitator
      print("x     |     ",end="")
      for z in range (0,x+1):   #prints the numbers
        if z > 9:
          print(z, end="   ")   #makes sure the spacing lines up with the number of digits
        else:
          print(z, end="    ")  #single digits, more space
        z=z+1  
      print("")    #breaks the "end" thing, starts a new line
      k=6.1*x    #mathematical magic trying to get the right number of lines (it works)
      k=int(round(k,0))+5  #makes sure we get an even one, +mathsy stuff
      for z in range (0,k):  #prints the actual lines
        print("_", end="")
    else:
      if i > 9:
        print(i, end="    |     ")   #any >9 or >99 means I am getting the spacing right
      else:
        print(i, end= "     |     ")
    for j in range (0,y+1):   
      if i==-1:
        continue             #in the special case, skip it
      if i*j>99:
        print(i*j, end="  ")
      elif i*j>9:
        print(i*j, end="   ")
      else:
        print(i*j, end="    ")
    print("")    #no need for return because it is meant to print

x=int(input("Pick x: "))
y=x  #I wanted to firstly make it of range x,y, but it failed pretty bad, I resorted to making it x * x. therefore y=x

makeTable(x,y) #calls the function, starts the process