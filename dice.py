from random import randint

print "Welcome to the dice roller."
print "What are your odds?"
print "roll the 2 six sided dice and see!"

def roll_dice():
    result = randint(1, 6)
    return result
# if you comment out line 12 and line 13 change total at the end of 15 to die0
die0 = roll_dice()
die1 = roll_dice()
total = die0 + die1

print "What are the odds!? You rolled a %i !" % total
