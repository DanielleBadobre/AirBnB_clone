import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up the City instance for testing"""
        self.city = City()

    def test_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes_exist(self):
        """Test that City has the required attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attributes_type(self):
        """Test that the attributes are of the correct type"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_default_attributes(self):
        """Test the default values of the attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def tearDown(self):
        """Clean up after each test"""
        del self.city


if __name__ == "__main__":
    unittest.main()
