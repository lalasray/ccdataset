
import bpy
import bmesh
import os
import numpy as np
import addon_utils
import mathutils 
from mathutils import Vector 




#------------------------------------------------------------------------------------------------------------------------------------------------
#Setting up the scene
#------------------------------------------------------------------------------------------------------------------------------------------------


#adding the custom addons
addon_utils.enable("io_import_images_as_planes")
addon_utils.enable("add_curve_extra_objects")
addon_utils.enable("blender_addon")

#creating scene and selecting the render engine
bpyscene = bpy.context.scene
for scene in bpy.data.scenes:
    scene.render.engine = 'BLENDER_EEVEE'
    scene.eevee.use_soft_shadows = False
    scene.grease_pencil_settings.antialias_threshold = 0

# give directory for image
directory = 'C:/Users/ray/Desktop/ccdataset-main/textures/'

#create lightfield camera and update it with our desired configuraion from the external configuration.cfg file
bpy.ops.scene.create_lightfield()
bpy.ops.scene.load_lightfield()


# create 4 light sourrces for the 4 direction the target might be facing then orient it properly and increase the illumination power
bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(4.8,-0.25,3.5), scale=(1, 1, 1))
bpy.context.object.data.energy = 150
bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(0.9,0.01,0.01), scale=(1, 1, 1))
bpy.context.object.data.energy = 150
bpy.data.objects['Spot.001'].rotation_euler[1]=3*3.14 / 2
bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(7.9,0.01,0.01), scale=(1, 1, 1))
bpy.context.object.data.energy = 150
bpy.data.objects['Spot.002'].rotation_euler[1]=3.14 / 2
bpy.ops.object.light_add(type='SPOT', radius=1, align='WORLD', location=(4.8,-0.25,-5), scale=(1, 1, 1))
bpy.context.object.data.energy = 150
bpy.data.objects['Spot.003'].rotation_euler[0]=3.14



#import the tecture images as planes fusing addon and put it in the scene as per requirements
bpy.ops.import_image.to_plane(files=[{'name':'C:/Users/ray/Desktop/ccdataset-main/texture.png' }])
bpy.data.objects["texture"].scale[0] = 0.75
bpy.data.objects["texture"].scale[1] = 0.75
bpy.data.objects["texture"].location[0] = 4.8
bpy.data.objects["texture"].rotation_euler[1] = 3.14 / 2
bpy.ops.mesh.primitive_plane_add(location=(5.7, 0, 0))
bpy.data.objects["Plane"].scale[0] = 0.001
bpy.data.objects["Plane"].scale[1] = 0.001
bpy.data.objects["Plane"].rotation_euler[1] = 3.14 / 2


#create a spiral path for the camera to move on and put it in the scene as per reqiuremnts 
bpy.ops.curve.spirals(spiral_type="ARCH", turns=4, dif_radius=0.5, dif_z=0.65, radius=0.15)
bpy.data.objects["Spiral"].rotation_euler[0] = 3*(3.14 / 2)
bpy.data.objects["Spiral"].rotation_euler[2] = 3.14 / 2
bpy.data.objects["Spiral"].scale[0] = 0.8
bpy.data.objects["Spiral"].scale[1] = 0.8
bpy.data.objects["Spiral"].scale[2] = 0.8



#set hiereachy of the objects we created (for the camera to follow the path it must be a child of the path)
bpy.data.objects['LF0'].parent=bpy.data.objects['Spiral']


#set the camera grid as current active object to add constarints to it
bpy.context.scene.objects["Spiral"].select_set(False)
bpy.context.scene.objects["LF0"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0"]


# add track to constarint to the active object make it target the plane and set its parameters
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].track_axis = 'TRACK_NEGATIVE_X'
bpy.context.object.constraints["Track To"].up_axis = 'UP_Z'


#add follow path constraint to the camera grid make it follow the siral and add parameters
bpy.ops.object.constraint_add(type='FOLLOW_PATH')
bpy.context.object.constraints["Follow Path"].forward_axis = 'FORWARD_Z'
bpy.context.object.constraints["Follow Path"].up_axis = 'UP_X'
bpy.context.object.constraints["Follow Path"].use_curve_follow = False
bpy.context.object.constraints["Follow Path"].use_fixed_location = True
bpy.context.object.constraints["Follow Path"].target = bpy.data.objects["Spiral"]

#the offset factor decide the position of the camera in the spiral path so set 0 frame as intital position and 250 frame as final position
ob = bpy.context.object
con = ob.constraints.get("Follow Path")

if con:
    con.offset_factor = 1.0
    con.keyframe_insert("offset_factor", frame=1)

if con:
    con.offset_factor = 0.0
    con.keyframe_insert("offset_factor", frame=250)


