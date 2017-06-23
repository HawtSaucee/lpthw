# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# simpler version of above fuction
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one take no arguments
def print_none():
    print "not enough people main zen'."

print_two("MLG genji main", "NOOB hanzo main")
print_two_again("MLG genji main", "NOOB hanzo main")
print_one("and nobody mains winston")
print_none()
