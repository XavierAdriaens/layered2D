#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:12:26 2019

@author: xavier
"""
layerList = ["heart", "lung", "rib", "muscle", "abdomen"];
V_tagList = [1,2,3,4,5];
S_tagList = [11,12,13,14,15];

def inclusionsOf(layer):
    return {
        "heart": [],
        "lung": ["heart"],
        "rib": ["lung"],
        "muscle": ["rib"],
        "abdomen": ["muscle"]
    }[layer]

