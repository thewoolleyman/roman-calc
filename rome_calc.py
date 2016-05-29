import sys, getopt
#remove all pluses from args array then concatenate remainder

filtered_args = filter(lambda arg: arg != "+", sys.argv[1:])
result = "".join(filtered_args)
if (result == "IIII"):
    print "IV"
else:
    print result
