import bpy

# switch on nodes and get reference
bpy.context.scene.use_nodes = True
tree = bpy.context.scene.node_tree

# clear default nodes
for node in tree.nodes:
    tree.nodes.remove(node)

# create input image node
image_node = tree.nodes.new(type='CompositorNodeMovieClip')
#load new movie clip
bpy.data.movieclips.load("C:\\Users\\ray\\Desktop\\ccdataset-main\\textures\\video.avi")
#get the new movie clip
movie_clip = bpy.data.movieclips.get("video.avi")
#assign movie clip to the node
bpy.context.scene.node_tree.nodes['Movie Clip'].clip = movie_clip
image_node.location = 0,0
# create distort node
dist_node = tree.nodes.new('CompositorNodeMovieDistortion')   
dist_node.location = 400,0
#load new movie clip
#bpy.data.movieclips.load("C:\\Users\\ray\\Desktop\\ccdataset-main\\textures\\video.avi")
#get the new movie clip
#dist_clip = bpy.data.movieclips.get("video.avi")
#assign movie clip to the node
#bpy.context.scene.node_tree.nodes['Undistortion'].clip =dist_clip

# create output node
comp_node = tree.nodes.new('CompositorNodeComposite')   
comp_node.location = 800,0

# link nodes
links = tree.links
link = links.new(image_node.outputs[0], dist_node.inputs[0])
link = links.new(dist_node.outputs[0], comp_node.inputs[0])



bpy.data.movieclips["video.avi"].tracking.camera.k1 = 0.1
bpy.data.movieclips["video.avi"].tracking.camera.k2 = 0.2
bpy.data.movieclips["video.avi"].tracking.camera.k3 = 0.3
