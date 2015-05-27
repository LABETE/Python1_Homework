#!/usr/local/bin/python3
"""Refactoring program..."""

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(str_title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    new_title = str_title.title()
    index_word = 0
    for word in small_words:
        if word in new_title[1:].lower():
            new_title = new_title.replace(" " + word.title() + " "," " + word + " ")
    
    return new_title 
    

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()