#!/usr/bin/python3
""" Defines a class TestCity for City module. """
import unittest
from models.city import City
from models.base_model import BaseModel
import datetime

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    @classmethod
    def setUp(cls):
       
        cls.city1 = City()
        cls.city1.name = "Addis Ababa"

    @classmethod
    def tearDown(cls):
        """Clean-up after each test """
        
        del cls.city1

    def test_class_exists(self):
        """Tests if class exists """
        
        result = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.city1)), result)

    def test_inheritance(self):
        
        self.assertIsInstance(self.city1, City)
        self.assertEqual(type(self.city1), City)
        self.assertEqual(issubclass(self.city1.__class__, BaseModel), True)

    def test_types(self):
       
        self.assertIsInstance(self.city1.name, str)
        self.assertEqual(type(self.city1.name), str)
        self.assertIsInstance(self.city1.id, str)
        self.assertEqual(type(self.city1.id), str)
        self.assertIsInstance(self.city1.created_at, datetime.datetime)
        self.assertIsInstance(self.city1.updated_at, datetime.datetime)
        self.assertIsInstance(self.city1.state_id, str)

    def test_save(self):
      
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_functions(self):
       
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
     
        self.assertTrue(hasattr(self.city1, 'name'))
        self.assertTrue(hasattr(self.city1, 'id'))
        self.assertTrue(hasattr(self.city1, 'created_at'))
        self.assertTrue(hasattr(self.city1, 'updated_at'))
        self.assertTrue(hasattr(self.city1, 'state_id'))

    def test_to_dict(self):
       
        my_model_json = self.city1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.city1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.city1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.city1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.city1.id)

    def test_unique_id(self):
  
        city2 = self.city1.__class__()
        city3 = self.city1.__class__()
        city4 = self.city1.__class__()
        self.assertNotEqual(self.city1.id, city2.id)
        self.assertNotEqual(self.city1.id, city3.id)
        self.assertNotEqual(self.city1.id, city4.id)


if __name__ == '__main__':
    unittest.main()
