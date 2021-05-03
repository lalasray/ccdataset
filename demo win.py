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
bpy.ops.import_image.to_plane(use_shadeless=True, files=[{'name':'C:/Users/Lala/Desktop/Synthetic Calibration Dataset/texture.png' }])
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



for i in range(0,251,10):
    bpyscene.frame_set(i)
    bpyscene.update()
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            bpy.data.images['texture.png'].filepath = directory + filename
            for ob in bpy.context.scene.objects:
                if ob.type == 'CAMERA':
                    bpy.context.scene.camera = ob
                    print('Set camera %s' % ob.name)
                    file = os.path.join(directory + "cpt/",
                                        filename + 'frame_' + str(bpyscene.frame_current) + 'camera_' + ob.name)
                    bpy.context.scene.render.filepath = file
                    bpy.ops.render.render(write_still=True)


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
    for f in data.polygons:
        for idx in f.vertices:
            lVertices = (data.vertices[idx].co)
            mat = ob.matrix_world
            Vertices = mat * lVertices
            file.write('Plane Vertice '+str(idx)+':('+str(Vertices.x)+', '+str(Vertices.y)+', '+str(Vertices.z)+')\n')
    for every_frame in range(0, 251,10):
        bpyscene.frame_set(every_frame)
        loc0 = bpy.context.scene.objects["LF0_Cam000"].matrix_world.to_translation()
        nploc0 = np.array([loc0.x, loc0.y, loc0.z])
        dist0 = np.sqrt(np.sum((nplocation - nploc0) ** 2, axis=0))
        rot0 = bpy.context.scene.objects["LF0_Cam000"].matrix_world.to_euler('XYZ')
        loc1 = bpy.context.scene.objects["LF0_Cam001"].matrix_world.to_translation()
        nploc1 = np.array([loc1.x, loc1.y, loc1.z])
        dist1 = np.sqrt(np.sum((nplocation - nploc1) ** 2, axis=0))
        rot1 = bpy.context.scene.objects["LF0_Cam001"].matrix_world.to_euler('XYZ')
        loc2 = bpy.context.scene.objects["LF0_Cam002"].matrix_world.to_translation()
        nploc2 = np.array([loc2.x, loc2.y, loc2.z])
        dist2 = np.sqrt(np.sum((nplocation - nploc2) ** 2, axis=0))
        rot2 = bpy.context.scene.objects["LF0_Cam002"].matrix_world.to_euler('XYZ')
        loc3 = bpy.context.scene.objects["LF0_Cam003"].matrix_world.to_translation()
        nploc3 = np.array([loc3.x, loc3.y, loc3.z])
        dist3 = np.sqrt(np.sum((nplocation - nploc3) ** 2, axis=0))
        rot3 = bpy.context.scene.objects["LF0_Cam003"].matrix_world.to_euler('XYZ')
        loc4 = bpy.context.scene.objects["LF0_Cam004"].matrix_world.to_translation()
        nploc4 = np.array([loc4.x, loc4.y, loc4.z])
        dist4 = np.sqrt(np.sum((nplocation - nploc4) ** 2, axis=0))
        rot4 = bpy.context.scene.objects["LF0_Cam004"].matrix_world.to_euler('XYZ')
        loc5 = bpy.context.scene.objects["LF0_Cam005"].matrix_world.to_translation()
        nploc5 = np.array([loc5.x, loc5.y, loc5.z])
        dist5 = np.sqrt(np.sum((nplocation - nploc5) ** 2, axis=0))
        rot5 = bpy.context.scene.objects["LF0_Cam005"].matrix_world.to_euler('XYZ')
        loc6 = bpy.context.scene.objects["LF0_Cam006"].matrix_world.to_translation()
        nploc6 = np.array([loc6.x, loc6.y, loc6.z])
        dist6 = np.sqrt(np.sum((nplocation - nploc6) ** 2, axis=0))
        rot6 = bpy.context.scene.objects["LF0_Cam006"].matrix_world.to_euler('XYZ')
        loc7 = bpy.context.scene.objects["LF0_Cam007"].matrix_world.to_translation()
        nploc7 = np.array([loc7.x, loc7.y, loc7.z])
        dist7 = np.sqrt(np.sum((nplocation - nploc7) ** 2, axis=0))
        rot7 = bpy.context.scene.objects["LF0_Cam007"].matrix_world.to_euler('XYZ')
        loc8 = bpy.context.scene.objects["LF0_Cam008"].matrix_world.to_translation()
        nploc8 = np.array([loc8.x, loc8.y, loc8.z])
        dist8 = np.sqrt(np.sum((nplocation - nploc0) ** 2, axis=0))
        rot8 = bpy.context.scene.objects["LF0_Cam008"].matrix_world.to_euler('XYZ')

        file.write(
            'Cam000 Position at frame '+str(every_frame)+':('+str(loc0.x)+', '+str(loc0.y)+', '+str(loc0.z)+')\n'
            'Cam000 Distance at frame '+str(every_frame)+':('+str(dist0)+')\n'
            'Cam000 Orientation at frame '+str(every_frame)+':('+str(rot0.x)+', '+str(rot0.y)+', '+str(rot0.z)+')\n'
            'Cam001 Position at frame ' + str(every_frame) + ':(' + str(loc1.x) + ', ' + str(loc1.y) + ', ' + str(loc1.z) + ')\n'
            'Cam001 Distance at frame '+str(every_frame)+':('+str(dist1)+')\n'
            'Cam001 Orientation at frame ' + str(every_frame) + ':(' + str(rot1.x) + ', ' + str(rot1.y) + ', ' + str(rot1.z) + ')\n'
            'Cam002 Position at frame ' + str(every_frame) + ':(' + str(loc2.x) + ', ' + str(loc2.y) + ', ' + str(loc2.z) + ')\n'
            'Cam002 Distance at frame '+str(every_frame)+':('+str(dist2)+')\n'
            'Cam002 Orientation at frame ' + str(every_frame) + ':(' + str(rot2.x) + ', ' + str(rot2.y) + ', ' + str(rot2.z) + ')\n'
            'Cam003 Position at frame ' + str(every_frame) + ':(' + str(loc3.x) + ', ' + str(loc3.y) + ', ' + str(loc3.z) + ')\n'
            'Cam003 Distance at frame '+str(every_frame)+':('+str(dist3)+')\n'
            'Cam003 Orientation at frame ' + str(every_frame) + ':(' + str(rot3.x) + ', ' + str(rot3.y) + ', ' + str(rot3.z) + ')\n'
            'Cam004 Position at frame ' + str(every_frame) + ':(' + str(loc4.x) + ', ' + str(loc4.y) + ', ' + str(loc4.z) + ')\n'
            'Cam004 Distance at frame '+str(every_frame)+':('+str(dist4)+')\n'
            'Cam004 Orientation at frame ' + str(every_frame) + ':(' + str(rot4.x) + ', ' + str(rot4.y) + ', ' + str(rot4.z) + ')\n'
            'Cam005 Position at frame ' + str(every_frame) + ':(' + str(loc5.x) + ', ' + str(loc5.y) + ', ' + str(loc5.z) + ')\n'
            'Cam005 Distance at frame '+str(every_frame)+':('+str(dist5)+')\n'
            'Cam005 Orientation at frame ' + str(every_frame) + ':(' + str(rot5.x) + ', ' + str(rot5.y) + ', ' + str(rot5.z) + ')\n'
            'Cam006 Position at frame ' + str(every_frame) + ':(' + str(loc6.x) + ', ' + str(loc6.y) + ', ' + str(loc6.z) + ')\n'
            'Cam006 Distance at frame '+str(every_frame)+':('+str(dist6)+')\n'
            'Cam006 Orientation at frame ' + str(every_frame) + ':(' + str(rot6.x) + ', ' + str(rot6.y) + ', ' + str(rot6.z) + ')\n'
            'Cam007 Position at frame ' + str(every_frame) + ':(' + str(loc7.x) + ', ' + str(loc7.y) + ', ' + str(loc7.z) + ')\n'
            'Cam007 Distance at frame '+str(every_frame)+':('+str(dist7)+')\n'
            'Cam007 Orientation at frame ' + str(every_frame) + ':(' + str(rot7.x) + ', ' + str(rot7.y) + ', ' + str(rot7.z) + ')\n'
            'Cam008 Position at frame ' + str(every_frame) + ':(' + str(loc8.x) + ', ' + str(loc8.y) + ', ' + str(loc8.z) + ')\n'
            'Cam008 Distance at frame '+str(every_frame)+':('+str(dist8)+')\n'
            'Cam008 Orientation at frame ' + str(every_frame) + ':(' + str(rot8.x) + ', ' + str(rot8.y) + ', ' + str(rot8.z) + ')\n')