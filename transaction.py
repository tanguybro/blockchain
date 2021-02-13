# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:47:13 2021

@author: Tanguy
"""

class Transaction:
        
    def __init__(self, sender, recipient, amount): 
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
