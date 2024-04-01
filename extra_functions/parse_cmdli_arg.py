#!/usr/bin/python3
# Contributor: Kevin Yeff Espinoza Salguedo

"""Function to parse a cmdli argument ver 0.0.2"""


def int_or_float_or_string(arg):
    """
    Function to parse a cmdli argument ver 0.0.2
    :param arg: cmdli argument
    :return: parsed argument with the correct type value
    """
    if isinstance(arg, str):
        if arg.isdigit():
            return int(arg)
        elif arg.startswith('-') and "." not in arg:
            return int(arg)
        else:
            parameters = arg.split(".")
            if parameters[0].isdigit() and parameters[1].isdigit():
                return float(arg)
            elif parameters[0].startswith("-") and parameters[1].isdigit():
                return float(arg)
            else:
                # if arg is not int or float return the arg
                return arg.strip('"')
    # return the arg without any changes
    return arg