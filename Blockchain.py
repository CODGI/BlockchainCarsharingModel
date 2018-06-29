#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 19:08:40 2018

@author: danielr
"""

from Block import Block

class Blockchain:
    
    def __init__(self, origin):
        self.Blocks = [origin]
        self.HighestBlock = origin
        self.HighestBlockIndex = 0
    
    def AddBlock(self,B):
        self.Blocks.append(B)
        self.HighestBlock = B
        self.NumberOfBlocks += 1
    
    def SearchHash(self, Hash):
        pass
    
    def SearchInData(self, Hash):
        pass
        