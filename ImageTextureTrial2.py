# Link to the code from StackExchange: https://blender.stackexchange.com/questions/157531/blender-2-8-python-add-texture-image

#Import python
import bpy
from bpy import context, data, ops


mat = bpy.data.materials.new(name="New_Mat")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load("C:\\Users\\satna\\OneDrive\\Desktop\\Programming\\Python\\Blender\\Blender-World-Generator\\DirtBlock.png")
mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

ob = context.view_layer.objects.active

# Assign it to object
if ob.data.materials:
    ob.data.materials[0] = mat
else:
    ob.data.materials.append(mat)

