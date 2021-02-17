#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version
    of html validation by checking whether every
    opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    # HINT:
    # use the _extract_tags function below to
    # generate a list of html tags without any extra text;
    # then process these html tags using
    # the balanced parentheses algorithm from the class/book
    # the main difference between your code and
    # the code from class will be that you will have
    # to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    taggies = _extract_tags(html)
    stack = []
    if len(taggies) <= 1 and len(html) > 0:
        return False
    for i in range(len(taggies)):
        if '/' not in taggies[i]:
            stack.append(taggies[i])
        else:
            if len(stack) == 0:
                return False
            if stack[-1][1:] in taggies[i]:
                stack.pop()
            else:
                return False
    return(len(stack)) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions
    that are not meant to be used directly by
    the user are prefixed with an underscore.

    This function returns a list of all the html
    tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    >>> _extract_tags('<strong> ifdsfj </strong>')
    ['<strong>', '</strong>']
    '''
    listy = []
    if '>' not in html:
        return listy
    for i in range(len(html)):
        if html[i] == '<':
            count = 0
            b = i
            while html[b] != '>':
                count += 1
                b += 1
            listy.append(html[i:b + 1])
    return listy
