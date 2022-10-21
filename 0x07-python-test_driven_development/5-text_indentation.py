#!/usr/bin/python3
"""This module contain a function that prints a text with new lines"""


def text_indentation(text):
    """text_indentation function that prints text formatted
    depending of the character identified (".", ":", "?")
    Args:
        text (str): parameter to be printed
    """
    special_chars = [".", ":", "?"]
    if type(text) != str:
        raise TypeError("text must be a string")
    # flag to know if the last character was a special character
    last = False
    for i in text:
        if i in special_chars:
            print(i)
            print()
            last = True
        else:
            if last is True and i == " ":
                last = False
                continue
            else:
                print(i, end="")
                last = False
