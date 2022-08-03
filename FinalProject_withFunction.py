# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 16:04:18 2022

@author: brianne
"""
# this script extracts hydrologic units that intersect a 
# target county (selected from a statewide shapefile of all counties)
# from a DEM, performs Hillshade and Slope operations,
# and projects all output rasters in a specified coordinate system

import arcpy
import os
# import custom module
import FinalProjectModule

# import data files
dataWS = r'E:\PSU\GEOG485\FinalProject'
countyShapefile = dataWS + r'\OregonSpatialData\orcntypoly.shp'
hydroUnits = dataWS + r'\OregonSpatialData\WDB_Oregon_State_GDB.gdb\WBDHU8'
DEM = dataWS + r'\OregonSpatialData\OR_DEM_10m.gdb\DEM_10meter_Oregon'
countyLabel = 'altName'
targetCounty = 'Lane'

# create output folder for HUs and set it as the workspace
os.mkdir(dataWS + r'\CountyHydroUnits')
arcpy.env.workspace = dataWS + r'\CountyHydroUnits'
arcpy.env.overwriteOutput = True

# set preferred projection to a Spatial Reference object
SR = arcpy.SpatialReference(2992)

# create and set output folder for rasters
os.mkdir(dataWS + r'\HURasterOutput')
rasterOutput = dataWS + r'\HURasterOutput'

try:
    # iterate through HUs in list for remaining operations
    FinalProjectModule.countyHUIntersection(countyShapefile, countyLabel, targetCounty, hydroUnits, arcpy.env.workspace)
    
    # Put HU polygons into a list
    HUList = arcpy.ListFeatureClasses()
    
    # iterate through HUs in list for remaining operations
    FinalProjectModule.HURasterOperations(HUList, SR, DEM, rasterOutput)

except:
    print (arcpy.GetMessages())