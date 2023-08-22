#!/usr/bin/python3
# Contributor: Kevin Yeff Espinoza Salguedo

"""Program console 0.0.1 that uses the cmd module"""
import cmd
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """Class that will be the entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Method that exits the program"""
        return (True)

    def do_EOF(self, arg):
        """Secures a clean exit"""
        return True

    def do_help(self, arg: str):
        """Method that gives the user a short description of the 
        commands"""
        return super().do_help(arg)

    def emptyline(self):
        pass
    # New commands

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it in to the 
        JSON file and also prints the id of the instance"""
        # parameters = arg.split()
        if not arg:
            print("** class name missing **")
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """This method will print the string representation of an
        instance based on the class name and id 
        EX: show BaseModel 12121212"""
        parameters = arg.split()
        if not arg:
            print("** class name is missing **")
        elif parameters[0] not in models.classes:
            print("** class doesn't exists **")
        elif len(parameters) == 1:
            print("** instance id missing **")
        else:
            classAndId = f"{parameters[0]}.{parameters[1]}"
            if classAndId in storage.all():
                print(storage.all()[classAndId])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
