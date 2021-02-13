# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:30:19 2021

@author: Tanguy
"""

from block import Block
from transaction import Transaction

class Blockchain(object):
    
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(0, 0) # Create the genesis block     
        
        
    @property
    def last_block(self):
        return self.chain[-1]
        
    
    """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
    """
    def new_block(self, proof, previous_hash=None):
        block = Block(len(self.chain) + 1, 1, previous_hash or self.chain[-1].calculate_hash())
        self.chain.append(block)
    
    
    """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
    """
    def new_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)


