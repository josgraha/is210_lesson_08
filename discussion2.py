#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 08 discussion 02."""
from television import Televison


class TelevisonOnScreenControls(Television):
    def __init__(self, on_or_off='off', channel='CBS', dvr='empty'):
        """
        default constructor
        :param  on_or_off:
        :param channel:
        :param dvr:
        :return:
        """
        Televison.__init__(self, on_or_off, channel, dvr)
        self.osg_visible = False

    def display_osg(self):
        """
        Displays the on screen guide.
        :return:
        """
        print 'Displaying On Screen Guide'

    def hide_osg(self):
        """
        Hides the on screen guide.
        :return:
        """
        print 'Hiding On Screen Guide'


    def toggle_osg(self, display=False):
        if not display:
            self.osg_visible = False
            self.hide_osg()
            return
        self.osg_visible = True
        self.display_osg()