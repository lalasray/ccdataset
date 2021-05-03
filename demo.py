import bpy
import bmesh
import os
import numpy as np

bpy.ops.wm.addon_enable(module="io_import_images_as_planes")
bpy.ops.wm.addon_enable(module="add_curve_extra_objects")
bpy.ops.wm.addon_enable(module="blender-addon-master")


#create scene
bpyscene = bpy.context.scene
for scene in bpy.data.scenes:
    scene.render.engine = 'CYCLES'

# give directory for image
directory = 'Project/Textures/'

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
bpy.data.objects["Basic_Sphere"].scale[0]=2
bpy.data.objects["Basic_Sphere"].scale[2]=2
bpy.data.objects["Basic_Sphere"].scale[1]=0.1
bpy.data.objects["Basic_Sphere"].rotation_euler[2] = 3.14 / 2
bpy.data.objects["Basic_Sphere"].location[0] = 1
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

# set activer material to your new material
bpy.context.object.active_material = material
basic_sphere.data.materials.append(material)




# create and position the plane
bpy.ops.import_image.to_plane(use_shadeless=True, files=[{'name':'Project/texture.png' }])
bpy.data.objects["texture"].scale[0] = 0.8
bpy.data.objects["texture"].scale[1] = 0.8
bpy.data.objects["texture"].location[0] = 4.8
bpy.data.objects["texture"].rotation_euler[1] = 3.14 / 2
bpy.ops.mesh.primitive_plane_add(location=(5.7, 0, 0))
bpy.data.objects["Plane"].scale[0] = 0.01
bpy.data.objects["Plane"].scale[1] = 0.01
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
#ob.constraints['Follow Path']
con = ob.constraints.get("Follow Path")

if con:
    con.offset_factor = 0.0
    con.keyframe_insert("offset_factor", frame=1)
    print("Hi")

if con:
    con.offset_factor = 1.0
    con.keyframe_insert("offset_factor", frame=250)
    print("Bye")


#add light
bpy.ops.object.lamp_add(type='SUN',location=(4.8,-0.25,3.5),)
bpy.data.lamps['Sun'].node_tree.nodes["Emission"].inputs[1].default_value=80

#------------------------------------------------------------------------------------------------------------------------------------------------
#Capturing the scene
#------------------------------------------------------------------------------------------------------------------------------------------------



#for i in range(0,251,10):
#    bpyscene.frame_set(i)
#    bpyscene.update()
#    for filename in os.listdir(directory):
#        if filename.endswith(".png"):
#            bpy.data.images['texture.png'].filepath = directory + filename
#            for ob in bpy.context.scene.objects:
#                if ob.type == 'CAMERA':
#                    bpy.context.scene.camera = ob
#                    print('Set camera %s' % ob.name)
#                    file = os.path.join(directory + "cpt/",
#                                        filename + 'frame_' + str(bpyscene.frame_current) + 'camera_' + ob.name)
#                    bpy.context.scene.render.filepath = file
#                    bpy.ops.render.render(write_still=True)


bpyscene.frame_set(100)
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        bpy.data.images['texture.png'].filepath = directory + filename
        for ob in bpy.context.scene.objects:
            if ob.type == 'CAMERA':
                bpy.context.scene.camera = ob
                print('Set camera %s' % ob.name)
                file = os.path.join(directory + "cpt/",filename + '_frame_' + str(bpyscene.frame_current) + '_camera_' + ob.name)
                bpy.context.scene.render.filepath = file
                bpy.ops.render.render(write_still=True)

bpyscene.frame_set(200)
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        bpy.data.images['texture.png'].filepath = directory + filename
        for ob in bpy.context.scene.objects:
            if ob.type == 'CAMERA':
                bpy.context.scene.camera = ob
                print('Set camera %s' % ob.name)
                file = os.path.join(directory + "cpt/",filename + '_frame_' + str(bpyscene.frame_current) + '_camera_' + ob.name)
                bpy.context.scene.render.filepath = file
                bpy.ops.render.render(write_still=True)

