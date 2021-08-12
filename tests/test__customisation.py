##
# Tests in this file verify that placeholder values in the template project have been customised.
##
import unittest
import sys
import string
import random
import importlib
import os

sys.path.append('..') # To find the core module in the folder above.


class test_customisation(unittest.TestCase):

    def setUp(self):

        self.tokens = ['PROJECTNAME',
                       'AUTHORNAME']


    def test_module_name(self):

        defaultProject = importlib.util.find_spec("PROJECTNAME")
        self.assertIsNone(defaultProject, msg='Module folder name "PROJECTNAME" must be customised.')


    def test_setup_py(self):

        with open(os.path.join('..', 'setup.py')) as f: 
            setupPy = f.read()

        for token in self.tokens:
            with self.subTest(msg=f'Checking for "{token}" in "setup.py"'):
                self.assertFalse(token in setupPy, msg=f'All instances of "{token}" in "setup.py" must be customised.')


    def test_readme(self):

        with open(os.path.join('..', 'README.md')) as f: 
            setupPy = f.read()
