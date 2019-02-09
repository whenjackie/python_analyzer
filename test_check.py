import unittest
import ast

from checkhello import checkHello
# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class CheckHelloTest(unittest.TestCase):
    def test_correct_answer(self):
    	r = open('parse.py','r')
    	tree = ast.parse(r.read())
        self.assertEqual(checkHello(tree), True)

    def test_wrong_string(self):
    	r = open('parse2.py','r')
    	tree = ast.parse(r.read())
        self.assertEqual(checkHello(tree), False)

    def test_wrong_return_type(self):
        r = open('parse3.py','r')
    	tree = ast.parse(r.read())
        self.assertEqual(checkHello(tree), False)

if __name__ == '__main__':
    unittest.main()