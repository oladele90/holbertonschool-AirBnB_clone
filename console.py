#!/usr/bin/python3
"""console module/ entry point for command interpreter"""
import sys
import cmd
from models.base_model import BaseModel 
import models
from datetime import datetime


models_list = ["BaseModel"]

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
        if args in models_list:
            obj = eval(args)()
            models.storage.new(obj)
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not (args):
            print("** class name missing **")
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
        if args[0] not in models_list:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items()
                if args[1] == value.id:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on class name and id"""

        if not (args):
            print("** class name missing **")
        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
        if args[0] not in models_list:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if args[1] == value.id:
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances"""

        split_args = args.split()
        new_list = []
        dict_json = models.storage.all()
        if args:
            try:
                for key in models.storage.all():
                    if split_args[0] == key.split('.')[0]:
                        new_list.append(str(dict_json))
                print(new_list)
            except Exception:
                print("** class doesn't exist **")
        else:
            for kein module.storage.all():
                new_list.append(str(models.storage.all()[key]))
            print(new_list)
            

    def 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
