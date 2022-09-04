#!/usr/bin/python3
"""Test suite for the State class of the models.state module"""
import unittest

from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
   """Defines tests for State Class"""

    def setUp(self):
        self.state = State()
        self.state1.name = "Addis Ababa"


    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))
