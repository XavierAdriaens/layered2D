#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:32:14 2019

@author: xavier
"""
import gmsh

def readPointsFromFile(fileName,h,scaling):
    """Create gmsh points from a structured file containing the x and y coordinates of each point.

    Parameters:
    fileName (str): structured file containing the x and y coordinates of each point
    h (float): mesh size around each point
    scaling (float): scaling applied to the coordinates

    Returns:
    list(int): list containing the tag of each created point
    """
    f = open("Input/center.txt",'r');
    next(f);
    fields = f.readline().split();
    center = [float(fields[1]),float(fields[2])];
        
    pointList = [];
    f = open("Input/"+fileName,'r');
    next(f)
    for line in f:
        fields = line.split()
        p=gmsh.model.geo.addPoint( (float(fields[1])-center[0])*scaling,(float(fields[2])-center[1])*scaling, 0.0,h)
        pointList.append(p)
    return pointList;
