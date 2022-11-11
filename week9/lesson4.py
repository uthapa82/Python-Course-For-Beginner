def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name.

    Args:
        first : String
        last : String
    """ 
    if middle:
        full_name = first + ' ' + middle + ' ' + last 
    else:
        full_name = first + ' ' + last
    return full_name.title()

