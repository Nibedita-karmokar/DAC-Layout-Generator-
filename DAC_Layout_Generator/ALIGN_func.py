#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:27:57 2022

@author: nibeditakarmokar
"""

import Cap_Layout_Generation

import json

cap_array_gen=Cap_Layout_Generation.capGenerator('layers.json')
list1=[]

input_string = input("Enter a list element separated by space: ")
list1 = list(map(int,input_string.split()))

circuit_type='Binary'
if circuit_type=='Binary':
    Placement_type='Spiral'
    cap_array_gen.cap_gen('test.json', list1, circuit_type, Placement_type)

if circuit_type=='Split':
    Placement_type='Spiral'
    cap_array_gen.cap_gen('test.json', list1, circuit_type, Placement_type)
