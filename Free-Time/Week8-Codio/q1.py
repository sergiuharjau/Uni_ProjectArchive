class Fraction:
    """Class of fraction objects. First argument: nummerator, second argument: denominator.
    You can input a float as the first number, and the string "float" as the second 
    argument to turn the float into a fraction. We support the operations:
    print, +, -, *, /, <, >, ==, and simplify. """
    
    def __init__(self,n,d):
        
        if d =="float":
            i=0
            while n % 10 !=0:  #while n is a float 
                i = i + 1
                n = n * 10   #find the power of 10 of decimals
            self.n = round(n)  
            self.d= 10 ** i  #d is whatever the power of 10 is 
            
        elif type(n) != int or type(d) != int:
            raise ValueError("Both numbers need to be integers.")
        elif d == 0:
            raise ValueError("D can't be 0")
        elif d < 0:
            self.n = -n
            self.d = -d            
        else:
            self.n = n
            self.d = d 
            
        self.simplify()  #simplifies any created fraction 
        
    def __str__(self):
        """ Takes care of printing. """
        if self.d != 1:
            ans = str(self.n) + "/" + str(self.d) 
        else:
            ans = str(self.n)
        return ans
    
    def __radd__(self,other):
        """ Takes care of integer + fraction object. """
        if type(other) == int:
            nFinal = self.n + self.d * other
            dFinal = self.d
        return(Fraction(nFinal,dFinal))
    
    def __add__(self,other):
        """ Does addition between fractions. """
        if type(other) == int:
            nFinal = self.n + self.d * other
            dFinal = self.d
        else:
            nFinal = self.n * other.d + other.n * self.d
            dFinal = self.d * other.d 
        return(Fraction(nFinal,dFinal))
    
    def __sub__(self,other):
        """ Does substraction between fractions. """
        nFinal = self.n * other.d - other.n * other.d
        dFinal = self.d * other.d 
        return(Fraction(nFinal,dFinal))
    
    def __mul__(self,other):
        """ Does multiplication between fractions. """
        nFinal = self.n * other.n
        dFinal = self.d * other.d
        return(Fraction(nFinal,dFinal))
    
    def __truediv__(self, other):
        """ Does division between fractions. """
        nFinal = self.n * other.d 
        dFinal = self.d * other.n 
        return(Fraction(nFinal,dFinal))
    
    def __eq__(self,other):
        """ Checks equality between fractions. """
        result1 = self.n / self.d
        result2 = other.n / other.d 
        if result1 == result2:
            return True 
        else:
            return False
        
    def __lt__(self,other):
        """ Checks lower than between fractions. """
        result1 = self.n / self.d
        result2 = other.n / other.d 
        if result1 < result2:
            return True
        else:
            return False
        
    def __gt__(self,other):
        """ Checks greater than between fractions. """
        result1 = self.n / self.d
        result2 = other.n / other.d 
        if result1 > result2:
            return True
        else:
            return False
        
    def simplify(self):
        """ Simplifies fractions. """
        for count in range (1,10): #finds factors of prime numbers to the power of 10 max
            for i in [2,3,5,7,9]: #prime numbers to check for factors
                if self.n // i == self.n / i and self.d // i == self.d / i:
                    self.n = self.n // i
                    self.d = self.d // i 

def makeFraction(): 
    print("Note: Input an integer followed by the string 'float' to convert it to a fraction")
    n = input("What do you want your numerator to be? ")
      
    d = input("What do you want your denominator to be? ")
        
    if d == "float":
        n= float(n)
        pass
    else:
        n = int(n)
        d = int(d)
    return(Fraction(n,d))
    
fraction1 = makeFraction()

fraction2 = makeFraction()

fractionAdd = fraction1 + fraction2
fractionSub = fraction1 - fraction2
fractionMul = fraction1 * fraction2 
fractionDiv = fraction1 / fraction2
fractionEq  = fraction1 == fraction2
fractionLower = fraction1 < fraction2
fractionGreater = fraction1 > fraction2


print (str(fraction1)+ " + " +str(fraction2)+ "  =   " + str(fractionAdd))
print (str(fraction1)+ " - " +str(fraction2)+ "  =   " + str(fractionSub))
print (str(fraction1)+ " * " +str(fraction2)+ "  =   " + str(fractionMul))
print (str(fraction1)+ " / " +str(fraction2)+ "  =   " + str(fractionDiv))
print (str(fraction1)+ " = " +str(fraction2)+ " --> " + str(fractionEq))
print (str(fraction1)+ " < " +str(fraction2)+ " --> " + str(fractionLower))
print (str(fraction1)+ " > " +str(fraction2)+ " --> " + str(fractionGreater))


#print(fraction2)
#fraction1.simplify()
#fraction2.simplify()
#print(fraction1)
#print(fraction2)

