#!/usr/bin/python3
""" Test the console """

import unittest
import sys
import json
from io import StringIO
from models import storage
from console import HBNBCommand
from unittest.mock import patch

from models.place import Place


class TestConsole(unittest.TestCase):
    """ Test the console """

    def test_do_create(self):
        """ Test function that creates objects"""
        # If the class name is missing, print ** class name missing **
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("create")
        self.assertEqual(fd.getvalue(), '** class name missing **\n')

        # If the class name doesn’t exist, print ** class doesn't exist **
        with patch('sys.stdout', new=StringIO()) as fd:
            HBNBCommand().onecmd("create AnyModel")
        self.assertEqual(fd.getvalue(), '''** class doesn't exist **\n''')

        # If the class name exist, get id and
        # check if it is saved in the file storage
        # for class_name in HBNBCommand().classes.keys():
        #     with patch('sys.stdout', new=StringIO()) as fd:
        #         HBNBCommand().onecmd("create " + class_name)
        # self.assertIn(class_name + '.' + fd.getvalue()[:-1], storage.all())
        # with open(storage._FileStorage__file_path, "r") as f:
        #     test_dict = json.load(f)
        # for key in storage.all().keys():
        #     self.assertIn(key, test_dict)

        # If the class name exist, check if recives and set extra values
        with patch('sys.stdout', new=StringIO()) as fd:
            cmnd = 'create Place name="My_little_home"\
            number_rooms=8 latitude=-122.5465416'
            HBNBCommand().onecmd(cmnd)
            self.assertIn('Place.' + fd.getvalue()[:-1], storage.all())
