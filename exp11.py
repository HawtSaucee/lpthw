age = raw_input('How old are you? ')
height = raw_input('How tall are you? ')
weight = raw_input('How much do you weigh? ')
pickles = raw_input('Do you like pickles [y/n]? ')

print "so, you're %s years old, %s tall, and weigh %s pounds." % (age, height, weight)
if pickles == "y":
    print "You like pickles!"
else:
    print "So you're not a fan of pickles?!"
