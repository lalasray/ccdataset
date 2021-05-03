import bpy

bpy.ops.object.select_all( action = 'SELECT' )
bpy.ops.object.origin_set( type = 'ORIGIN_GEOMETRY' )

save_to_file = '/Data.txt'

#vertices = [(vert.co.x, vert.co.y, vert.co.z) for vert in bpy.context.object.data.vertices]
location = bpy.data.objects["Plane"].location
rotation = bpy.data.objects["Plane"].rotation_euler
data = bpy.data.meshes['Plane']
for f in data.polygons:
    for idx in f.vertices:
        Vertices=(data.vertices[idx].co)

cam0location = bpy.data.objects["LF0_Cam000"].location
cam0rotation = bpy.data.objects["LF0_Cam000"].rotation_euler
cam1location = bpy.data.objects["LF0_Cam001"].location
cam1rotation = bpy.data.objects["LF0_Cam001"].rotation_euler
cam2location = bpy.data.objects["LF0_Cam002"].location
cam2rotation = bpy.data.objects["LF0_Cam002"].rotation_euler
cam3location = bpy.data.objects["LF0_Cam003"].location
cam3rotation = bpy.data.objects["LF0_Cam003"].rotation_euler
cam4location = bpy.data.objects["LF0_Cam004"].location
cam4rotation = bpy.data.objects["LF0_Cam004"].rotation_euler
cam5location = bpy.data.objects["LF0_Cam005"].location
cam5rotation = bpy.data.objects["LF0_Cam005"].rotation_euler
cam6location = bpy.data.objects["LF0_Cam006"].location
cam6rotation = bpy.data.objects["LF0_Cam006"].rotation_euler
cam7location = bpy.data.objects["LF0_Cam007"].location
cam7rotation = bpy.data.objects["LF0_Cam007"].rotation_euler
cam8location = bpy.data.objects["LF0_Cam008"].location
cam8rotation = bpy.data.objects["LF0_Cam008"].rotation_euler
camlocation = bpy.data.objects["LF0"].location
camrotation = bpy.data.objects["LF0"].rotation_euler




with open(save_to_file, 'w') as file:
    file.write('Plane Verts = ' + str(vertices) + '\n'+'Plane location = ' + str(location) + '\n'+'Plane roatation = ' + '\n'+ str(rotation) +'Cam0 location = ' + str(cam0location) + '\n'+'Cam0 roatation = ' + str(cam0rotation) + '\n'+'Cam1 location = ' + str(cam1location) + '\n'+'Cam1 roatation = ' + str(cam1rotation) + '\n'+'Cam2 location = ' + str(cam2location) + '\n'+'Cam2 roatation = ' + str(cam2rotation) + '\n'+'Cam3 location = ' + str(cam3location) + '\n'+'Cam3 roatation = ' + str(cam3rotation) + '\n'+'Cam4 location = ' + str(cam4location) + '\n'+'Cam4 roatation = ' + str(cam4rotation) + '\n'+'Cam5 location = ' + str(cam5location) + '\n'+'Cam5 roatation = ' + str(cam5rotation) + '\n'+'Cam6 location = ' + str(cam6location) + '\n'+'Cam6 roatation = ' + str(cam6rotation) + '\n'+'Cam7 location = ' + str(cam7location) + '\n'+'Cam7 roatation = ' + str(cam7rotation) + '\n'+'Cam8 location = ' + str(cam8location) + '\n'+'Cam8 roatation = ' + str(cam8rotation) + '\n')
    file.close()
