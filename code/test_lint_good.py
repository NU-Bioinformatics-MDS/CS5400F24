#!/usr/bin/env python
'''
This is an example of a script that should pass all code linting checks.
'''

def simple_boolean_check(test_str: str) -> bool:
    """ Function that checks the truthiness of a string.

    Args:
        test_str (str): any string

    Returns:
        (bool): whether the string is non-empty.

    Raises:
        ValueError: The test_str is not a string or None
    """
    if isinstance(test_str), str):
        return(bool(test_str))

if __name__ == "__main__":
    simple_boolean_check("passing check")
