import os
import maya.cmds as cmds

#import and assign env var to in-script variable
assetName = str(os.getenv('ASSET_NAME'))

print(assetName)

#assign selected object to variable (add code that yells at user if they have nothing selected)
selectedObject = cmds.ls(sl=True)

#UI STUFF!!!
def createWin():
    #check if a window already exists. If yes, delete it
    if cmds.window('rigObject', exists=True):
        cmds.deleteUI('rigObject')
    
    #create a new window
    cmds.window('rigObject', title='Rig Object', widthHeight=(300, 100))
    #define the layout of the window
    cmds.columnLayout(adjustableColumn=True)
    
    #define function that generates a group based on env variable asset name (GRP_<ASSET>)
    def createGroup(*args):    
        groupName = ('GRP_'+ assetName)
        
        #check if the group already exists    
        if cmds.objExists(groupName):
            print('This group already exists dumbass')
            cmds.confirmDialog(title='wanh wanhh', message='This group already exists.')
            return
        #if not, continue...    
        else:
            #create GRP_<ASSET> group
            grp_MASTER= cmds.group( em=True, name=(groupName))    
         
            #create child groups GRP_geom and GRP_rig
            grp_GEO= cmds.group(em= True, name='GRP_geo')
            grp_RIG= cmds.group(em= True, name='GRP_rig')
            cmds.parent(grp_GEO, grp_MASTER)
            cmds.parent(grp_RIG, grp_MASTER)
            cmds.parent(selectedObject, grp_GEO)
            
        #define locator generator function
        def placeLocators(*args):
            locRoot = cmds.spaceLocator(p=(0,0,0), n='LOC_root')
            cmds.xform(locRoot, centerPivots=True)
            
            locBase = cmds.spaceLocator(p=(0,0,0), n='LOC_base')
            cmds.xform(locBase, centerPivots=True)
            
            locMove = cmds.spaceLocator(p=(0,0,0), n='LOC_move')
            cmds.xform(locMove, centerPivots=True)

            #define joint generator function
            def placeJoints(*args):          
                position = cmds.xform(locRoot, query=True, worldSpace=True, translation=True)
                print(position)
                rootJoint = cmds.joint(p=position)
                cmds.parent(rootJoint, world=True)
                cmds.rename(rootJoint, 'Root_jnt')
                
                position = cmds.xform(locBase, query=True, worldSpace=True, translation=True)
                print(position)
                baseJoint = cmds.joint(p=position)      
                cmds.rename(baseJoint, 'Base_jnt')
                
                position = cmds.xform(locMove, query=True, worldSpace=True, translation=True)
                print(position)
                moveJoint = cmds.joint(p=position)
                cmds.rename(moveJoint, 'Move_jnt')
                
                #define a function that binds the mesh to the rig
                def bindSelected(*args):
                    cmds.bindSkin(selectedObject, jointChain, ta=True)
                    print("Skin bind successful.")
        
                #select all children of root joint
                jointChain = cmds.listRelatives('Root_jnt', ad=True)
                print(jointChain)
                
                #"bind skin" button
                cmds.button('Bind rig to selected.', command=bindSelected)
                print('DONE!')
            
            #"create joints" button    
            cmds.button(label='Create joints at locator positions.', command=placeJoints)
            #debugging print statement
            print('create joints?')
        
        #"Generate locators" button
        cmds.button(label='Generate locators.', command=placeLocators)
    
    #"Generate group" button
    cmds.button(label='Generate group.', command=createGroup) 
    
    cmds.showWindow('rigObject')
    
createWin()

"""
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