#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08 task 04."""
import task_02

class Tigerpaw(task_02.Tire):
    """An improved Tire class.

    Args:
        miles (integer): The number of miles on the Tire. Defaults to 0.

    Attributes:
       miles (integer): The number of miles on the Tire.
       _maximum_miles (integer): The total number of miles usable for the Tire.
    """
    __maximum_miles = 750

    def __init__(self, miles=0):
        """Default constructor

        :param miles:
        """
        task_02.Tire(self, miles)
