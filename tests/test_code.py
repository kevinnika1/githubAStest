import unittest
import sys
import string
import random

sys.path.append('..') # To find the core module in the folder above.


def randomword(length):
    # Function to generate random strings:
    validChars = string.ascii_letters + string.digits
    return ''.join(random.choice(validChars) for i in range(length))


class test_module(unittest.TestCase):
    """
    Add your custom unit tests here.
    """

    def test_externalFunction(self):
        raise NotImplementedError()
