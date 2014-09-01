# Take in two arguments and add them together
import sys
import unittest


def two_arguments_sys_argv():
    print
    print
    print
    print
    print "Add 2 Arguments with sys.argv[]"
    print "-----------------"
    for argument in sys.argv[1:]:
        print argument

    print "Total Arguments: ", len(sys.argv) - 1

    print "Var 1: %d    Var 2: %d" % (int(sys.argv[1]), int(sys.argv[2]))
    print "Fist Two Argments Sum: ", int(sys.argv[1]) + int(sys.argv[2])

    print ''' This is how you print a %  '''
    print
    print
    print
    return


def two_arguemnts_addition(args):
    print
    print
    print
    print
    print "Add 2 Arguments with *self"
    print "-----------------"
    print "Arguments: ", args
    print "Total Arguments: ", len(args)
    print "Arguments List: "
    for arg in args:
        print arg

    # if len(arg) > 1:
    # 	print "Var 1: %d    Var 2: %d" % (int(arg[0]), int(arg[1])
    # 	#print "Fist Two Argments Sum: ", int(arg[0]) + int(arg[1])

    print ''' This is how you print a %  '''
    print
    print
    print
    return args

if __name__ == '__main__':
    # two_arguments_sys_argv()

    if len(sys.argv) == 1:
        print "Please give program some input ints"

    else:
        two_arguemnts_addition(sys.argv[1:])
