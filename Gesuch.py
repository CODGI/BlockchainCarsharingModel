#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:38:26 2018

@author: danielr
"""

from Hashable import Hashable
import random
import string

class Gesuch (Hashable):
    def __init__(self,owner):
        self.owner = owner
        self.desc = "".join(random.SystemRandom().choice(string.ascii_letters + \
               string.ascii_lowercase+string.ascii_uppercase + " " + ".") for _ in range(1000))
        
    def getHashableData(self):
        s = self.desc
        return s.encode('utf-8')
        
    def getType(self):
        return "Gesuch"