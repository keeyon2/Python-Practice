import unittest
import sys
import os
from practicemodules import twoargprog

print "First Line in test"
# filename = "practicemodules/twoargprog"
# sys.path.insert(0, os.path.dirname(filename))


class TestTwoArgProgramFunctions(unittest.TestCase):
    def setUp(self):
        # self.twoargprog = practicemodules.twoargprog
        print "running Test"

    def test_adding_two_numbers(self):
        print "Running Test test_adding_two_numbers"
        warning = "add_two_numbers gave an incorrect addition value"
        self.assertEqual(twoargprog.add_two_numbers(1, 2), 3, warning)

    # def test_adding_mult_args(self):
    #     self.assertEqual(self.twoargprog.mult_arguments_addition(1,2,3,4),
    #         10, "mult_arguments_addition gave incorrect return value")

if __name__ == '__main__':
    unittest.main()
