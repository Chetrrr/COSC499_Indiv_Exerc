import unittest
from integerConcat import integerConcat

class test (unittest.TestCase):
    def test1(self):
        concatN = integerConcat(5,6)
        self.assertEqual((concatN),(11))

if __name__ == '__main__':
    unittest.main()
