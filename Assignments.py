def printLine():
	print "------------"
	print 
	return


def print2vars( intA, intB ):
	print "A is: " 
	print intA
	print "B is: "
	print intB
	printLine();
	return



# Basics
x = 4
print x
a,b = 1, 2

print2vars(a, b);

# Switch the Variables 
a, b = b, a
print "After the switch"
print2vars(a, b);

# Problem 4
print "Problem 4"
x = 4
y = x + 1
x = 2
print2vars(x, y);

# Problem 5
print "Problem 5"
x, y = 2, 6
x, y = y, x + 2
print2vars(x, y)

# Problem 6
print "Problem 6"
a, b, c = 2, 3, 0
c, b = a, c + 1
print a, b, c



