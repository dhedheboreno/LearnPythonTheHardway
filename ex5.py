my_name = 'Munawar Syukur'
my_age = 34 # Just last month
my_height = 175 # centimeter
my_weight = 80 # kilograms
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "let's talk about %s." % my_name
print "He's %d centimeter tall." % my_height
print "he's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

# put this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
