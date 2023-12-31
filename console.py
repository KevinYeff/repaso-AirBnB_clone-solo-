#!/usr/bin/python3
# Contributor: Kevin Yeff Espinoza Salguedo

"""Program console 0.0.1 that uses the cmd module"""
import cmd
import models
from models.base_model import BaseModel
from models import classes, storage


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
        parameters = arg.split()
        if not arg:
            print("** class name missing **")
        elif parameters[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[parameters[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """This method will print the string representation of an
        instance based on the class name and id 
        EX: show BaseModel 12121212"""
        parameters = arg.split()
        if not arg:
            print("** class name is missing **")
        elif parameters[0] not in classes:
            print("** class doesn't exists **")
        elif len(parameters) == 1:
            print("** instance id missing **")
        else:
            classAndId = f"{parameters[0]}.{parameters[1]}"
            if classAndId in storage.all():
                print(storage.all()[classAndId])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id and save the change in to the JSON file
        EX: destroy BaseModel 121212"""
        parameters = arg.split()
        if not arg:
            print("** class name missing **")
        elif parameters[0] not in classes:
            print("** class doesn't exist **")
        elif len(parameters) == 1:
            print("** instance id missing **")
        else:
            classAndId = f"{parameters[0]}.{parameters[1]}"
            if classAndId not in storage.all():
                print("** no instance found **")
            else:
                instances = storage.all()
                del instances[classAndId]
                storage.save()

    def do_all(self, arg):
        """this method prints all string representation of all
        instances based or no in the class name
        EX: all BaseModel or all"""
        instances = storage.all()
        if not arg:
            for values in instances.values():
                print([str(values)])
        elif arg in classes:
            for values in instances.values():
                if isinstance(values, BaseModel)\
                        and values.__class__ == classes[arg]:
                    print([str(values)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """This method updates an instance based on the class name and
        id by adding or updating a attribute 
        EX:update BaseModel 121212 email <"aibnb@mail.com"> """
        parameters = arg.split()

        if not arg:
            print("** class name missing **")

        elif parameters[0] not in classes:
            print("** class doesn't exist **")

        elif len(parameters) == 1:
            print("** instance id missing **")

        elif len(parameters) == 2:
            clsAndId = f"{parameters[0]}.{parameters[1]}"
            if clsAndId not in storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(parameters) == 3:
            print("** value missing **")
        else:
            instances = storage.all()
            clsAndId = f"{parameters[0]}.{parameters[1]}"
            instance = instances[clsAndId]
            setattr(instance, parameters[2], parameters[3])
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
