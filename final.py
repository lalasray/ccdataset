import bpy

save_to_file = 'c:/Users/Lala/Desktop/file.txt'

ob = bpy.data.objects['Plane']

v = ob.data.vertices[0].co
mat = ob.matrix_world
loc = mat * v
print (loc)

with open(save_to_file, 'w') as file:
    #file.write('verts = ' + str(loc))
    file.close()
