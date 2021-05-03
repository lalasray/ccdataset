import bpy

bpy.ops.object.select_all( action = 'SELECT' )
bpy.ops.object.origin_set( type = 'ORIGIN_GEOMETRY' )

data = bpy.data.meshes['Plane']
for f in data.polygons:
    for idx in f.vertices:
        Vertices=(data.vertices[idx].co)
        print (Vertices)

