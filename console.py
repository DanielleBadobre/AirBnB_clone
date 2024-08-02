#!/usr/bin/python3
""" console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ contains the entry point of the command interprete """
    prompt = '(hbnb)'

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
