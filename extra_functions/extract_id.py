#!/usr/bin/python3
# Contributor: Kevin Yeff Espinoza Salguedo
import re
"""Function to parse id from an arg ver 0.0.1"""


def id_parser(arg):
    """
    Function to parse a id from parameter ver 0.0.1
    :param arg: parameter that contains id
    :var pattern: regex for the arg
    :return: parsed args with the correct command
    :inital example input: "246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
    """
    if arg:
        # define regex
        pattern = r'("([^"*\,\s{}]*)")((?:\)))'
        # if there are coincidences
        coincidences = re.match(pattern, arg)
        if coincidences:
            # extract the id
            coincidence = coincidences[2]
            # return the string cotaining the id
            return coincidence
    else:
        # otherwise do nothing
        return None
