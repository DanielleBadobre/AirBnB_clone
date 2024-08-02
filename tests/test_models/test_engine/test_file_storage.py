import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up test environment."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test that all() returns the __objects dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new() adds an object to __objects."""
        self.storage.new(self.model)
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save() properly saves objects to file."""
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test that reload() correctly loads objects from file."""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
