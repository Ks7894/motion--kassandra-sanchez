while True:
    if input.rotation(Rotation.PITCH) > 2:
        light.show_animation(light.rainbowAnimation, 600)
else:
       light.clear()


while True:
    if input.acceleration(Dimension.X) > 2:
        light.show_animation(light.rainbowAnimation, 600)
else:
       light.clear()


while True:
    if input.acceleration(Dimension.Z) > 0 or input.acceleration(Dimension.Z) <0 :
        light.show_animation(light.rainbowAnimation, 600)
    else:
        light.clear()
