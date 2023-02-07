#!/usr/bin/python3
"""console module/ entry point for command interpreter"""
import sys
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


models_list = ["BaseModel", "User", "Place",
               "State", "City", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """
        Some sort of comment here
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        exits console
        """
        raise SystemExit

    def do_EOF(self, args):
        """
        exits console
        """
        raise SystemExit

    def emptyline(self):
        pass

    def do_create(self, args):
        """
        creates a new instance of BaseModel
        """
        if args is None:
            print("** class name missing **")
            return
        if args in models_list:
            obj = eval(args)()
            storage.new(obj)
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not (args):
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in models_list:
            print("** class doesn't exist **")
            return
        else:
            for key, value in storage.all().items():
                if args[1] == value.id:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on class name and id"""

        if not (args):
            print("** class name missing **")
            return
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in models_list:
            print("** class doesn't exist **")
            return
        else:
            for key, value in storage.all().items():
                if args[1] == value.id:
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances"""

        if args not in models_list and len(args) > 0:
            print("** class doesn't exist **")
            return
        if not args:
            for key in storage.all():
                print([str(storage.all()[key])])
        if args in models_list:
            for key in storage.all():
                key1 = key.split(".")[0]
                if key1 == args:
                    print([str(storage.all()[key])])

    def do_update(self, args):
        a_list = args.split(" ")

        if len(a_list) == 0:
            print("** class name missing **")
            return
        if a_list[0] not in models_list:
            print("** class doesn't exist **")
            return
        if len(a_list) == 1:
            print("** instance id missing **")
            return
        if len(a_list) > 1:
            key_1 = ("{}.{}".format(a_list[0], a_list[1]))
            if storage.all().get(key_1) is None:
                print("** no instance found **")
                return
        if len(a_list) == 2:
            print("** attribute name missing **")
            return
        if len(a_list) == 3:
            print("** value missing **")
            return
        if key_1 in storage.all():
            setattr(storage.all()[key_1], a_list[2],
                    a_list[3].strip('\'"'))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
