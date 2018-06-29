#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:07:51 2018

@author: danielr
"""
import hashlib
import random

class Block:
    def __init__(self,contract,prevBlock = None):
        self.object = contract
        self.objectType = contract.getType()
        self.data = contract.getHashableData()
        self.HashAlg =  hashlib.sha3_256()
        if prevBlock:
            self.prevHash = self.HashPrev(prevBlock)
        else:
            pass
    
    def HashPrev(self,prevBlock):
        self.HashAlg.update(prevBlock.getData())
        return self.HashAlg.hexdigest()
    
    def getData(self):
        return self.data
        
    def getPrevHash(self):
        return self.prevHash
    


