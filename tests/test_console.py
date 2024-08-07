import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class TestHBNBCommand(unittest.TestCase):

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """Test help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            self.assertIn("Documented commands (type help <topic>):", output)

    def test_empty_line(self):
        """Test empty line command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_no_instance_found(self):
        """Test show command with non-existent ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_no_instance_found(self):
        """Test destroy command with non-existent ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_all_invalid_class(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_class(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_no_instance_found(self):
        """Test update command with non-existent ID"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attr_name(self):
        """Test update command with missing attribute name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with missing value"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234 first_name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_invalid_dict(self):
        """Test update command with invalid dictionary format"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("1234-1234-1234", {"first_name": "Betty", })')
            self.assertEqual(f.getvalue().strip(), "** invalid dictionary format **")

    def test_update_valid_dict(self):
        """Test update command with valid dictionary format"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("1234-1234-1234", {"first_name": "Betty", "age": 18})')
            self.assertIn("** no instance found **", f.getvalue())

    # Tests for BaseModel
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_basemodel(self, mock_stdout):
        """Test create command for BaseModel"""
        HBNBCommand().onecmd("create BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        key = f"BaseModel.{output}"
        self.assertIn(key, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_basemodel(self, mock_stdout):
        """Test show command for BaseModel"""
        obj = BaseModel()
        obj.save()
        HBNBCommand().onecmd(f"show BaseModel {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[BaseModel] ({obj.id})", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_basemodel(self, mock_stdout):
        """Test destroy command for BaseModel"""
        obj = BaseModel()
        obj.save()
        HBNBCommand().onecmd(f"destroy BaseModel {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertNotIn(f"BaseModel.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_basemodel(self, mock_stdout):
        """Test all command for BaseModel"""
        BaseModel().save()
        HBNBCommand().onecmd("all BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn("BaseModel", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_basemodel(self, mock_stdout):
        """Test update command for BaseModel"""
        obj = BaseModel()
        obj.save()
        HBNBCommand().onecmd(f"update BaseModel {obj.id} name 'NewName'")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_basemodel_with_dict(self, mock_stdout):
        """Test update command with dict for BaseModel"""
        obj = BaseModel()
        obj.save()
        update_dict = '{"name": "NewName", "age": 30}'
        HBNBCommand().onecmd(f"update BaseModel {obj.id} {update_dict}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')
        self.assertEqual(obj.age, 30)

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_basemodel(self, mock_stdout):
        """Test count command for BaseModel"""
        BaseModel().save()
        HBNBCommand().onecmd("count BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    # Tests for User
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_user(self, mock_stdout):
        """Test create command for User"""
        HBNBCommand().onecmd("create User")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        key = f"User.{output}"
        self.assertIn(key, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user(self, mock_stdout):
        """Test show command for User"""
        obj = User()
        obj.save()
        HBNBCommand().onecmd(f"show User {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[User] ({obj.id})", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_user(self, mock_stdout):
        """Test destroy command for User"""
        obj = User()
        obj.save()
        HBNBCommand().onecmd(f"destroy User {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertNotIn(f"User.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_user(self, mock_stdout):
        """Test all command for User"""
        User().save()
        HBNBCommand().onecmd("all User")
        output = mock_stdout.getvalue().strip()
        self.assertIn("User", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_user(self, mock_stdout):
        """Test update command for User"""
        obj = User()
        obj.save()
        HBNBCommand().onecmd(f"update User {obj.id} email 'newemail@example.com'")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.email, 'newemail@example.com')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_user_with_dict(self, mock_stdout):
        """Test update command with dict for User"""
        obj = User()
        obj.save()
        update_dict = '{"email": "newemail@example.com", "name": "NewName"}'
        HBNBCommand().onecmd(f"update User {obj.id} {update_dict}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.email, 'newemail@example.com')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_user(self, mock_stdout):
        """Test count command for User"""
        User().save()
        HBNBCommand().onecmd("count User")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    # Tests for State
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state(self, mock_stdout):
        """Test create command for State"""
        HBNBCommand().onecmd("create State")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        key = f"State.{output}"
        self.assertIn(key, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_state(self, mock_stdout):
        """Test show command for State"""
        obj = State()
        obj.save()
        HBNBCommand().onecmd(f"show State {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[State] ({obj.id})", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_state(self, mock_stdout):
        """Test destroy command for State"""
        obj = State()
        obj.save()
        HBNBCommand().onecmd(f"destroy State {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertNotIn(f"State.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_state(self, mock_stdout):
        """Test all command for State"""
        State().save()
        HBNBCommand().onecmd("all State")
        output = mock_stdout.getvalue().strip()
        self.assertIn("State", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_state(self, mock_stdout):
        """Test update command for State"""
        obj = State()
        obj.save()
        HBNBCommand().onecmd(f"update State {obj.id} name 'NewName'")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_state_with_dict(self, mock_stdout):
        """Test update command with dict for State"""
        obj = State()
        obj.save()
        update_dict = '{"name": "NewName"}'
        HBNBCommand().onecmd(f"update State {obj.id} {update_dict}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_state(self, mock_stdout):
        """Test count command for State"""
        State().save()
        HBNBCommand().onecmd("count State")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    # Tests for City
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_city(self, mock_stdout):
        """Test create command for City"""
        HBNBCommand().onecmd("create City")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        key = f"City.{output}"
        self.assertIn(key, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_city(self, mock_stdout):
        """Test show command for City"""
        obj = City()
        obj.save()
        HBNBCommand().onecmd(f"show City {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[City] ({obj.id})", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_city(self, mock_stdout):
        """Test destroy command for City"""
        obj = City()
        obj.save()
        HBNBCommand().onecmd(f"destroy City {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertNotIn(f"City.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_city(self, mock_stdout):
        """Test all command for City"""
        City().save()
        HBNBCommand().onecmd("all City")
        output = mock_stdout.getvalue().strip()
        self.assertIn("City", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_city(self, mock_stdout):
        """Test update command for City"""
        obj = City()
        obj.save()
        HBNBCommand().onecmd(f"update City {obj.id} name 'NewName'")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_city_with_dict(self, mock_stdout):
        """Test update command with dict for City"""
        obj = City()
        obj.save()
        update_dict = '{"name": "NewName"}'
        HBNBCommand().onecmd(f"update City {obj.id} {update_dict}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_city(self, mock_stdout):
        """Test count command for City"""
        City().save()
        HBNBCommand().onecmd("count City")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    # Tests for Amenity
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_amenity(self, mock_stdout):
        """Test create command for Amenity"""
        HBNBCommand().onecmd("create Amenity")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        key = f"Amenity.{output}"
        self.assertIn(key, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_amenity(self, mock_stdout):
        """Test show command for Amenity"""
        obj = Amenity()
        obj.save()
        HBNBCommand().onecmd(f"show Amenity {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[Amenity] ({obj.id})", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_amenity(self, mock_stdout):
        """Test destroy command for Amenity"""
        obj = Amenity()
        obj.save()
        HBNBCommand().onecmd(f"destroy Amenity {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertNotIn(f"Amenity.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_amenity(self, mock_stdout):
        """Test all command for Amenity"""
        Amenity().save()
        HBNBCommand().onecmd("all Amenity")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Amenity", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_amenity(self, mock_stdout):
        """Test update command for Amenity"""
        obj = Amenity()
        obj.save()
        HBNBCommand().onecmd(f"update Amenity {obj.id} name 'NewName'")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_amenity_with_dict(self, mock_stdout):
        """Test update command with dict for Amenity"""
        obj = Amenity()
        obj.save()
        update_dict = '{"name": "NewName"}'
        HBNBCommand().onecmd(f"update Amenity {obj.id} {update_dict}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_amenity(self, mock_stdout):
        """Test count command for Amenity"""
        Amenity().save()
        HBNBCommand().onecmd("count Amenity")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    # Tests for Place
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place(self, mock_stdout):
        """Test create command for Place"""
        HBNBCommand().onecmd("create Place")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        key = f"Place.{output}"
        self.assertIn(key, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_place(self, mock_stdout):
        """Test show command for Place"""
        obj = Place()
        obj.save()
        HBNBCommand().onecmd(f"show Place {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[Place] ({obj.id})", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_place(self, mock_stdout):
        """Test destroy command for Place"""
        obj = Place()
        obj.save()
        HBNBCommand().onecmd(f"destroy Place {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertNotIn(f"Place.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_place(self, mock_stdout):
        """Test all command for Place"""
        Place().save()
        HBNBCommand().onecmd("all Place")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Place", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_place(self, mock_stdout):
        """Test update command for Place"""
        obj = Place()
        obj.save()
        HBNBCommand().onecmd(f"update Place {obj.id} name 'NewName'")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_place_with_dict(self, mock_stdout):
        """Test update command with dict for Place"""
        obj = Place()
        obj.save()
        update_dict = '{"name": "NewName"}'
        HBNBCommand().onecmd(f"update Place {obj.id} {update_dict}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.name, 'NewName')

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_place(self, mock_stdout):
        """Test count command for Place"""
        Place().save()
        HBNBCommand().onecmd("count Place")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

    # Tests for Review
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_review(self, mock_stdout):
        """Test create command for Review"""
        HBNBCommand().onecmd("create Review")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)
        key = f"Review.{output}"
        self.assertIn(key, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_review(self, mock_stdout):
        """Test show command for Review"""
        obj = Review()
        obj.save()
        HBNBCommand().onecmd(f"show Review {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(f"[Review] ({obj.id})", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_review(self, mock_stdout):
        """Test destroy command for Review"""
        obj = Review()
        obj.save()
        HBNBCommand().onecmd(f"destroy Review {obj.id}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertNotIn(f"Review.{obj.id}", storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_review(self, mock_stdout):
        """Test all command for Review"""
        Review().save()
        HBNBCommand().onecmd("all Review")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Review", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_review(self, mock_stdout):
        """Test update command for Review"""
        obj = Review()
        obj.save()
        HBNBCommand().onecmd(f"update Review {obj.id} text 'NewReviewText'")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.text, 'NewReviewText')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_review_with_dict(self, mock_stdout):
        """Test update command with dict for Review"""
        obj = Review()
        obj.save()
        update_dict = '{"text": "NewReviewText"}'
        HBNBCommand().onecmd(f"update Review {obj.id} {update_dict}")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '')
        self.assertEqual(obj.text, 'NewReviewText')

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_review(self, mock_stdout):
        """Test count command for Review"""
        Review().save()
        HBNBCommand().onecmd("count Review")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '1')

if __name__ == '__main__':
    unittest.main()

