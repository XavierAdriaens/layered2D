#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:08:46 2019

@author: xavier
"""
import gmsh
import sys
from readPointsFromFile import readPointsFromFile
from Input.hierarchy import layerList, V_tagList, S_tagList, inclusionsOf

pxlSize = 0.33e-3; #real size of a pixel [m]
h=0.005; #mesh size

gmsh.initialize(sys.argv)
gmsh.model.add("thorax2D")

for idx,layer in enumerate(layerList):
    pointList = readPointsFromFile(layer+".txt",h,pxlSize)
    pointList.append(pointList[0]) #Close the curve
    pointList.reverse() #Reorder the point so that normal are along z and tangents are right handed
    gmsh.model.geo.addSpline(pointList,S_tagList[idx])
    gmsh.model.addPhysicalGroup(1,[S_tagList[idx]],S_tagList[idx])
    gmsh.model.geo.addCurveLoop([S_tagList[idx]],S_tagList[idx]) #CurveLoop have the same tag than splines
    
    S_inclusionsTagList = [S_tagList[idx]];
    for inclusion in inclusionsOf(layer):
        S_inclusionsTagList.append(S_tagList[layerList.index(inclusion)]);
    gmsh.model.geo.addPlaneSurface(S_inclusionsTagList,V_tagList[idx])
    gmsh.model.addPhysicalGroup(2,[V_tagList[idx]],V_tagList[idx])
    
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(1)
gmsh.model.mesh.generate(2)

gmsh.write("Output/thorax2D.msh")
gmsh.fltk.run()
gmsh.finalize()