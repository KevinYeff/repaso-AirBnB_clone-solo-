#!/usr/bin/python3
# Contributor: Kevin Yeff Espinoza Salguedo

"""Function to parse a cmdli command ver 0.0.1"""


def pre_cmd(arg):
    """
    Function to parse a cmdli command ver 0.0.1
    :param arg: cmdli arguments
    :return: parsed args with the correct command
    :inital example input: BaseModel.all()
    """
    # Verify if arg exists and there is a  dot character
    if arg and "." in arg:
        # split arguments taking dot as a delimiter
        parameters = arg.split(".")
        # save the class
        cls = parameters[0]
        # save the command
        parameters = parameters[1].split("(")
        command = parameters[0]
        # format the correct command
        format = f"{command} {cls}"
        # return the command formatted
        return format
    else:
        return None
