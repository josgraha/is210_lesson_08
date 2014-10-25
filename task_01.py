#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08 task 01."""

import data

# Create two instances of the Produce() class
# The first should not be passed any constructor variables and should be assigned to a variable named TOMATO
TOMATO = data.Produce()

# The next should be named EGGPLANT and the constructor should be passed the value of 1311210802
EGGPLANT = data.Produce(1311210802)

# Access the arrival attribute of TOMATO and save it to a variable named TOMATO_ARRIVAL
TOMATO_ARRIVAL = TOMATO.arrival

# Call the get_expiration() method of EGGPLANT and save its result to a variable named, EGGPLANT_EXPIRE
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()