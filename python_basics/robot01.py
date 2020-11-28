#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg

class Robot:

    def act(self, game):

        #Move to the center board
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        