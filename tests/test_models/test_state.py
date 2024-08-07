import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up the State instance for testing"""
        self.state = State()

    def test_inheritance(self):
        """Test that State inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes_exist(self):
        """Test that State has the required attributes"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_attributes_type(self):
        """Test that the attributes are of the correct type"""
        self.assertIsInstance(self.state.name, str)

    def test_default_attributes(self):
        """Test the default values of the attributes"""
        self.assertEqual(self.state.name, "")

    def tearDown(self):
        """Clean up after each test"""
        del self.state


if __name__ == "__main__":
    unittest.main()
