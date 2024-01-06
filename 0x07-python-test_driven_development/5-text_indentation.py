#!/usr/bin/python3
"""
    this module is 5-text_indentation

    it has one function, text_indentation()
    it gets a string and prints out a split strings after '?', ':', '.',
"""


def text_indentation(text):
    """
       function text_indentation takes one argument and prints out
       splitted string to a new line after punctionation marks['?', ':', '.']
    Args:
         text(str) = the only parameter
    Return:
           None
    Output:
           splited strings
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indented_text = ""
    delimeter = ['?', ':', '.']
    skip_next = False
    for idx in range(len(text)):
        if skip_next:
            if text[idx] == ' ':
                continue
            skip_next = False
        indented_text += text[idx]
        if text[idx] in delimeter and idx < len(text) - 1:
            if text[idx + 1] == ' ':
                skip_next = True
            indented_text += '\n\n'
    print(indented_text)
