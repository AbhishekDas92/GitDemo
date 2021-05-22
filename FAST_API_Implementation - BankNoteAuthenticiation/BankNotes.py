# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:31:44 2020

@author: abhis
"""

from pydantic import BaseModel
#2. Class which describes Bank Notes measurement

class BankNote(BaseModel):
    
    varience : float
    skewness : float
    curtosis : float
    entropy  : float
    
    