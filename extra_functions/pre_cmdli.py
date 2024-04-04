#!/usr/bin/python3
# Contributor: Kevin Yeff Espinoza Salguedo
from .exract_id import id_parser
"""Function to parse a cmdli command ver 0.0.2"""


def pre_cmd(arg):
    """
    Function to parse a cmdli command ver 0.0.2
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
        # if there are more chars that just ")"
        if len(parameters[1]) > 1 and parameters[1][0] != ")":
            # extract the id for the class
            id_for_cls = id_parser(parameters[1])
            # return <cmd> <cls> <id>
            return f"{format} {id_for_cls}"
        else:
            # return the (previous) command formatted
            return format
    else:
        return None
