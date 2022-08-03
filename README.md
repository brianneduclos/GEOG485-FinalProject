# GEOG485-FinalProject
My final project for GEOG 485, GIS Programming and Software Development at Penn State University.

This tool takes a statewide DEM, clips it to 12-digit hydrologic units that intersect a county border, creates hillshade and slope rasters, and projects those rasters into a state standard projection. Included here are a Python script and an ArcGIS Pro script tool. 

The files are:

FinalProjectModule: module containing the functions used in both the script and the ArcGIS Pro Script tool
FinalProject_withFunction: script that runs operation calling the FinalProjectModule
FinalProject_forScriptTool_withFunction: script for ArcGIS Pro tool that calls the FinalProjectModule
FinalProject.tbx: Toolbox containing the tool "Calculate Hillshade and Slope of Hydrologic Units"
