#Imports.
import bpy;

size = 1;
xNumOfCubes = 3;
yNumOfCubes = 2;
zNumOfCubes = 0;

x = y = z = size / 2;

#Creating the inital cube. 
bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#I need to create an algorithm that will create the cubes in the shape of a block. 

#Creating cubes in the X-Position.   
for i in range(xNumOfCubes):
    x += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#Creating cubes in the Y-Position. 
for i in range(yNumOfCubes):
    y += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#Creating cubes in the Z-Position.
for i in range(zNumOfCubes): 
    z += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));