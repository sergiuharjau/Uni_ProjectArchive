"""
1. Write a method that combines two strings, by taking one character from the first string, then one from
the second string and so on. Once one string has no characters left it should carry on with the other
string.
Input: two strings, such as s1 = "day" and s2 = "time"
Output: a result string, for the above input case it would be "dtaiyme".
"""
#Works as intended.

def stringCombine(string1, string2):
    
    result = ""
    
    for i in range(min(len(string1), len(string2))):
        result += string1[i] + string2[i]
    
    if len(string1) < len(string2):
        result += string2[len(string1):]
    else:
        result += string1[len(string2):]
        
    return result

if __name__ == "__main__":
    string1 = input("String1: ")
    string2 = input("String2: ")
    print(stringCombine(string1, string2))
    