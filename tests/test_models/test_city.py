#!/usr/bin/python3
""" Module for testing the city class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import models
import os


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value(state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value(name="San Francisco")
        self.assertEqual(type(new.name), str)

    def test_style_pep8_model(self):
        """ PEP8 python style """
        a = os.system("pep8 models/city.py")
        self.assertEqual(a, 0)

    def test_style_pep8(self):
        """ PEP8 python style """
        a = os.system("pep8 tests/test_models/test_city.py")
        self.assertEqual(a, 0)

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/city.py", mode='r') as f:
            r = f.read()
            b = r.splitlines()
            self.assertEqual(b[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_city.py", mode='r') as f:
            r = f.read()
            b = r.splitlines()
            self.assertEqual(b[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.city.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(City.__doc__) != 0)
