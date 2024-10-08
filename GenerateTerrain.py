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
                location = (x, y, -z)

                # Add the cubes. k
                bpy.ops.mesh.primitive_cube_add(size = size, location = location, scale = (size, size, size))
                
                # Set the newly created cube as the active object. 
                activeObject = bpy.context.active_object

                # Create the material (if the material already exists, then skip)
                groundMaterial = createMaterial(0.027325, 0.450766, 0.080214, 1)
                assignMaterial(activeObject, groundMaterial)

# Function to create the tree. 
def buildTree():
    # Getting a random position on top of the row of cubes.
    treeXPos = random.randint(0, xNum - 1)
    treeYPos = random.randint(0, yNum - 1)
    treeZPos = z 
    treeTrunkHeight = random.randint(3, 5)

    # Variables for the leaves
    leavesSize = (size * treeTrunkHeight) / 2
    leavesXPosition = treeXPos
    leavesYPosition = treeYPos
    leavesZPosition = treeTrunkHeight + leavesSize

    # Add a single block as the location of the tree stump.
    # Loop through the treeheight to add a new cube as a chunk of the trunk. Add colour to the trunk. 
    counter = 1
    while counter <= treeTrunkHeight:
        # Create the cube at that position.
        bpy.ops.mesh.primitive_cube_add(size = size, location = (treeXPos, treeYPos, treeZPos), scale = (size, size, size))
        # Save the active object
        activeObject = bpy.context.active_object
        # Increase the z position by 1 for the next iteration
        treeZPos += 1
        # Set the colour.
        treeTrunkColour = createMaterial(0.195465, 0.020193, 0.004988, 1)
        assignMaterial(activeObject, treeTrunkColour)
        # Increase the counter. 
        counter += 1

    # Create the leaves of the tree. 
    createLowPolyLeaves(leavesSize, leavesXPosition, leavesYPosition, leavesZPosition)

# Function to make the low poly leaves for the tree.
def createLowPolyLeaves(size, xPosition, yPosition, zPosition):
    bpy.ops.mesh.primitive_cube_add(size = size, location = (xPosition, yPosition, zPosition), scale = (size, size, size))
    activeObject = bpy.context.active_object
    colourOfLeaves = createMaterial(0.007951, 0.349087, 0.0003, 1)
    assignMaterial(activeObject, colourOfLeaves)
    return activeObject

# Function to add a material to the selected object.
def assignMaterial(object, material):
    if object and object.data:
        material.use_nodes = True
        object.data.materials.append(material)

# Function to create a new material
def createMaterial(red, green, blue, alpha):
    material = bpy.data.materials.new(name=f"Material_{len(bpy.data.materials)}")
    material.use_nodes = True
    material.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (red, green, blue, alpha)
    return material

# Calling the functions: 
cleanScene()
spawnGround()
buildTree()