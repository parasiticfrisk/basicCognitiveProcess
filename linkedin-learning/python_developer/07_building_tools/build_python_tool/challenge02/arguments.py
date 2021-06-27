import sys

args = sys.argv

if len(args) > 2:
    print("Good %s, %s" % (args[1], args[2]))
else:
    print("I need two or more arguments!")
    quit()