name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74 # inches
height_centimeters = height_inches * 2.54 #centimeters
weight_bs = 180 # lbs
weight_kg = weight_bs * 0.45 #kg

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %r." %name)
print("He's %r centimeters tall." %height_centimeters)
print("He's %r kg heavey." %weight_kg)
print("Actually that's not too heavey")
print("He's got %r eyes and %r hair." %(eyes,hair))

#this line is tricky, try to get it exactly right
print("If I add %r, %r, and %r I get %r." %(age,height_centimeters,weight_kg,age + height_centimeters + weight_kg))