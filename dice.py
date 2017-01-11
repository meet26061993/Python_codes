
import random
import sys
e=raw_input("Do you want to use dice? Press 4 \n")
if e == '4':
    print "yes"
    while 1:
        print "Please press 1 to toss dice or press 2 to escape :"
        f=raw_input()
        if f=='1':
            g=random.randint(1,6)
            print "The dice output is", g
        else:
            print"quitting"
            sys.exit()
            