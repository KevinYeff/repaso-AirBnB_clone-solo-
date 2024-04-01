"""Function to parse a cmdli argument ver 0.0.1"""


def int_or_float_or_string(arg):
    """
    Function to parse a cmdli argument ver 0.0.1
    :param arg: cmdli argument
    :return: parsed argument with the correct type value
    """
    if isinstance(arg, str):
        if arg.isdigit():
            return int(arg)
        else:
            if "." in arg:
                parameters = arg.split(".")
                if parameters[0].isdigit() and parameters[1].isdigit():
                    return float(arg)
                else:
                    return arg
