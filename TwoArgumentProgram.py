# Take in two arguments and add them together
import sys

print
print
print
print
print "Arguments"
print "-----------------"
for arg in sys.argv[1:]:
	print arg


print "Total Arguments: ", len(sys.argv) - 1

print "Var 1: %d    Var 2: %d" % (int(sys.argv[1]), int(sys.argv[2]))
print "Fist Two Argments Sum: ", int(sys.argv[1]) + int(sys.argv[2])

print ''' This is how you print a %  '''