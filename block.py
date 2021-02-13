# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:44:09 2021

@author: Tanguy
"""

from time import time
import json
import hashlib

class Block(dict):
    
    def __init__(self, index, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash
        
    
    """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
    """
    def calculate_hash(self):
        block_string = json.dumps(self, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()