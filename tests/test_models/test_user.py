import unittest
from models.user import User
from models.base_model import BaseModel
import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up the User instance for testing"""
        self.user = User()

    def test_inheritance(self):
        """Test that User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes_exist(self):
        """Test that User has the required attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes_type(self):
        """Test that the attributes are of the correct type"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_default_attributes(self):
        """Test the default values of the attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        """Test the string representation of the User instance"""
        string_representation = str(self.user)
        self.assertIn("[User]", string_representation)
        self.assertIn(self.user.id, string_representation)

    def test_save(self):
        """Test that save method updates the updated_at attribute"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def tearDown(self):
        """Clean up after each test"""
        del self.user


if __name__ == "__main__":
    unittest.main()
