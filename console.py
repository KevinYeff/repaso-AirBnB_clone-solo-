#!/usr/bin/python3
#Contributor: Kevin Yeff Espinoza Salguedo

"""Program console 0.0.1 that uses the cmd module"""
import cmd

class HBNBCommand(cmd.Cmd):
    
    """Class that will be the entry point of the command interpreter""" 

    prompt = "(hbnb )"
    
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
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
    