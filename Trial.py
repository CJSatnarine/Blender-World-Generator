import bpy;

size = 1;
x = y = z = size / 2;

bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));
#z = 1.5;
#bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#x 
for i in range(15):
    x += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#Z
for i in range(15): 
    z += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));

#y    
for i in range(15):
    y += size;
    bpy.ops.mesh.primitive_cube_add(size = size, location = (x, y, z));
