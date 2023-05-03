import bpy;

# Variables: 
# Size of each cube.
size = 1;  
# Setting the x, y, and z positions.
x = y = z = size / 2;  
# Setting the number of cubes in each coordinate. 
xNum = 1;
yNum = 3;
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

# Function to recursively spawn the cubes to create the ground. 
def spawnGroundRecursively(count):
    if count < numOfCubes: 
        location = (x, y, z);
        bpy.ops.mesh.primitive_cube_add(size = size, location = location, scale = (size, size, size));
        activeObjectRecursive = bpy.context.active_object;
        # location += 1;
    else: 
        print(count);
        # x += 1;
        # y += 1;
        # z += 1;
        location = (x + 1, y + 1, x + 1);
        spawnGroundRecursively(count + 1);

# ChatGPT's method: 
def addCube(x, y, z, size, material):
    bpy.ops.mesh.primitive_cube_add(size=size, location=(x, y, z));
    cube = bpy.context.active_object;
    cube.data.materials.append(material);

# Set up material.
material = bpy.data.materials.new("Material")
material.use_nodes = True
materialNodes = material.node_tree.nodes
materialLinks = material.node_tree.links
materialNodes['Principled BSDF'].inputs['Base Color'].default_value = (1.0, 0.47, 1.0, 1.0)

# Generate the cubes recursively. 
def addCubesRecursively(x, y, z, size, material, num_cubes):
    if num_cubes == 0:
        return
    addCube(x, y, z, size, material);
    for i in range(1, num_cubes):
        addCubesRecursively(x + i*size, y, z, size, material, num_cubes - 1);
        addCubesRecursively(x, y + i*size, z, size, material, num_cubes - 1);
        addCubesRecursively(x, y, z + i*size, size, material, num_cubes - 1);
        for j in range(1, num_cubes):
            addCubesRecursively(x + i*size, y + j*size, z, size, material, num_cubes - 1);
            addCubesRecursively(x + i*size, y, z + j*size, size, material, num_cubes - 1);
            addCubesRecursively(x, y + i*size, z + j*size, size, material, num_cubes - 1);
            for k in range(1, num_cubes):
                addCubesRecursively(x + i*size, y + j*size, z + k*size, size, material, num_cubes - 1);

# Call the methods. 
cleanScene(); 
# spawnGroundRecursively(cubeCount);
addCubesRecursively(x, y, z, size, material, max(xNum, yNum, zNum));
print('works lmao');

# Notes: 
# - Not very fast. I need to impliment recursion in a better way. 