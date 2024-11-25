win = cmds.window("Create Reference Plane") 
layout = cmds.columnLayout() 
cmds.text(label='Enter Dimensions:')
cmds.text(label='Height')
cmds.floatField('height_field', minValue = 0, maxValue = 5000, value = 0)
cmds.text(label='Width')
cmds.floatField('width_field', minValue = 0, maxValue = 5000, value = 0)
btn = cmds.button(label="Create Plane", command=buttonPressed, parent=layout) 
cmds.showWindow(); 