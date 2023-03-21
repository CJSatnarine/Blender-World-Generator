#Imports.
import bpy;
import random;

size = 1;

x = y = z = size / 2;

#Creating the inital cube. 
bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

# Iterate over each grid 'cell' we want a cube at. 
for x in range(20):
    for y in range(20):
        #Set the location. 
        location = (x, y, z);

        #Add the cubes. 
        bpy.ops.mesh.primitive_cube_add(size = size, location=location, scale=(1, 1, 1));

##Creating cubes in the X-Position.   
#for i in range(xNumOfCubes):
#    x += size;
#    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

##Creating cubes in the Y-Position. 
#for i in range(yNumOfCubes):
#    y += size;
#    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

##Creating cubes in the Z-Position.
#for i in range(zNumOfCubes): 
#    z += size;
#    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));


#Notes: 
# - There is a cube that spawns amongst the grid that doesn't fit in with the rest.
# - To create the grid to spawn cubes in the z-axis, then I should create a new for loop within the nested loop to take create it in the z-axis. 