from sys import argv

thing = argv[1]
print "Do you like %s [y/n]? " % thing,
answer = raw_input()
if answer == "y":
    print "Yes %s are pretty good!" % thing
else:
    print "No %s are not good at all!" % thing
