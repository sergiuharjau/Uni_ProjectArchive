two2 = 4 
for i in range(3,21):
  exec( "two" + str(i) + " = two" + str(i-1) + " *  2" )
print( "2 to the 20th power " + str(two20) )