#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.engine.db_storage import DBStorage
import os
import models


class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """

    def test_style_pep8_model(self):
        """ PEP8 python style """
        a = os.system("pep8 models/engine/db_storage.py")
        self.assertEqual(a, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        a = os.system("pep8 tests/test_models/test_engine/test_db_storage.py")
        self.assertEqual(a, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/engine/db_storage.py", mode='r') as f:
            r = f.read()
            b = r.splitlines()
            self.assertEqual(b[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        p = "tests/test_models/test_engine/test_db_storage.py"
        with open(p, mode='r') as f:
            r = f.read()
            b = r.splitlines()
            self.assertEqual(b[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.engine.db_storage.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(DBStorage.__doc__) != 0)
