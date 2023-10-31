#!/usr/bin/python3
"""a module for text indentation func"""


def text_indentation(text):
    """a func for adding 2 new lines after '.?:' chars
    Args:
        text: the text string
    Raises:
        TypeError: if the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for tok in ".?:":
        text_list = []
        for row in text.split(tok):
            text_list.append(row.strip(' '))

        text = (tok + '\n\n').join(text_list)

    print(text, end='')


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
