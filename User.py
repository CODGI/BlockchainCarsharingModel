#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:49:44 2018

@author: danielr
"""
import rsa

class User:
    def __init__(self, network):
        (self.RSApubKey, self.RSAprvKey) = rsa.newkeys(1048, poolsize=4)
    
    def getRSAPubKey(self):
        return self.RSApubKey

    def makeProposal(self,Block):
        pass
    
    def receiveMessage(self, PubKeyOrig):
        self.acceptContract(PubKeyOrig)
    
    def acceptContract(self):
        return "Accepted"
    
    def signContract(self):
        pass
    
    def deployContract(self):
        pass