import bpy
import os
directory = 'C:/Users/Lala/Desktop/Synthetic Calibration Dataset/'
scene = bpy.context.scene
bpy.ops.scene.create_lightfield()
bpy.ops.object.empty_add(type='CUBE')
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        bpy.ops.object.delete()
        bpy.ops.import_image.to_plane(use_shadeless=True, files=[{'name':'C:/Users/Lala/Desktop/Synthetic Calibration Dataset/'+ filename }])
        for obj in scene.objects:
            if obj.type == 'MESH':
                obj.name = "Plane"
                bpy.data.objects["Plane"].location.x = 10.0
                bpy.data.objects["Plane"].rotation_euler[1]= 3.14/2
        for ob in scene.objects:
            if ob.type == 'CAMERA':
                bpy.context.scene.camera = ob
                print('Set camera %s' % ob.name )
                file = os.path.join("C:/Users/Lala/Desktop/Synthetic Calibration Dataset/cpt/", filename+ob.name )
                bpy.context.scene.render.filepath = file
                bpy.ops.render.render( write_still=True )