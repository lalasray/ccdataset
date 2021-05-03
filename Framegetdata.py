import bpy
import numpy as np

bpy.ops.object.select_all( action = 'SELECT' )
bpy.ops.object.origin_set( type = 'ORIGIN_GEOMETRY' )

save_to_file = 'c:/Users/Lala/Desktop/frame.txt'
bpyscene = bpy.context.scene
with open(save_to_file, 'w') as file:
    location = bpy.data.objects["Plane"].location
    nplocation = np.array([location.x,location.y,location.z])
    file.write('Plane Position:('+str(location.x)+', '+str(location.y)+', '+str(location.z)+')\n')
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