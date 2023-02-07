#!/usr/bin/python3
import sys
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
