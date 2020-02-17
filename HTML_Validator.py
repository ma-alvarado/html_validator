#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.
top[2:]top[2:]
    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    balanced = True
    mylist = []
    for tag in _extract_tags(html):
        if "/" not in tag:
            mylist.append(tag)
        else:
            if mylist == []:
                return False
            else:
                top = mylist.pop()
                if top[2:] not in tag[1:]:
                    balanced = False
    if balanced and mylist == []:
        return True
    else:
        return False
    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = []
    while len(html) != 0:
        lefttag = html.find("<")
        righttag = html.find(">")

        if lefttag==-1 or righttag==-1:
            break
        
        tags.append(html[lefttag:righttag+1])
        html = html[(righttag+1):]
    return tags
