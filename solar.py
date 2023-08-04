from ursina import *
import math
import random

app = Ursina()
camera = EditorCamera()

def update():
    # Rotate the camera based on mouse input
    camera.rotation_y += held_keys['right mouse'] * mouse.delta[0] * 100
    camera.rotation_x -= held_keys['right mouse'] * mouse.delta[1] * 100

# Set the background color to black
window.color = color.black

# Create stars
stars = []
num_stars = 7000
for _ in range(num_stars):
    star = Entity(model='sphere', scale=random.uniform(0.04, 0.04), position=(random.uniform(-50, 50), random.uniform(-50, 50), random.uniform(-50, 50)), color=color.white)
    stars.append(star)

# Create the Sun
sun_texture = load_texture('sun_texture.jpg')
sun = Entity(model='sphere', texture=sun_texture, scale=2)

# Create the mercury
mercury_texture = load_texture('mercury_texture.jpg')
mercury = Entity(model='sphere', texture=mercury_texture, scale=0.8)

# Create the Venus
venus_texture = load_texture('venus_texture.jpg')
venus = Entity(model='sphere', texture=venus_texture, scale=0.9)

# Create the Earth
earth_texture = load_texture('earth_texture.jpg')
earth = Entity(model='sphere', texture=earth_texture, scale=1)

# Create the mars
mars_texture = load_texture('mars_texture.jpg')
mars = Entity(model='sphere', texture=mars_texture, scale=0.6)

# Create the jupitar
jupitar_texture = load_texture('jupitar_texture.jpg')
jupitar = Entity(model='sphere', texture=jupitar_texture, scale=1.5)

# Create the saturn
saturn_texture = load_texture('saturn_texture.jpg')
saturn = Entity(model='sphere', texture=saturn_texture, scale=1.4)

# Create the uranus
uranus_texture = load_texture('uranus_texture.jpg')
uranus = Entity(model='sphere', texture=uranus_texture, scale=0.8)

# Create the neptune
neptune_texture = load_texture('neptune_texture.jpg')
neptune = Entity(model='sphere', texture=neptune_texture, scale=0.7)

# Set the mercury position relative to the Sun
mercury_orbit_radius = 2
mercury.position = Vec3(mercury_orbit_radius, 0, 0)

# Set the venus's position relative to the Sun
venus_orbit_radius=4
venus.position = Vec3(venus_orbit_radius, 0, 0)

# Set the Earth's position relative to the Sun
earth_orbit_radius = 6
earth.position = Vec3(earth_orbit_radius, 0, 0)

# Set the mars's position relative to the Sun
mars_orbit_radius=8
mars.position = Vec3(mars_orbit_radius, 0, 0)

# Set the jupitar's position relative to the Sun
jupitar_orbit_radius=10
jupitar.position = Vec3(jupitar_orbit_radius, 0, 0)

# Set the saturn's position relative to the Sun
saturn_orbit_radius=12
saturn.position = Vec3(saturn_orbit_radius, 0, 0)

# Set the uranus's position relative to the Sun
uranus_orbit_radius=14
uranus.position = Vec3(uranus_orbit_radius, 0, 0)

# Set the neptune's position relative to the Sun
neptune_orbit_radius=16
neptune.position = Vec3(neptune_orbit_radius, 0, 0)

# Set rotation speeds
mercury_rotation_speed = 0.1
venus_rotation_speed = 0.2
earth_rotation_speed = 0.3
mars_rotation_speed = 0.25
jupitar_rotation_speed = 0.15
saturn_rotation_speed = 0.1
uranus_rotation_speed = 0.05
neptune_rotation_speed = 0.03
sun_rotation_speed = 3

# Set up camera for top view
# camera.position = (0, 55, 0)  # Positioned above the scene
# camera.rotation_x = 90    # Look at the scene from above

# Zoom settings
zoomed_in = False
zoomed_distance = 10

# Function to update the Earth's position for rotation
def update():
    global zoomed_in

    mercury.rotation_y += time.dt * mercury_rotation_speed
    mercury.x = mercury_orbit_radius * math.cos(mercury.rotation_y)
    mercury.z = mercury_orbit_radius * math.sin(mercury.rotation_y)

    venus.rotation_y += time.dt * venus_rotation_speed
    venus.x = venus_orbit_radius * math.cos(venus.rotation_y)
    venus.z = venus_orbit_radius * math.sin(venus.rotation_y)

    earth.rotation_y += time.dt * earth_rotation_speed
    earth.x = earth_orbit_radius * math.cos(earth.rotation_y)
    earth.z = earth_orbit_radius * math.sin(earth.rotation_y)

    mars.rotation_y += time.dt * mars_rotation_speed
    mars.x = mars_orbit_radius * math.cos(mars.rotation_y)
    mars.z = mars_orbit_radius * math.sin(mars.rotation_y)

    jupitar.rotation_y += time.dt * jupitar_rotation_speed
    jupitar.x = jupitar_orbit_radius * math.cos(jupitar.rotation_y)
    jupitar.z = jupitar_orbit_radius * math.sin(jupitar.rotation_y)

    saturn.rotation_y += time.dt * saturn_rotation_speed
    saturn.x = saturn_orbit_radius * math.cos(saturn.rotation_y)
    saturn.z = saturn_orbit_radius * math.sin(saturn.rotation_y)

    uranus.rotation_y += time.dt * uranus_rotation_speed
    uranus.x = uranus_orbit_radius * math.cos(uranus.rotation_y)
    uranus.z = uranus_orbit_radius * math.sin(uranus.rotation_y)

    neptune.rotation_y += time.dt * neptune_rotation_speed
    neptune.x = neptune_orbit_radius * math.cos(neptune.rotation_y)
    neptune.z = neptune_orbit_radius * math.sin(neptune.rotation_y)
    
    sun.rotation_y += time.dt * sun_rotation_speed
    
    if held_keys['q']:
        if not zoomed_in:
            camera.position = (0, 50, 0)  
            camera.rotation_x = 90   
            zoomed_in=True
    elif held_keys['w']:
        if not zoomed_in:
            camera.position = (0, 0, -10)  
            camera.rotation_x = 0
            zoomed_in=True
    elif held_keys['e']:
        if not zoomed_in:
            camera.position = (-2, 0, -20)  
            camera.rotation_x = 0
            zoomed_in=True
    else:
        if zoomed_in:
            camera.position = (0, 0, -20)  
            camera.rotation_x = 0
            zoomed_in = False


app.run()
