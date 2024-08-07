import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up the Review instance for testing"""
        self.review = Review()

    def test_inheritance(self):
        """Test that Review inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes_exist(self):
        """Test that Review has the required attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_attributes_type(self):
        """Test that the attributes are of the correct type"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_default_attributes(self):
        """Test the default values of the attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def tearDown(self):
        """Clean up after each test"""
        del self.review


if __name__ == "__main__":
    unittest.main()
