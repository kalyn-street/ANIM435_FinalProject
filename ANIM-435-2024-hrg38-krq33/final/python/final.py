import os
import maya.cmds as cmds

# Import and assign env var to in-script variable
assetName = str(os.getenv('ASSET_NAME'))

print(f'Environment varibale is "{assetName}".')

# Assign selected object to variable (add code that yells at user if they have nothing selected)
selectedObject = cmds.ls(sl=True)

# Check if an object is selected, do not allow main script to run if not
if not selectedObject:
    cmds.confirmDialog(title='Error', message='No object selected. Please select an object to proceed.', button='OK')
    selectedObject = None
    executeScript = False
else:
    executeScript = True


# Determine points of locators
if selectedObject:
    bbox = cmds.exactWorldBoundingBox(selectedObject)
    minX, minY, minZ, maxX, maxY, maxZ = bbox
    center_pos = [(minX + maxX) / 2, (minY + maxY) / 2, (minZ + maxZ) / 2]
    bottom_pos = [(minX + maxX) / 2, minY, (minZ + maxZ) / 2]
    top_pos = [(minX + maxX) / 2, maxY, (minZ + maxZ) / 2]

# UI Stuff!!!
def createWin():
    # Check if a window already exists. If yes, delete it
    if cmds.window('rigObject', exists=True):
        cmds.deleteUI('rigObject')
    
    # Create a new window with a larger size
    cmds.window('rigObject', title='Rig Object', widthHeight=(400, 250))
    
    # Define the layout of the window
    winLayout = cmds.columnLayout(adjustableColumn=True, rowSpacing=10, columnAlign="center")
    
    #check if main script is allowed to run (is an object selected?)
    if executeScript == False:
        return
    
    # Function to create a group based on env variable asset name (GRP_<ASSET>)
    def createGroup(*args):    
        groupName = ('GRP_' + assetName)
        
        # Check if the group already exists    
        if cmds.objExists(groupName):
            cmds.confirmDialog(title='Warning', message='This group already exists. Please delete it or move on to the next step.', button='OK')
            return
        else:
            # Create GRP_<ASSET> group
            grp_MASTER = cmds.group(em=True, name=groupName)
            
            # Create child groups GRP_geom and GRP_rig
            grp_GEO = cmds.group(em=True, name='GRP_geom')
            grp_RIG = cmds.group(em=True, name='GRP_rig')
            cmds.parent(grp_GEO, grp_MASTER)
            cmds.parent(grp_RIG, grp_MASTER)
            cmds.parent(selectedObject, grp_GEO)
    
    # Function to place locators
    def placeLocators(*args):
        #check if locators exist already
        if cmds.objExists('LOC_root'):
            cmds.confirmDialog(title='Warning', message='The locator "LOC_root" already exists. Please delete it to continue.', button='OK')
            return
        elif cmds.objExists('LOC_base'):
            cmds.confirmDialog(title='Warning', message='The locator "LOC_base" already exists. Please delete it to continue.', button='OK')
            return
        elif cmds.objExists('LOC_move'):
            cmds.confirmDialog(title='Warning', message='The locator "LOC_move" already exists. Please delete it to continue.', button='OK')
            return
        
        # generate locators with transforms defined by the bounding box of the selected object (locators can still be moved around)   
        locRoot = cmds.spaceLocator(p=bottom_pos, n='LOC_root')
        locBase = cmds.spaceLocator(p=center_pos, n='LOC_base')
        locMove = cmds.spaceLocator(p=top_pos, n='LOC_move')
                
        # Function to create joints
        def placeJoints(*args):
            #yell at user if they don't have locators for some reason
            if not cmds.objExists('LOC_root'):
                cmds.confirmDialog(title='Warning', message='Missing locator "LOC_root". Cannot build rig.', button='OK')
                return
            elif not cmds.objExists('LOC_base'):
                cmds.confirmDialog(title='Warning', message='Missing locator "LOC_base". Cannot build rig.', button='OK')
                return
            elif not cmds.objExists('LOC_move'):
                cmds.confirmDialog(title='Warning', message='Missing locator "LOC_move". Cannot build rig.', button='OK')
                return
            
            # assign position data of locators to variables
            positionRoot = cmds.pointPosition(locRoot, w=True)
            positionBase = cmds.pointPosition(locBase, w=True)
            positionMove = cmds.pointPosition(locMove, w=True)
            
            # check if joint chain exists already, replace with joints at appropriate locations if yes         
            if cmds.objExists('JNT_root'):
                cmds.delete('JNT_root')
                cmds.select(d=True)
                rootJoint = cmds.joint(p=positionRoot)
                cmds.rename(rootJoint, 'JNT_root')
                cmds.select(d=True)
                
                #cmds.delete('JNT_base')
                baseJoint = cmds.joint(p=positionBase)
                cmds.rename(baseJoint, 'JNT_base')
                cmds.select(d=True)
                
                #cmds.delete('JNT_move')
                moveJoint = cmds.joint(p=positionMove)
                cmds.rename(moveJoint, 'JNT_move')
                                 
            else:
                # create them jawns
                cmds.select(d=True)
                rootJoint = cmds.joint(p=positionRoot)
                cmds.rename(rootJoint, 'JNT_root')
                cmds.select(d=True)
                
                baseJoint = cmds.joint(p=positionBase)
                cmds.rename(baseJoint, 'JNT_base')
                cmds.select(d=True)
                
                moveJoint = cmds.joint(p=positionMove)
                cmds.rename(moveJoint, 'JNT_move')
                
            #parent joints appropriately
            cmds.parent('JNT_root', 'GRP_rig')
            cmds.parent('JNT_base', 'JNT_root')
            cmds.parent('JNT_move', 'JNT_base')            
            print('Rig build successful.')

        # Function that binds the mesh to the rig
        def bindSelected(*args):
            if not selectedObject:
                cmds.confirmDialog(title='Error', message='No object selected. Please select an object to proceed.', button='OK')
                return
            
            jointChain = cmds.listRelatives('JNT_root', ad=True)
            cmds.bindSkin(selectedObject, jointChain, ta=True)
            print("Skin bind successful.")
        

        # Add "create joints" and "bind skin" buttons in the window layout
        cmds.button(label='Build Rig', command=placeJoints, parent=winLayout)
        cmds.button(label='Bind', command=bindSelected, parent=winLayout)
        print('Done!')
        
        
    # Create group button
    cmds.button(label='Create Group', command=createGroup, parent=winLayout)
    
    # Place locators button
    cmds.button(label='Place Locators', command=placeLocators, parent=winLayout)

    # Add a space to separate buttons for better visual clarity
    cmds.separator(height=10, parent=winLayout)

    # Show the window
    cmds.showWindow('rigObject')

# Call the function to create the window
createWin()