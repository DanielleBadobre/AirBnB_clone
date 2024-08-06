#!/usr/bin/python3
""" console
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interprete """
    prompt = '(hbnb)'
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, class_name):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id """
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based on the
        class name and id """
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return
        if arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        key = arguments[0] + '.' + arguments[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the
        change into the JSON file). """
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return
        if arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        key = arguments[0] + '.' + arguments[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, class_name=None):
        """ Prints all string representation of all instances based or not on
        the class name """
        if class_name:
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in storage.all().items()
                         if key.startswith(class_name + '.')]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)"""
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return
        if arguments[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        key = arguments[0] + '.' + arguments[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arguments) == 2:
            print("** attribute name missing **")
            return
        if len(arguments) == 3:
            print("** value missing **")
            return
        instance = storage.all()[key]
        attr_name = arguments[2]
        attr_value = arguments[3]
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_quit(self, args):
        """ exits """
        exit()

    def do_EOF(self, args):
        """ exit with eof """
        print()
        exit()

    def emptyline(self):
        """ do nothing when empty line """
        pass

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("Exits programm without formatting\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