#set the camera grid as current active object to add constarints to it
bpy.context.scene.objects["LF0"].select_set(False)
bpy.context.scene.objects["LF0_Cam000"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam000"]
bpy.data.objects["LF0_Cam000"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam000"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam000"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam000"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam000"].select_set(False)
bpy.context.scene.objects["LF0_Cam001"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam001"]
bpy.data.objects["LF0_Cam001"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam001"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam001"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam001"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam001"].select_set(False)
bpy.context.scene.objects["LF0_Cam002"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam002"]
bpy.data.objects["LF0_Cam002"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam002"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam002"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam002"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam002"].select_set(False)
bpy.context.scene.objects["LF0_Cam003"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam003"]
bpy.data.objects["LF0_Cam003"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam003"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam003"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam003"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam003"].select_set(False)
bpy.context.scene.objects["LF0_Cam004"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam004"]
bpy.data.objects["LF0_Cam004"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam004"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam004"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam004"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam004"].select_set(False)
bpy.context.scene.objects["LF0_Cam005"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam005"]
bpy.data.objects["LF0_Cam005"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam005"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam005"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam005"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam005"].select_set(False)
bpy.context.scene.objects["LF0_Cam006"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam006"]
bpy.data.objects["LF0_Cam006"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam006"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam006"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam006"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam006"].select_set(False)
bpy.context.scene.objects["LF0_Cam007"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam007"]
bpy.data.objects["LF0_Cam007"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam007"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam007"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam007"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam007"].select_set(False)
bpy.context.scene.objects["LF0_Cam008"].select_set(True)
bpy.context.view_layer.objects.active = bpy.context.scene.objects["LF0_Cam008"]
bpy.data.objects["LF0_Cam008"].rotation_euler[2] = 0
bpy.data.objects["LF0_Cam008"].keyframe_insert('rotation_euler',frame=0)
bpy.data.objects["LF0_Cam008"].rotation_euler[2] = 6.28
bpy.data.objects["LF0_Cam008"].keyframe_insert('rotation_euler',frame=280)
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Plane"]
bpy.context.object.constraints["Track To"].influence = 0.6
bpy.context.scene.objects["LF0_Cam008"].select_set(False)





#------------------------------------------------------------------------------------------------------------------------------------------------
#Capturing the scene
#------------------------------------------------------------------------------------------------------------------------------------------------
for i in range(0,251,2):
    bpyscene.frame_set(i)
    #update the objects for each selected frame (in our case in every 2 frames)
    bpy.context.view_layer.update() 
    for filename in os.listdir(directory):
        #take all the texture from the texture directory and capture it one after another
        if filename.endswith(".png"):
            bpy.data.images['texture.png'].filepath = directory + filename
            for ob in bpy.context.scene.objects:
                if ob.type == 'CAMERA':
                    #for a perticular frame select all cameras and capture that scene using all those cameras
                    bpy.context.scene.camera = ob
                    print('Set camera %s' % ob.name)
                    #save the capture with frame no and camera name included in it
                    file = os.path.join(directory + "cpt/",
                                        filename + 'frame_' + str(bpyscene.frame_current) + 'camera_' + ob.name)
                    bpy.context.scene.render.filepath = file
                    bpy.ops.render.render(write_still=True)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Creating the txt file with position & orientation data
#------------------------------------------------------------------------------------------------------------------------------------------------

# before taking data we need to set the local origin(the position where the cursor lies) to global origin(centre of the scene)
def CenterOrigin():
    bpy.ops.transform.translate(value=(0, 0, 1), orient_type='GLOBAL')
    
    #put cursor at origin 
    bpy.context.scene.cursor.location = Vector((0.0, 0.0, 0.0))
    bpy.context.scene.cursor.rotation_euler = Vector((0.0, 0.0, 0.0))
    
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    
CenterOrigin()

#cretae txt file to save data
save_to_file = 'C:/Users/ray/Desktop/ccdataset-main/textures/frame.txt'
bpyscene = bpy.context.scene
with open(save_to_file, 'w') as file:
    file.write('Camera Parameters:'')\n')
    # to_translation() used for converting vertex to world space coordinates
    location = bpy.data.objects["Plane"].matrix_world.to_translation()
    nplocation = np.array([location.x,location.y,location.z])
    file.write('Plane Centre:('+str(location.x)+', '+str(location.y)+', '+str(location.z)+')\n')
    obj = bpy.data.objects['Plane']
    for every_frame in range(6, 241,2):
        bpyscene.frame_set(every_frame)
        for f in obj.data.polygons:
            for idx in f.vertices:
            	# again vertices and extracted and converted to world coordinates by multiplying with matrix world
                Vert = (obj.data.vertices[idx].co)
                mat = ob.matrix_world
                Vertices = mat @ Vert
                file.write('Plane Vertice at frame '+str(every_frame)+':('+ 'Vertices:'+str(idx) + ':(' + str(Vertices.x) + ', ' + str(Vertices.y) + ', ' + str(Vertices.z) + ')\n')
        # location and orientation for each cameras

        loc0 = bpy.context.scene.objects["LF0_Cam000"].matrix_world.to_translation()
        nploc0 = np.array([loc0.x, loc0.y, loc0.z])
        dist0 = np.sqrt(np.sum((nplocation - nploc0) ** 2, axis=0))
        #to_quaternion() is used for converting the angles to quaternion form 
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
        #all the data calculated is written into the text file
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