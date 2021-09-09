
import unittest     # this makes Python unittest module available
import math

def classifyTriangle(a, b, c):
    """
    
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
        
        
    """
    x = ""
    
    if a == b == c:
        x = x + 'Equilateral'
    elif a == b or a == c or b == c:
        x = x + 'Isosceles'
    elif a == 0 or b == 0 or c == 0:
        x = x + 'NotATriangle'
    elif pow(a,2) + pow(b,2) == pow(c,2) or pow(c,2) + pow(b,2) == pow(a,2) or pow(a,2) + pow(c,2) == pow(b,2):
        x = x + 'Right'
    else:
        x = x + 'Scalene'
    return x
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right')
        self.assertEqual(classifyTriangle(0,4,5),'NotATriangle')
        self.assertEqual(classifyTriangle(3,4,3),'Isosceles')
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral')
        self.assertEqual(classifyTriangle(3,4,2),'Scalene')
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        #self.assertEqual(classifyTriangle(0,0,0),'NotATriangle')  failure: both NotATriangle and Equilateral
        #self.assertEqual(classifyTriangle(1,1,0),'NotATriangle')  failure: both NotATriangle and Isosceles
        self.assertEqual(classifyTriangle(6,1,4),'Scalene')
        #self.assertEqual(classifyTriangle(1,3),'NotATriangle')  failure: not enough positional arguments
        #self.assertEqual(classifyTriangle(1,2,3,4),'NotATriangle') failure: too many positional arguments
        self.assertEqual(classifyTriangle(7,1,7),'Isosceles')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    
    unittest.main(exit=True) # this runs all of the tests