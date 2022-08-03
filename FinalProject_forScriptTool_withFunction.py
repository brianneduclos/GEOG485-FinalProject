# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:11:35 2022

@author: brianne
"""
# this script tool extracts hydrologic units that intersect a 
# target county (selected from a statewide shapefile of all counties)
# from a DEM, performs Hillshade and Slope operations,
# and projects all output rasters in a specified coordinate system

import arcpy
arcpy.env.overwriteOutput = True
# import custom module
import FinalProjectModule

try: 
    # import data files
    # statewide county shapefile
    countyShapefile = arcpy.GetParameterAsText(0)
    # statewide hydrologic units
    hydroUnits = arcpy.GetParameterAsText(1)
    # statewide DEM
    DEM = arcpy.GetParameterAsText(2)
    # specify target county label in Attribute table
    countyLabel = arcpy.GetParameterAsText(3)
    # specify target county name
    targetCounty = arcpy.GetParameterAsText(4)
    
    # set workspace folder to output file for hydrologic units and rasters
    # (must be an empty folder)
    arcpy.env.workspace = arcpy.GetParameterAsText(5)
    
    # set preferred projection to a Spatial Reference object
    SR = arcpy.GetParameterAsText(6)
    
    # set output folder for rasters
    outputFolder = arcpy.GetParameterAsText(7)
    
    # iterate through HUs in list for remaining operations
    FinalProjectModule.countyHUIntersection(countyShapefile, countyLabel, targetCounty, hydroUnits, arcpy.env.workspace)
    
    # Put HU polygons into a list
    HUList = arcpy.ListFeatureClasses()
    
    # iterate through HUs in list for remaining operations
    FinalProjectModule.HURasterOperations(HUList, SR, DEM, outputFolder)

except:
    print (arcpy.GetMessages())