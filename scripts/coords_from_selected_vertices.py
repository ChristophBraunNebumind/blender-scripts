# from https://blender.stackexchange.com/questions/120593/how-can-i-export-or-print-coordinates-of-each-selected-vertex 
import bpy
import bmesh
import random

# Get the active mesh
obj = bpy.context.edit_object
me = obj.data


# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

bm.faces.active = None

# Modify the BMesh, can do anything here...

with open('C:/Work/blender_test.csv', 'w') as f:
    f.write(f'index,x,y,z,value\n')
    for v in bm.verts:
        if v.select:
           f.write(f'{v.index},{v.co[0]},{-v.co[2]},{v.co[1]},{random.random()*10}\n')

