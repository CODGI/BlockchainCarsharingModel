#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 20:32:54 2018

@author: danielr
"""
from Hashable import Hashable
#import random
#import string
#import hashlib


class Fahrzeug(Hashable):
    def __init__(self, ID, desc, owner):
        self.ID = ID
        self.desc = desc
        self.owner = owner
    
    def getType(self):
        return "Fahrzeug"
    
    def getHashableData(self):
        s = self.ID+self.desc+self.owner
        return s.encode('utf-8')
    
    def UnlockForUser():
        pass

#PubKeyOwner = "".join(random.SystemRandom().choice("0123456789abcdef") for _ in range(100))
#ID = "".join(random.SystemRandom().choice("0123456789abcdef") for _ in range(100))
#Desc = "".join(random.SystemRandom().choice(string.ascii_letters + \
#               string.ascii_lowercase+string.ascii_uppercase + " " + ".") for _ in range(1000))
#F = Fahrzeug(ID,Desc,PubKeyOwner)
#HD = F.getHashableData()
#m=hashlib.sha3_512()
#m.update(HD)
#print(m.hexdigest())


