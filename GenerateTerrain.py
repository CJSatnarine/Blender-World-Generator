#Imports.
import bpy
import random

# Size of each cube.
size = 1
# Setting the x, y, and z positions.
x = y = z = size
# Setting the number of cubes in each coordinate. 
xNum = 10
yNum = 10
zNum = 1

#Function to clean the scene. This removes all of the objects, collections, materials, particles, textures, images, curves, meshes, actions, nodes, and worlds from the scene. 
def cleanScene():
    # Changes the mode to object mode if it is in Edit mode. 
    if (bpy.context.active_object and bpy.context.active_object.mode == "EDIT"):
        bpy.ops.object.editmode_toggle()
        
    # Checks for hidden stuff and unhides them.     
    for obj in bpy.data.objects: 
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False
        
    # Selects all the objects and then deletes.     
    bpy.ops.object.select_all(action = "SELECT")
    bpy.ops.object.delete()

# Function to spawn the "ground" by creating several cubes using a nested for loop. 
def spawnGround(): 
    # Iterate over each grid "cell" we want a cube at.
    for x in range(xNum):
        for y in range(yNum):
            for z in range(zNum): 
                # Set the location. 
                location = (x, y, z)

                # Add the cubes. 
                bpy.ops.mesh.primitive_cube_add(size = size, location = location, scale = (size, size, size))
                
                # Set the newly created cube as the active object. 
                activeObject = bpy.context.active_object

                # Create the material (if the material already exists, then skip)
                groundMaterial = createMaterial(0.027325, 0.080214, 0.450766, 1) #Colour input is: red, blue, green, alpha
                assignMaterial(activeObject, groundMaterial)

# Function to add a material to the selected object.
def assignMaterial(object, material):
    if object and object.data:
        material.use_nodes = True
        object.data.materials.append(material)

# Function to create a new material
def createMaterial(red, blue, green, alpha):
    material = bpy.data.materials.new(name=f"Material_{len(bpy.data.materials)}")
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (red, green, blue, alpha)
    return material

# Function to create the tree. 
def buildTree():
    # Getting a random position on top of the row of cubes.
    treeXPos = random.randint(0, xNum - 1)
    treeYPos = random.randint(0, yNum - 1)
    treeZPos = z + 0.5

    bpy.ops.mesh.primitive_cube_add(size = size, location = (treeXPos, treeYPos, treeZPos), scale = (size, size, size))


# Calling the functions: 
cleanScene()
spawnGround()
buildTree()

# Shows that the code ran. 
print("The code ran to the end successfully.")