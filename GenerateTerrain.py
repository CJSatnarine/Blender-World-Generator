#Imports.
import bpy;

# Variables: 
# Size of each cube.
size = 1;  
# Setting the x, y, and z positions.
x = y = z = size / 2;  
# Setting the number of cubes in each coordinate. 
xNum = 5;
yNum = 5;
zNum = 1;
# Setting the initial value for the number of cubes in each recursive call. 
cubeCount = 0;
# Setting the maximum amount of cubes that is needed to be created. 
numOfCubes = xNum * yNum * zNum;

#Function to clean the scene. This removes all of the objects, collections, materials, particles, textures, images, curves, meshes, actions, nodes, and worlds from the scene. 
def cleanScene():
    # Changes the mode to object mode if it is in Edit mode. 
    if (bpy.context.active_object and bpy.context.active_object.mode == "EDIT"):
        bpy.ops.object.editmode_toggle();
        
    # Checks for hidden stuff and unhides them.     
    for obj in bpy.data.objects: 
        obj.hide_set(False);
        obj.hide_select = False;
        obj.hide_viewport = False;
        
    # Selects all the objects and then deletes.     
    bpy.ops.object.select_all(action = "SELECT");
    bpy.ops.object.delete();

# Function to spawn the "ground" by creating several cubes using a nested for loop. 
def spawnGround():  
    # Iterate over each grid "cell" we want a cube at.
    for x in range(xNum):
        for y in range(yNum):
            for z in range(zNum): 
                # Set the location. 
                location = (x, y, z);

                # Add the cubes. 
                bpy.ops.mesh.primitive_cube_add(size = size, location = location, scale = (size, size, size));
                # Set the newly created cube as the active object. 
                activeObject = bpy.context.active_object;
                
                # Creating a new material and assigning it to the active cube. 
                material = bpy.data.materials.new("Material");
                material.use_nodes = True;
                materialNodes = material.node_tree.nodes;
                materialLinks = material.node_tree.links;
                
                activeObject.data.materials.append(material);

                # Change the base colour. 
                materialNodes['Principled BSDF'].inputs['Base Color'].default_value = (0.056, 0.439, 0.059, 1.0); 
# Function to spawn trees on the grass. 
def spawnTree():
    print("Tree has spawned.");

# Calling the functions: 
cleanScene();
spawnGround();
spawnTree;

# Shows that the code ran. 
print("The code ran.");

# Notes: 
# - For loop for the grid: 
#        - x is for creating cubes in the x axis. 
#        - y is for creating cubes in the y axis. 
#        - z is for creating cubes in the z axis. 
# - I need to add the materials to the cubes and somehow save it in the Blender program. 
# - I need to replace the nested for loop with a recursive function to spawn the ground. 
# - I need to add a function to create a tree in a random position. This function will create cubes and put them in a way to look like a tree. It will also assign the correct materials to their proper cubes. 
# - I need to find a way to create creat and assign a single material to all the respective cubes. 
# - I need to find a way to select every single face of the cube and then just add the image texture to them. 
