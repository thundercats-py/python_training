import unittest
from factorial import factorial

# ... other importsj script codej etc. ... 

class FactorialTests(unittest.TestCase): 
    def testSingleValue(self): 
        self.assertEqual(factorial(5), 120)

    def testMultipleValues(self): 
        self.assertRaises(TypeError, factorial, [1,2,3,4])

    def testBoolean(self): 
        self.assertTrue(factorial(5) == 120) 

def main() : 
    """Main function for this script""" 
    unittest.main() # Chech the documentation for more verbosity Levels , etc. 
    # ... rest of main function ... 

if __name__ == "__main__":
    main()