# ANIM435_FinalProject
Repo for Procedural Rigging Tool Project
TITLE: PROCEDURAL RIGGING TOOL
AUTHOR: Kalyn Street and Hailey Gerhart

INTRODUCTION:
Welcome to our PROCEDURAL RIGGING TOOL. This tool will place a selected object in a group, place locators on this object, and create joints at the position of those locators. In addition, the user can bind the selected geometry to those created joints. The purpose of this tool is to quickly set up rigs for props. The name of the master group is set in congruence with an environment variable. This means your shell must be configured correctly before running Maya.

PROGRAMS YOU WILL USE:
VisCode or similar, Git Bash or similar, and Maya(This was written with Maya 2024)

TABLE OF CONTENTS:
1) Setup environment function
2) Define variables in shell
3) Run Rigging Tool in Maya
4) Warning Messages

GUIDE
1) SETUP ENVIRONMENT FUNCTION
Add a configurable env variable function in your shell's aliases.sh file. Mine looks like this:

[ALIASES.SH opened with VISCODE]
final(){
	export ASSET_NAME ="$1"
	echo "$1"	
}

2) DEFINE VARIABLES IN SHELL
Then, run your shell. Call the function you created and assign the ASSET_NAME variable a temporary name. Then, run Maya from the shell so it will read the new environment. I'll be calling my rig Steve. I am using an alias so '$ maya' will do. Here's what my shell looks like:

[GIT BASH]
Owner@DESKTOP-4P8R08B MINGW64 ~
$ final Steve
Steve

Owner@DESKTOP-4P8R08B MINGW64 ~
$ maya [HIT ENTER]

3) RUN FINAL.PY IN MAYA
Next, switch over to Maya, and open final.py. Import or create the geometry you want to rig. Run the script. Before pressing any of the two visible buttons, select the geo. Then hit 'Create Group.' Then, press press 'Place Locators.' Three locators will appear at the top, center, and bottom of your object. Two more buttons will become visible. Hit 'Build Rig' and you'll see a chain of joints appear where the locators are. Then, with your geo selected, press "Bind". Now your geo will have a basic skin bind with the joint chain 

4) WARNINGS
The script will deliver a warning if you attempt to complete a step with an improper setup: 
For example, if you attempt to run the script with nothing selected, it will prompt you to choose an object first. You only have to select an object once at the beginning. The script will remember the object throughout the execution of the code.

If you press the 'Create Group' button after a group has already been created in the scene, the script will not generate a second group, but instead prompt you to either delete the existing group or press a different button.

The 'Place Locators' button will tell you which locators already exist in the scene, and prompt you to delete them before generating any new ones.

The 'Build Rig' button won't work if you are missing any locators.


CLOSING:
This concludes the guide to our code. We are glad we stepped out of our comfort zone and did something rigging-related. We learned about different position query methods as well as the importance of staying organized when functions nest into each other. In the future we'd like to learn about applying for-in loops to have a more adjustable rigging pipeline. 