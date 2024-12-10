import maya.cmds as cmds
import os

#import and assign env var to in-script variable
assetName = os.getenv('ASSET_NAME')

#define function that generates a group based on env variable asset name (GRP_<ASSET>)
def createGroup(*args):
    #check if group already exists for specified asset
        #return if yes
        #tell user "GRP_<ASSET> already exists
    
    #create GRP_<ASSET> group
    grp_MASTER= cmds.group( em=True, name=('GRP_'+ assetName))    
 
    #create child groups GRP_geom and GRP_rig
    grp_GEO= cmds.group(em= True, name='GRP_geo')
    grp_RIG= cmds.group(em= True, name='GRP_rig')
    cmds.parent(grp_GEO, grp_MASTER)
    cmds.parent(grp_RIG, grp_MASTER
    #if not geometry selected
    if not selected_objects:
        #return, prompt user to select geometry
        print("No object selected.")
    #else
    else:
        #move geometry into GRP_geom
        cmds.parent(assetName, grp_GEO)
        #tell user "geo moved into group"
        print("geo moved into group.")

#define a function that generates three locators (probably with slight offsets)
    #name appropriately
def placeLocators(*args): 
    cmds.spaceLocator(p=(0,0,0), n='LOC_root')
    cmds.spaceLocator(p=(0,1,0), n='LOC_base')
    cmds.spaceLocator(p=(0,2,0), n='LOC_move')
    locators= [loc_root, loc_base, loc_move]

    
#define a function that creates a joint hierarchy using the locators as reference
    #check if joints already exist for this mesh/meshes
        #if yes
            #prompt the user "Are you sure you want to move joints to current locator positions?" y/n
            #move existing joints to locators
            for locator in locators:
            if cmds.objExists(locator):
                position = cmds.xform(locator, query=True, worldSpace=True, translation=True)
                cmds.joint( p=(position)
                cmds.rename(joint, locator+'_jnt')
        #if no
            #prompt the user "Are you sure you want to generate joints at these locations? y/n
            #generate new joints at locators
            

#define a function that binds the mesh to the rig
def bindSkin(*args):
    
    #prompt the user "Are you sure you want to bind skin? y/n
    

#connect functions to buttons...
win = cmds.window(title="Procedural Rigging Tool", widthHeight=(200,125)) 
layout =cmds.columnLayout()
cmds.separator(height=12)
btn = cmds.button(label="Create Group", align='center', command=createGroup, parent=layout)
cmds.separator(height=12)
btn = cmds.button(label='Place Locators', align='center', command=placeLocators, parent=layout) 
cmds.separator(height=12)
#btn = cmds.button(label='Build Rig', command=buildRig, parent=layout)
btn = cmds.button(label='Bind Skin',align='center',  command=bindSkin, parent=layout)
cmds.showWindow();      