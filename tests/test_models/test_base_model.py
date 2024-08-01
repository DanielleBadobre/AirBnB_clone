#!/usr/bin/python3
"""
Base Model tests
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """tests base model """
    def setUp(self):
        """ set up tests """
        self.model = BaseModel()

    def testId(self):
        """ test that id is string """
        self.assertIsInstance(self.model.id, str)
        self.assertTrue(len(self.model.id) > 0)

    def testUuid(self):
        """ test if uuid is unique """
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def testCreatedAt(self):
        """ tests if created_at is datetime object """
        self.assertIsInstance(self.model.created_at, datetime)

    def testUpdatedAt(self):
        """ tests if updated at is datetime object """
        self.assertIsInstance(self.model.updated_at, datetime)

    def testStr(self):
        """ tests the str method """
        expectedStr = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expectedStr)

    def testSave(self):
        """ tests save method """
        oldUpdatedAt = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, oldUpdatedAt)
        self.assertTrue(self.model.updated_at > oldUpdatedAt)

    def testToDictMethod(self):
        """Test to_dict method"""
        modelDict = self.model.to_dict()
        self.assertIsInstance(modelDict, dict)
        self.assertEqual(modelDict['__class__'], 'BaseModel')
        self.assertEqual(modelDict['id'], self.model.id)
        self.assertIsInstance(modelDict['created_at'], str)
        self.assertIsInstance(modelDict['updated_at'], str)
        self.assertEqual(modelDict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(modelDict['updated_at'],
                         self.model.updated_at.isoformat())

    def testInitKwargs(self):
        """Tests if init creates from kwargs"""
        modelDict = self.model.to_dict()
        recreatedModel = BaseModel(**modelDict)
        self.assertEqual(recreatedModel.id, self.model.id)
        self.assertEqual(recreatedModel.created_at.isoformat(),
                         self.model.created_at.isoformat())
        self.assertEqual(recreatedModel.updated_at.isoformat(),
                         self.model.updated_at.isoformat())
        self.assertEqual(recreatedModel.__class__.__name__,
                         self.model.__class__.__name__)
        self.assertIsInstance(recreatedModel.created_at, datetime)
        self.assertIsInstance(recreatedModel.updated_at, datetime)

    def testInitNoKwargs(self):
        """ Tests if init creates without kwargs"""
        newModel = BaseModel()
        self.assertIsInstance(newModel.id, str)
        self.assertIsInstance(newModel.created_at, datetime)
        self.assertIsInstance(newModel.updated_at, datetime)
        self.assertNotEqual(newModel.id, self.model.id)
        self.assertNotEqual(newModel.created_at, self.model.created_at)
        self.assertNotEqual(newModel.updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
