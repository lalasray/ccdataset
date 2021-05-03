import bpy
import bmesh
import os
import numpy as np


#create scene
bpyscene = bpy.context.scene
for scene in bpy.data.scenes:
    scene.render.engine = 'CYCLES'

# give directory for image
directory = 'C:/Users/Lala/Desktop/Synthetic Calibration Dataset/'

# Create an empty mesh and the object.
mesh = bpy.data.meshes.new('Basic_Sphere')
basic_sphere = bpy.data.objects.new("Basic_Sphere", mesh)

# Add the object into the scene.
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True


# Construct the bmesh sphere and assign it to the blender mesh.
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere"].scale[0]=0.01
bpy.data.objects["Basic_Sphere"].scale[1]=0.002
bpy.data.objects["Basic_Sphere"].scale[2]=0.01
bpy.data.objects["Basic_Sphere"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere"].modifiers["Mirror"].use_x=False

# Create a new material
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A

# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])

# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)

basic_sphere = bpy.data.objects.new("Basic_Sphere1", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere1"].scale[0]=0.01
bpy.data.objects["Basic_Sphere1"].scale[1]=0.001
bpy.data.objects["Basic_Sphere1"].scale[2]=0.01
bpy.data.objects["Basic_Sphere1"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere1"].location[2] = -0.02

bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere1"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere1"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere1"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere1"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)

basic_sphere = bpy.data.objects.new("Basic_Sphere2", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere2"].scale[0]=0.01
bpy.data.objects["Basic_Sphere2"].scale[1]=0.003
bpy.data.objects["Basic_Sphere2"].scale[2]=0.01
bpy.data.objects["Basic_Sphere2"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere2"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere2"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere2"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere2"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere2"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)

basic_sphere = bpy.data.objects.new("Basic_Sphere3", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere3"].scale[0]=0.01
bpy.data.objects["Basic_Sphere3"].scale[1]=0.004
bpy.data.objects["Basic_Sphere3"].scale[2]=0.01
bpy.data.objects["Basic_Sphere3"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere3"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere3"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere3"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere3"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere3"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)

basic_sphere = bpy.data.objects.new("Basic_Sphere4", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere4"].scale[0]=0.01
bpy.data.objects["Basic_Sphere4"].scale[1]=0.0045
bpy.data.objects["Basic_Sphere4"].scale[2]=0.01
bpy.data.objects["Basic_Sphere4"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere4"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere4"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere4"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere4"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere4"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)


basic_sphere = bpy.data.objects.new("Basic_Sphere5", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere5"].scale[0]=0.01
bpy.data.objects["Basic_Sphere5"].scale[1]=0.0035
bpy.data.objects["Basic_Sphere5"].scale[2]=0.01
bpy.data.objects["Basic_Sphere5"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere5"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere5"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere5"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere5"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere5"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)

basic_sphere = bpy.data.objects.new("Basic_Sphere6", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere6"].scale[0]=0.01
bpy.data.objects["Basic_Sphere6"].scale[1]=0.0025
bpy.data.objects["Basic_Sphere6"].scale[2]=0.01
bpy.data.objects["Basic_Sphere6"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere6"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere6"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere6"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere6"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere6"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)


basic_sphere = bpy.data.objects.new("Basic_Sphere7", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere7"].scale[0]=0.01
bpy.data.objects["Basic_Sphere7"].scale[1]=0.0015
bpy.data.objects["Basic_Sphere7"].scale[2]=0.01
bpy.data.objects["Basic_Sphere7"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere7"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere7"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere7"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere7"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere7"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)

basic_sphere = bpy.data.objects.new("Basic_Sphere8", mesh)
bpyscene.objects.link(basic_sphere)
bpyscene.objects.active = basic_sphere
basic_sphere.select = True
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
bpy.data.objects["Basic_Sphere8"].scale[0]=0.01
bpy.data.objects["Basic_Sphere8"].scale[1]=0.0005
bpy.data.objects["Basic_Sphere8"].scale[2]=0.01
bpy.data.objects["Basic_Sphere8"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Basic_Sphere8"].location[2] = -0.02
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.data.objects["Basic_Sphere8"].modifiers["Subsurf"].levels=3
bpy.data.objects["Basic_Sphere8"].modifiers["Subsurf"].render_levels=4
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='MIRROR')
bpy.data.objects["Basic_Sphere8"].modifiers["Mirror"].use_z=True
bpy.data.objects["Basic_Sphere8"].modifiers["Mirror"].use_x=False
material = bpy.data.materials.new(name="Diffuse")
material.use_nodes = True
material.node_tree.nodes.remove(material.node_tree.nodes.get('Diffuse BSDF')) #title of the existing node when materials.new
material_output = material.node_tree.nodes.get('Material Output')
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfGlass')    #name of diffuse BSDF when added with shift+A
# link diffuse shader to material
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])
# set active material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)

# create and position the plane
bpy.ops.import_image.to_plane(use_shadeless=True, files=[{'name':'C:/Users/Lala/Desktop/Synthetic Calibration Dataset/texture.png' }])
bpy.data.objects["texture"].scale[0] = 0.75
bpy.data.objects["texture"].scale[1] = 0.75
bpy.data.objects["texture"].location[0] = 4.8
bpy.data.objects["texture"].rotation_euler[1] = 3.14 / 2
bpy.ops.mesh.primitive_plane_add(location=(5.7, 0, 0))
bpy.data.objects["Plane"].scale[0] = 0.001
bpy.data.objects["Plane"].scale[1] = 0.001
bpy.data.objects["Plane"].rotation_euler[1] = 3.14 / 2



#create and position the path
bpy.ops.curve.spirals(spiral_type="ARCH", turns=4, dif_radius=0.7, dif_z=0.1, radius=0.5)
bpy.data.objects["Spiral"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Spiral"].rotation_euler[2] = 3.14 / 2
bpy.data.objects["Spiral"].scale[0] = 0.5
bpy.data.objects["Spiral"].scale[1] = 0.5
bpy.data.objects["Spiral"].scale[2] = 0.5

#create lightfield camera
bpy.ops.scene.create_lightfield()

#ser heirarchy
objects = bpy.data.objects
b = objects['LF0']
b0 = objects['LF0_Cam000']
b1 = objects['LF0_Cam001']
b2 = objects['LF0_Cam002']
b3 = objects['LF0_Cam003']
b4 = objects['LF0_Cam004']
b5 = objects['LF0_Cam005']
b6 = objects['LF0_Cam006']
b7 = objects['LF0_Cam007']
b8 = objects['LF0_Cam008']
a = objects['Basic_Sphere']
d = objects['Basic_Sphere1']
e = objects['Basic_Sphere2']
f = objects['Basic_Sphere3']
g = objects['Basic_Sphere4']
h = objects['Basic_Sphere5']
i = objects['Basic_Sphere6']
j = objects['Basic_Sphere7']
k = objects['Basic_Sphere8']
a.parent = b0
d.parent = b1
e.parent = b2
f.parent = b3
g.parent = b4
h.parent = b5
i.parent = b6
j.parent = b7
k.parent = b8
c = objects['Spiral']

b.parent = c
# add follow path constraint
bpy.ops.object.constraint_add(type='FOLLOW_PATH')
bpy.data.objects["LF0"].constraints["Follow Path"].target = bpy.data.objects["Spiral"]
bpy.data.objects["LF0"].constraints["Follow Path"].forward_axis = 'FORWARD_Y'
bpy.data.objects["LF0"].constraints["Follow Path"].use_curve_follow = True
bpy.data.objects["LF0"].constraints["Follow Path"].use_fixed_location = True

#track the plane
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.data.objects["LF0"].constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.data.objects["LF0"].constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
bpy.data.objects["LF0"].constraints["Track To"].up_axis = 'UP_X'

#add frames
ob = bpy.context.object
con = ob.constraints.get("Follow Path")

if con:
    con.offset_factor = 0.0
    con.keyframe_insert("offset_factor", frame=1)

if con:
    con.offset_factor = 1.0
    con.keyframe_insert("offset_factor", frame=250)

myplane = bpy.data.objects['texture']
myplane.rotation_mode = 'XYZ'
myplane.rotation_euler = (0, 0, 0)
myplane.keyframe_insert('rotation_euler',frame=1)
myplane.rotation_euler = (45,45,45) # (x, y, z)
myplane.keyframe_insert('rotation_euler',frame=250) # index=0 is x-axis


#add light
bpy.ops.object.lamp_add(type='SPOT',location=(4.8,-0.25,3.5),)
bpy.data.lamps['Spot'].node_tree.nodes["Emission"].inputs[1].default_value=100
bpy.ops.object.lamp_add(type='SPOT',location=(0.9,0.01,0.01),)
bpy.data.lamps['Spot.001'].node_tree.nodes["Emission"].inputs[1].default_value=200
bpy.data.objects['Spot.001'].rotation_euler[1]=3*3.14 / 2
bpy.ops.object.lamp_add(type='SPOT',location=(7.9,0.01,0.01),)
bpy.data.lamps['Spot.002'].node_tree.nodes["Emission"].inputs[1].default_value=100
bpy.data.objects['Spot.002'].rotation_euler[1]=3.14 / 2
bpy.ops.object.lamp_add(type='SPOT',location=(4.8,-0.25,-5),)
bpy.data.lamps['Spot.003'].node_tree.nodes["Emission"].inputs[1].default_value=100
bpy.data.objects['Spot.003'].rotation_euler[0]=3.14


#------------------------------------------------------------------------------------------------------------------------------------------------
#Capturing the scene
#------------------------------------------------------------------------------------------------------------------------------------------------






#------------------------------------------------------------------------------------------------------------------------------------------------
#Creating the txt file with position & orientation data
#------------------------------------------------------------------------------------------------------------------------------------------------
bpy.ops.object.select_all( action = 'SELECT' )
bpy.ops.object.origin_set( type = 'ORIGIN_GEOMETRY' )

save_to_file = 'c:/Users/Lala/Desktop/frame.txt'
bpyscene = bpy.context.scene
with open(save_to_file, 'w') as file:
    location = bpy.data.objects["Plane"].matrix_world.to_translation()
    nplocation = np.array([location.x,location.y,location.z])
    file.write('Plane Position:('+str(location.x)+', '+str(location.y)+', '+str(location.z)+')\n')
    data = bpy.data.meshes['Plane']
    for every_frame in range(0, 251,10):
        bpyscene.frame_set(every_frame)
        for f in data.polygons:
            for idx in f.vertices:
                lVertices = (data.vertices[idx].co)
                mat = ob.matrix_world
                Vertices = mat * lVertices
                file.write('Plane Vertice at frame '+str(every_frame)+':('+ 'Vert:'+str(idx) + ':(' + str(Vertices.x) + ', ' + str(Vertices.y) + ', ' + str(
                    Vertices.z) + ')\n')
        loc0 = bpy.context.scene.objects["LF0_Cam000"].matrix_world.to_translation()
        nploc0 = np.array([loc0.x, loc0.y, loc0.z])
        dist0 = np.sqrt(np.sum((nplocation - nploc0) ** 2, axis=0))
        rot0 = bpy.context.scene.objects["LF0_Cam000"].matrix_world.to_quaternion()
        loc1 = bpy.context.scene.objects["LF0_Cam001"].matrix_world.to_translation()
        nploc1 = np.array([loc1.x, loc1.y, loc1.z])
        dist1 = np.sqrt(np.sum((nplocation - nploc1) ** 2, axis=0))
        rot1 = bpy.context.scene.objects["LF0_Cam001"].matrix_world.to_quaternion()
        loc2 = bpy.context.scene.objects["LF0_Cam002"].matrix_world.to_translation()
        nploc2 = np.array([loc2.x, loc2.y, loc2.z])
        dist2 = np.sqrt(np.sum((nplocation - nploc2) ** 2, axis=0))
        rot2 = bpy.context.scene.objects["LF0_Cam002"].matrix_world.to_quaternion()
        loc3 = bpy.context.scene.objects["LF0_Cam003"].matrix_world.to_translation()
        nploc3 = np.array([loc3.x, loc3.y, loc3.z])
        dist3 = np.sqrt(np.sum((nplocation - nploc3) ** 2, axis=0))
        rot3 = bpy.context.scene.objects["LF0_Cam003"].matrix_world.to_quaternion()
        loc4 = bpy.context.scene.objects["LF0_Cam004"].matrix_world.to_translation()
        nploc4 = np.array([loc4.x, loc4.y, loc4.z])
        dist4 = np.sqrt(np.sum((nplocation - nploc4) ** 2, axis=0))
        rot4 = bpy.context.scene.objects["LF0_Cam004"].matrix_world.to_quaternion()
        loc5 = bpy.context.scene.objects["LF0_Cam005"].matrix_world.to_translation()
        nploc5 = np.array([loc5.x, loc5.y, loc5.z])
        dist5 = np.sqrt(np.sum((nplocation - nploc5) ** 2, axis=0))
        rot5 = bpy.context.scene.objects["LF0_Cam005"].matrix_world.to_quaternion()
        loc6 = bpy.context.scene.objects["LF0_Cam006"].matrix_world.to_translation()
        nploc6 = np.array([loc6.x, loc6.y, loc6.z])
        dist6 = np.sqrt(np.sum((nplocation - nploc6) ** 2, axis=0))
        rot6 = bpy.context.scene.objects["LF0_Cam006"].matrix_world.to_quaternion()
        loc7 = bpy.context.scene.objects["LF0_Cam007"].matrix_world.to_translation()
        nploc7 = np.array([loc7.x, loc7.y, loc7.z])
        dist7 = np.sqrt(np.sum((nplocation - nploc7) ** 2, axis=0))
        rot7 = bpy.context.scene.objects["LF0_Cam007"].matrix_world.to_quaternion()
        loc8 = bpy.context.scene.objects["LF0_Cam008"].matrix_world.to_translation()
        nploc8 = np.array([loc8.x, loc8.y, loc8.z])
        dist8 = np.sqrt(np.sum((nplocation - nploc0) ** 2, axis=0))
        rot8 = bpy.context.scene.objects["LF0_Cam008"].matrix_world.to_quaternion()

        file.write(
            'Cam000 Position at frame '+str(every_frame)+':('+str(loc0.x)+', '+str(loc0.y)+', '+str(loc0.z)+')\n'
            'Cam000 Distance at frame '+str(every_frame)+':('+str(dist0)+')\n'
            'Cam000 Orientation at frame '+str(every_frame)+':('+str(rot0)+')\n'
            'Cam001 Position at frame ' + str(every_frame) + ':(' + str(loc1.x) + ', ' + str(loc1.y) + ', ' + str(loc1.z) + ')\n'
            'Cam001 Distance at frame '+str(every_frame)+':('+str(dist1)+')\n'
            'Cam001 Orientation at frame ' + str(every_frame) + ':(' + str(rot1) + ')\n'
            'Cam002 Position at frame ' + str(every_frame) + ':(' + str(loc2.x) + ', ' + str(loc2.y) + ', ' + str(loc2.z) + ')\n'
            'Cam002 Distance at frame '+str(every_frame)+':('+str(dist2)+')\n'
            'Cam002 Orientation at frame ' + str(every_frame) + ':(' + str(rot2) + ')\n'
            'Cam003 Position at frame ' + str(every_frame) + ':(' + str(loc3.x) + ', ' + str(loc3.y) + ', ' + str(loc3.z) + ')\n'
            'Cam003 Distance at frame '+str(every_frame)+':('+str(dist3)+')\n'
            'Cam003 Orientation at frame ' + str(every_frame) + ':(' + str(rot3) + ')\n'
            'Cam004 Position at frame ' + str(every_frame) + ':(' + str(loc4.x) + ', ' + str(loc4.y) + ', ' + str(loc4.z) + ')\n'
            'Cam004 Distance at frame '+str(every_frame)+':('+str(dist4)+')\n'
            'Cam004 Orientation at frame ' + str(every_frame) + ':(' + str(rot4) + ')\n'
            'Cam005 Position at frame ' + str(every_frame) + ':(' + str(loc5.x) + ', ' + str(loc5.y) + ', ' + str(loc5.z) + ')\n'
            'Cam005 Distance at frame '+str(every_frame)+':('+str(dist5)+')\n'
            'Cam005 Orientation at frame ' + str(every_frame) + ':(' + str(rot5) + ')\n'
            'Cam006 Position at frame ' + str(every_frame) + ':(' + str(loc6.x) + ', ' + str(loc6.y) + ', ' + str(loc6.z) + ')\n'
            'Cam006 Distance at frame '+str(every_frame)+':('+str(dist6)+')\n'
            'Cam006 Orientation at frame ' + str(every_frame) + ':(' + str(rot6) + ')\n'
            'Cam007 Position at frame ' + str(every_frame) + ':(' + str(loc7.x) + ', ' + str(loc7.y) + ', ' + str(loc7.z) + ')\n'
            'Cam007 Distance at frame '+str(every_frame)+':('+str(dist7)+')\n'
            'Cam007 Orientation at frame ' + str(every_frame) + ':(' + str(rot7) + ')\n'
            'Cam008 Position at frame ' + str(every_frame) + ':(' + str(loc8.x) + ', ' + str(loc8.y) + ', ' + str(loc8.z) + ')\n'
            'Cam008 Distance at frame '+str(every_frame)+':('+str(dist8)+')\n'
            'Cam008 Orientation at frame ' + str(every_frame) + ':(' + str(rot8) + ')\n')