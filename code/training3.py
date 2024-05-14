import pyglet
from pyglet import shapes

window = pyglet.window.Window(width=1280,height=720, caption ="Hello pyglet")
window.set_location(x=400, y=200)

#create a batch object
batch = pyglet.graphics.Batch()

#define the shapes to be drawn and add them to the batch
circle1 = shapes.Circle(x=700, y=150, radius=10, color=(50,255,30), batch=batch)
circle2 = shapes.Circle(x=100, y=150, radius=25, color=(255, 0,0), batch=batch)

@window.event 
def on_draw():
  window.clear()
  batch.draw()


pyglet.app.run()