import maya.cmds as cmds
import os

#import and assign env var to in-script variable

#define function that generates a group based on env variable asset name (GRP_<ASSET>)
    #check if group already exists for specified asset
        #return if yes
        #tell user "GRP_<ASSET> already exists
    
    #create GRP_<ASSET> group
        
    #create child groups GRP_geom and GRP_rig
    
    #if not geometry selected
        #return, prompt user to select geometry
    #else
        #move geometry into GRP_geom
        #tell user "geo moved into group"


#define a function that generates three locators (probably with slight offsets)
    #name appropriately


#define a function that creates a joint hierarchy using the locators as reference
    #check if joints already exist for this mesh/meshes
        #if yes
            #prompt the user "Are you sure you want to move joints to current locator positions?" y/n
            #move existing joints to locators
        #if no
            #prompt the user "Are you sure you want to generate joints at these locations? y/n
            #generate new joints at locators
            

#define a function that binds the mesh to the rig
    #prompt the user "Are you sure you want to bind skin? y/n
    

#connect functions to buttons...      