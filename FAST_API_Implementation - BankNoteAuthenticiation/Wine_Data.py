# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:45:57 2020

@author: abhis
"""

from pydantic import BaseModel

class WinePrediction(BaseModel):
    fixed_acidity : float
    volatile_acidity : float
    citric_acid : float
    residual_sugar  : float
    chlorides : float
    free_sulfur_dioxide : float
    total_sulfur_dioxide : float
    density : float
    pH : float
    sulphates : float
    alcohol : float