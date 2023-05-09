#Imports.
import bpy;
import bmesh;

# Variables: 
# Size of each cube.
size = 1;  
# Setting the x, y, and z positions.
x = y = z = size / 2;  
# Setting the number of cubes in each coordinate. 
xNum = 1;
yNum = 1;
zNum = 1;
# Setting the initial value for the number of cubes in each recursive call. 
cubeCount = 0;
# Setting the maximum amount of cubes that is needed to be created. 
numOfCubes = xNum * yNum * zNum;
# print(numOfCubes);

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

                # Object View Layer variable. 
                activeObjectViewLayer = bpy.context.view_layer.objects.active;

                # Add a new material slot. 
                # bpy.ops.object.material_slot_add();

                # Creating a new material and assigning it to the active cube. 
                material = bpy.data.materials.new("Material");
                material.use_nodes = True;
                BSDF = material.node_tree.nodes["Principled BSDF"];
                materialNodes = material.node_tree.nodes;
                materialLinks = material.node_tree.links;

                # Add the material.  
                activeObject.data.materials.append(material);

                # Selecting each face and then assigning the material to that face. 
                for i in range(6): 
                    # Checks if the object is currently in edit mode, and if not, sets it into edit mode. 
                    if (bpy.context.active_object.mode != "EDIT"):
                        bpy.ops.object.editmode_toggle();
                    
                    bm = bmesh.from_edit_mesh(activeObject.data);

                    # Make sure the bmesh is up-to-date with the mesh data.
                    bm.faces.ensure_lookup_table();
                    
                    # Set selecting the faces to be true. 
                    bm.faces[i].select = True;

                    # Show the updates in the viewport. 
                    bmesh.update_edit_mesh(activeObject.data);
                    print('Face ', i, ' grabbed');

                    # Appened the material to the face. 
                    # bpy.ops.object.material_slot_assign({'object': activeObject});
                    # bpy.ops.transform.translate(value=(0.169302, 0, 0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False);

                    # Deselect the faces. 
                    bm.faces[i].select = False;
                    print('Face ', i, ' released');                

                # Change the texture of the cube. 
                textureImage = material.node_tree.nodes.new('ShaderNodeTexImage');
                textureImage.image = bpy.data.images.load("C://Users//satna//OneDrive//Desktop/Programming//Python//Blender//Blender-World-Generator//DirtBlock.png");
                material.node_tree.links.new(BSDF.inputs['Base Color'], textureImage.outputs['Color']);

                # Assign the texture to the object. 
                if activeObjectViewLayer.data.materials:
                    activeObjectViewLayer.data.materials[0] = material;
                else: 
                    activeObjectViewLayer.data.materials.append(material);

# Calling the functions: 
cleanScene();
spawnGround();
print('Code has run.');