import os
import maya.cmds as cmds

#import and assign env var to in-script variable
assetName = str(os.getenv('ASSET_NAME'))

print(assetName)

#define function that generates a group based on env variable asset name (GRP_<ASSET>)
def createGroup():    
    groupName = ('GRP_'+ assetName)
    
    #check if the group already exists    
    if cmds.objExists(groupName):
        print('This group already exists dumbass')
        return
    #if not, continue...    
    else: 
        selectedObject = cmds.ls(sl=True)
        
        #create GRP_<ASSET> group
        grp_MASTER= cmds.group( em=True, name=(groupName))    
     
        #create child groups GRP_geom and GRP_rig
        grp_GEO= cmds.group(em= True, name='GRP_geo')
        grp_RIG= cmds.group(em= True, name='GRP_rig')
        cmds.parent(grp_GEO, grp_MASTER)
        cmds.parent(grp_RIG, grp_MASTER)
        cmds.parent(selectedObject, grp_GEO)

createGroup()


#define a function that generates three locators (probably with slight offsets)
#name appropriately
def placeLocators():
    locRoot = cmds.spaceLocator(p=(0,0,0), n='LOC_root')
    locBase = cmds.spaceLocator(p=(0,1,0), n='LOC_base')
    locMove = cmds.spaceLocator(p=(0,2,0), n='LOC_move')
    
    #function that generates joints at locator locations
    def placeJoints(locRoot, locBase, locMove):          
        position = cmds.xform(locRoot, query=True, ws=True, translation=True)
        rootJoint = cmds.joint(p=position)
        cmds.parent(rootJoint, world=True)
        cmds.rename(rootJoint, 'Root_jnt')
        
        position = cmds.xform(locBase, query=True, ws=True, translation=True)
        baseJoint = cmds.joint(p=position)      
        #cmds.parent(baseJoint, rootJoint)
        cmds.rename(baseJoint, 'Base_jnt')
        
        position = cmds.xform(locMove, query=True, ws=True, translation=True)
        moveJoint = cmds.joint(p=position)
        #cmds.parent(moveJoint, baseJoint)
        cmds.rename(moveJoint, 'Move_jnt')
        
    #JOINTS NOT GENERATING AT LOCATOR POSITIONS, FIX!
    placeJoints(locRoot, locBase, locMove)


placeLocators()
   
#define a function that creates a joint hierarchy using the locators as reference
    #check if joints already exist for this mesh/meshes
        #if yes
            #prompt the user "Are you sure you want to move joints to current locator positions?" y/n
            #move existing joints to locators            

"""
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
#btn = cmds.button(label='Bind Skin',align='center',  command=bindSkin, parent=layout)
cmds.showWindow();
"""