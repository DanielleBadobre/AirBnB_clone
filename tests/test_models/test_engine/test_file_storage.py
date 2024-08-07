import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        self.model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

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

    def test_serialization_deserialization(self):
        """Test serialization and deserialization of all new classes."""
        models = [self.model, self.user, self.state, self.city, self.amenity,
                  self.place, self.review]
        for model in models:
            self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        for model in models:
            key = f"{type(model).__name__}.{model.id}"
            self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
