#!/usr/bin/python3

"""An interactive shell?"""

import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Interactive command for HBNB project"""
    prompt = '(hbnb)  '

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        return cmd.Cmd.emptyline(self)

    def do_create(self, args):
        """Creates a new instance of BaseModel

            Args:
                arg(line):  BaseModel command
        """
        args_split = args.split()

        if (len(args_split) == 0):
            print("** class name missing **")
            return 0
        elif (args_split[0] != "BaseModel"):
            print("** class doesn't exist **")
            return 0
        else:
            objInstance = eval(args_split[0])()
            objInstance.save()
            print(objInstance.id)

    def do_show(self, args):
        """Prints the string representation of an instance 
            based on the class name and id

            Args:
                arg(line)
        """
        args_split = args.split()
        cls_name = args_split[0]
        cls_id = args_split[1]
        cls_nameId = cls_name + "." + cls_name
        all_objs = FileStorage.storage.all()

        if (len(args_split) == 0):
            print("** class name missing **")
        elif (cls_name != "BaseModel"):
            print("** class doesn't exist **")
        elif (cls_name == "BaseModel" and len(args_split) < 2):
            print("** instance id missing **")
        elif():
            pass
        else:
            print(eval(cls_id))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
