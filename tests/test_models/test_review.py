#!/usr/bin/python3
""" unit test module for review class"""
import unittest
import os
from models.base_model import BaseModel
from models.review import Review
import pep8


class TestReview(unittest.TestCase):
    """ test cases for the Review model"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "Best class"

    @classmethod
    def teardown(cls):
        """removes instance at the end of the test"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """chekcing if review have attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_place_id(self):
        """ test for review place_id attr type"""
        self.assertEqual(type(self.rev.place_id), str)

    def test_user_id(self):
        """ test for review user_id attr type"""
        self.assertEqual(type(self.rev.user_id), str)

    def test_text(self):
        """ test for review text attr type"""
        self.assertEqual(type(self.rev.text), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', 'NO FILE')
    def test_save_Review(self):
        """test if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
