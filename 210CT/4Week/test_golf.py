import unittest 
import codeGolf as cg 

class TestGolf(unittest.TestCase):
    
    def test_Palindrome(self):
        palindromeList = ["anna", "civic", "racecar", "kayak", "level", "mom"]
        for element in palindromeList:
            self.assertTrue(cg.isPalindrome(element))
        randomWords = ["chocolate", "peanuts", "music", "serge", "coventry", "uni"] 
        for element in randomWords:
            self.assertFalse(cg.isPalindrome(randomWords))
    
    def test_Substring(self):
        words = ["test", "racecar", "machine", "library", "phoenix"]
        for givenInput in words:
            for substring in cg.everySubstring(givenInput):
                self.assertIn(substring, givenInput) #checks if substring is part of main string 
    
if __name__ == "__main__":
    unittest.main() 