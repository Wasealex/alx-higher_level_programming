#!/usr/bin/python3
def text_indentation(text):
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
