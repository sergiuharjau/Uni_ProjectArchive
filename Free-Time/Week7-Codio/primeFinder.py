
def makeList(value,x):   
  """Function to make a list of size (1,value)"""
  while x<value: 
    list1.append(x+1)   #increments itself until it reaches the desired value
    x=x+1
  return(list1)

primenumbers=[2,3,5,7,9,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]

def makePrimeNumbers(list1,value):
  """Function that takes a list and outputs the prime numbers in it"""
  for i in primenumbers:
    for z in range (2,value):   #starting at two because otherwise we delete the first prime
      result=i*z     #using the method described in the labsheet, i is a prime number
      if result >value:
        break         #if the results is bigger than what's in the list, break the loop, prevents an error
      if result in list1:  # part of the method, remove multiples of prime from the list
        list1.remove(result)
      else:
        continue    #if it's not in the list, just continue the iteration, prevents an error
  return(list1)

#To be noted that this program works because a prime is never the multiple of any two numbers, so it never deletes any primes, only other numbers

x=1  #we start the numbers from 2, x=1 here, and x=x+1 upstairs, because 1 is not a prime

value=int(input("Enter a number: "))

list1=[]             #prevents an error message

list1=makePrimeNumbers(makeList(value,x),value)  #self explanatory

print("Here are your prime numbers!!\n"+str(list1)) #the \n breaks the line, starts a new one




  