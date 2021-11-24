import unittest
import puzzle 

class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = "foobar"
        answer = puzzle.solve(data)
        self.assertEqual(-1, answer)

if __name__ == '__main__':
    unittest.main()
