import bpy

bpy.ops.mesh.primitive_plane_add(location=(10, 0, 0))
bpy.data.objects["Plane"].rotation_euler[1] = 3.14 / 2
bpy.ops.curve.spirals(spiral_type="ARCH", turns=4, dif_radius=0.7, dif_z=0.1, radius=0.5)
# bpy.ops.curve.primitive_nurbs_circle_add(location=(0,0,0))
bpy.data.objects["Spiral"].rotation_euler[0] = 3.14 / 2
bpy.data.objects["Spiral"].rotation_euler[2] = 3.14 / 2

# bpy.data.objects["NurbsCircle"].rotation_euler[0]= 3.14/2
# bpy.data.objects["NurbsCircle"].rotation_euler[2]= 3.14/2
# bpy.data.objects["NurbsCircle"].scale[0]=2

bpy.ops.scene.create_lightfield()

objects = bpy.data.objects
b = objects['LF0']
# c = objects['NurbsCircle']
c = objects['Spiral']
b.parent = c

bpy.ops.object.constraint_add(type='FOLLOW_PATH')
# add follow path constraint
# bpy.data.objects["LF0"].constraints["Follow Path"].target = bpy.data.objects["NurbsCircle"]
# #sets the cube on the nurbs curve path
bpy.data.objects["LF0"].constraints["Follow Path"].target = bpy.data.objects["Spiral"]
bpy.data.objects["LF0"].constraints["Follow Path"].forward_axis = 'FORWARD_Y'
# sets the face of the cube on the positive x-axis as front of car
bpy.data.objects["LF0"].constraints["Follow Path"].use_curve_follow = True
bpy.data.objects["LF0"].constraints["Follow Path"].use_fixed_location = True

bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.data.objects["LF0"].constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.data.objects["LF0"].constraints["Track To"].track_axis = 'TRACK_NEGATIVE_Z'
bpy.data.objects["LF0"].constraints["Track To"].up_axis = 'UP_X'

ob = bpy.context.object
ob.constraints['Follow Path']
con = ob.constraints.get("Follow Path")

if con:
    con.offset_factor = 0.0
    con.keyframe_insert("offset_factor", frame=1)
    print("Hi")

if con:
    con.offset_factor = 1.0
    con.keyframe_insert("offset_factor", frame=250)
    print("Bye")
