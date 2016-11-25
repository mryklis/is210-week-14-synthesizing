#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""list comprehension example"""


import task_01


def fibo(count):
    """fibonacci sequece in list comprehension

    Args:
        count (int): numbers in sequence

    Returns:
        list of fibonacci sequence

    Example:
        >>> fibo(5)
        [0, 1, 1, 2, 3]

    """

    return[num for num in task_01.xfibo(count)]
