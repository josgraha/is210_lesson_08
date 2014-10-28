#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 08 discussion 01."""
import time
from threading import Thread


class Timer(Thread):
    def __init__(self, owner=None, seconds=0):
        """Default constructor

        :param seconds:
        """
        Thread.__init__(self)
        self.owner = owner
        self.seconds = seconds

    def run(self):
        """
        run the timer and print seconds left
        :return:
        """
        for x in xrange(0, self.seconds):
            print 'seconds left: {}'.format(self.seconds - x)
            # speed up the timer
            time.sleep(.1)
        if self.owner is not None:
            self.owner.timer_complete()


class MicrowaveOven(object):
    """A food heating device.

    Args:
        kilowatts (integer): Device power in watts.

    Attributes:
       kilowatts (integer): The wattage of the oven.
       heating (boolean): True if the device is heating.
    """

    def __init__(self, kilowatts=300):
        """Default constructor.

        :param kilowatts:
        """
        self.kilowatts = kilowatts
        self.heating = False
        self.power_level = 10
        self.seconds_left = 0
        self.timer = None
        self.cb = None

    def add_time(self, minutes=0, seconds=0):
        self.seconds_left = (minutes * 60) + seconds

    def start_oven(self, cb=None):
        """
        Start the oven.
        :return:
        """
        self.heating = True
        self.timer = Timer(self, self.seconds_left)
        self.cb = cb
        self.timer.start()

    def reset(self):
        """
        Resets the oven back to default state.
        :return:
        """
        self.timer = None
        self.heating = False
        self.power_level = 10
        self.seconds_left = 0


    def timer_complete(self):
        """
        Timer callback
        :return:
        """
        print 'food ready!'
        self.reset()
        if self.cb is not None:
            self.cb()


def food_ready():
    print 'heating: {}'.format(mw.heating)
    print 'seconds left: {}'.format(mw.seconds_left)
    print 'power level: {}'.format(mw.power_level)


if __name__ == "__main__":
    mw = MicrowaveOven()
    mw.add_time(0, 30)
    mw.power_level = 5
    print 'heating: {}'.format(mw.heating)
    print 'seconds left: {}'.format(mw.seconds_left)
    print 'power level: {}'.format(mw.power_level)
    mw.start_oven(food_ready)