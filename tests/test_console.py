import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

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

if __name__ == '__main__':
    unittest.main()
