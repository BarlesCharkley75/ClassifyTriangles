import unittest
import triangles

class Test_triangles(unittest.TestCase):
    def test_1(self):
        self.assertEqual(triangles.classify_triangle(3,4,5),'Right')
    def test_2(self):
        self.assertEqual(triangles.classify_triangle(0,4,5),'NotATriangle')
    def test_3(self):
        self.assertEqual(triangles.classify_triangle(3,4,3),'Isosceles')
    def test_4(self):
        self.assertEqual(triangles.classify_triangle(3,3,3),'Equilateral')
    def test_5(self):
        self.assertEqual(triangles.classify_triangle(3,4,2),'Scalene')
    def test_6(self):
        self.assertEqual(triangles.classify_triangle(5,3,4),'Right')
    def test_7(self):
        self.assertEqual(triangles.classify_triangle(6,1,4),'Scalene')
    def test_8(self):
        self.assertEqual(triangles.classify_triangle(7,1,7),'Isosceles')
        
if __name__ == '__main__':
    unittest.main()
