#Imports.
import bpy;

size = 1;
numOfCubes = 15;
x = y = z = size / 2;

#Add starting cube.
bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#Creating cubes in the X-Position. 
for i in range(numOfCubes):
    x += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#Creating cubes in the Y-Position.    
for i in range(numOfCubes):
    y += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#Creating cubes in the Z-Position.
for i in range(numOfCubes): 
    z += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));
