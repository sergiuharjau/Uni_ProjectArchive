"""Write a program that finds the longest palindromic substring of a given string"""

def isPalindrome(target):
    """Checks if target is palindrome. Returns bool."""
    for i in range(len(target)//2):
        if target[i] != target[len(target)-i-1]:
            return False
    return True 

def everySubstring(target):
    """Returns a list of all possible substrings of given target, descending order."""
    
    substrings = [] 
    for i in range(len(target)):
        for j in range(i+1,len(target)):
            substrings.append(target[i:j+1])
    
    substrings.remove(target)
    
    return substrings

def main(target):
    """Processes given word, then checks all substrings for palindromes."""
    
    maximum = ""
    
    for element in everySubstring(target):
        if isPalindrome(element):
            if len(element) > len(maximum):
                maximum = element 
            
    return maximum


if __name__ == "__main__":
    word = input() 
    print(main(word))