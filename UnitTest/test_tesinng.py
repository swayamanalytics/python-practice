import unittest
from UnitTest import testinng

class TestUnitTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(testinng.add(10,5),15)
        self.assertEqual(testinng.add(-10,5),-5)
        self.assertEqual(testinng.add(0,0),0)
        self.assertEqual(testinng.add(-12,-10),-22)

    def test_substract(self):
        self.assertEqual(testinng.substract(10,5),5)
        self.assertEqual(testinng.substract(-10,5),-15)
        self.assertEqual(testinng.substract(0,0),0)
        self.assertEqual(testinng.substract(-12,-10),-2)

    def test_devide(self):
        with self.assertRaises(ValueError):
            testinng.devide(20,2)