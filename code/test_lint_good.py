#!/usr/bin/env python

def foo(test_str: str) -> bool:
    if test_str:
        return True
    else:
        return False

if __name__ == "__main__":
    foo("hello")
