# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:26:45 2022

@author: brianne
"""
import arcpy
from arcpy.sa import *
import os

def countyHUIntersection(allcounties, countyTableLabel, targetCounty, hydroUnits, outWorkspace):
    # Select 8 digit HUs that intersect Lane County and make them individual layers
    # Select Lane County from county polygon
    ctyWhereClause = countyTableLabel + " = '" + targetCounty + "'"
    ctyFC = arcpy.SelectLayerByAttribute_management(allcounties, 'NEW_SELECTION', ctyWhereClause)
    # Extract each intersecting HU into individual polygons
    # place HU polygons into empty workspace folder to create list in next step
    intersectingHUs = arcpy.SelectLayerByLocation_management(hydroUnits, 'INTERSECT', ctyFC)
    arcpy.SplitByAttributes_analysis(intersectingHUs, outWorkspace, 'HUC8')
    

def HURasterOperations(HUList, SR, DEM, outputFolder):
    # Check out Spatial Analyst extension
    arcpy.CheckOutExtension("Spatial")

    for HU in HUList:
        # mask polygon out of DEM and save the file
        HUname = HU.split('.')
        filename = HUname[0] + '.tif'
        print('masking ' + HUname[0] + ' out of DEM')
        arcpy.AddMessage('masking ' + HUname[0] + ' out of DEM')
        DEMmask = ExtractByMask(DEM, HU)   
        outpath = os.path.join(outputFolder, filename)
        print('projecting ' + HUname[0])
        arcpy.AddMessage('projecting ' + HUname[0])
        arcpy.DefineProjection_management(DEMmask, SR)
        DEMmask.save(outpath)
        print(HUname[0] + ' DEM mask saved as ' + outpath)
        arcpy.AddMessage(HUname[0] + ' DEM mask saved as ' + outpath)
        # Hillshade
        print('running hillshade for ' + HUname[0])
        arcpy.AddMessage('running hillshade for ' + HUname[0])
        HUHillshade = Hillshade(outpath)
        hillshadeFilename = HUname[0] + 'Hillshade.tif'
        hillshadeOutpath = os.path.join(outputFolder, hillshadeFilename)
        print('projecting hillshade ' + HUname[0])
        arcpy.AddMessage('projecting hillshade ' + HUname[0])
        arcpy.DefineProjection_management(HUHillshade, SR)
        HUHillshade.save(hillshadeOutpath)
        print(HUname[0] + ' hillshade saved as ' + hillshadeOutpath)
        arcpy.AddMessage(HUname[0] + ' hillshade saved as ' + hillshadeOutpath)
        # Slope
        print('running slope for ' + HUname[0])
        arcpy.AddMessage('running slope for ' + HUname[0])
        HUSlope = Slope(outpath)
        slopeFilename = HUname[0] + 'Slope.tif'
        slopeOutpath = os.path.join(outputFolder, slopeFilename)
        print('projecting slope ' + HUname[0])
        arcpy.AddMessage('projecting slope ' + HUname[0])
        arcpy.DefineProjection_management(HUSlope, SR)
        HUSlope.save(slopeOutpath)
        print(HUname[0] + ' slope saved as ' + slopeOutpath)
        arcpy.AddMessage(HUname[0] + ' slope saved as ' + slopeOutpath)
        
    # Check in Spatial Analyst extension
    arcpy.CheckInExtension("Spatial")
        