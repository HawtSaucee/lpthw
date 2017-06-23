name = 'Breandon V. Shumate'
age = 12 # not a lie
height = 63 # inches
weight = 111 # lbs
eyes = 'brown'
teeth = 'white'
hair = 'brown'

print "Lets talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually thats not that heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + weight + weight)

centimeters_per_inch = 2.54
pounds_per_kilogram = 2.2
height_in_centimeters = height * centimeters_per_inch
weight_in_kilograms = weight / pounds_per_kilogram
print "He's %i centimeters tall." % height_in_centimeters
print "He weighs %i kilograms" % weight_in_kilograms
