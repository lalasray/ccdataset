import bpy
import bmesh

bpyscene = bpy.context.scene

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
bpy.data.objects["Basic_Sphere"].scale[1]=0.15
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
