#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:45:37 2018

@author: danielr
"""

class Network:
    def __init__(self):
        self.Users = []
    
    def registerUser(self, user):
        self.Users.append(user)
        
    def sendMessage(self, PubKeyRec, PubKeyOrig, message):
        for u in self.Users:
            if u.getRSAPubKey == PubKeyRec:
                u.receiveMessage(PubKeyOrig, message)
                break