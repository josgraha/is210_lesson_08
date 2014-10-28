#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08 task 03."""
import time


class Snapshot(object):
    """A timestamp holder.  Instantiate to set the timestamp.

    Args:
    None

    Attributes:
       created: holds time.time() timestamp when object was created.
    """
    def __init__(self):
        """Default constructor.

        """
        self.created = time.time()
