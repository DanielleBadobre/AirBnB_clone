import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up the Amenity instance for testing"""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes_exist(self):
        """Test that Amenity has the required attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attributes_type(self):
        """Test that the attributes are of the correct type"""
        self.assertIsInstance(self.amenity.name, str)

    def test_default_attributes(self):
        """Test the default values of the attributes"""
        self.assertEqual(self.amenity.name, "")

    def tearDown(self):
        """Clean up after each test"""
        del self.amenity


if __name__ == "__main__":
    unittest.main()
