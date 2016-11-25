#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci generator module"""


def xfibo(count):
    """fibonacci sequence generator

    Args:
        count (int): the number of numbers to produce

    Returns
        fibonacci sequence of numbers

    Example:
    >>> for i in xfibo(5):
    ...     print i
    0
    1
    1
    2
    3

    """

    lastnum, currentnum = 0, 1
    counter = 0
    while counter < count:
        yield lastnum
        lastnum, currentnum = currentnum, lastnum + currentnum
        counter += 1
