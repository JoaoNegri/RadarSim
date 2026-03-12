from modules import scene

# create a scene containing one radar and a point target
scene1 = scene.Scene("Scene 1")

# display a static plot of the initial scene (optional)
# scene1.plot()

# animate for 200 frames; the method returns the animation object
# and stores it on the scene instance to keep it alive.
anim = scene1.animate(frames=200)
