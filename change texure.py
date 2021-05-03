import bpy
import bmesh
import os

#bpy.ops.mesh.primitive_plane_add(location=(9, 0, 0))
#bpy.data.objects["Plane"].dimensions[0] = 2.3
#bpy.data.objects["Plane"].dimensions[1] = 2.3
#bpy.data.objects["Plane"].rotation_euler[1] = 3.14 / 2

#mat = bpy.data.materials.new("mat")
#mat = bpy.data.materials.new(name="mat")
#tex = bpy.data.textures.new("tex","IMAGE")

#img = bpy.data.images.load("C:/Users/Lala/Desktop/Synthetic Calibration Dataset/cc.png")
#slot = texture.texture_slots.add()
#slot.texture = tex
#tex.image = img
#Plane.data.materials.append(mat)
#object.data.materials.append(mat)
#object.data.materials[0] = mat
bpy.data.images['texture.png'].filepath = "C:/Users/Lala/Desktop/Synthetic Calibration Dataset/cc.png"