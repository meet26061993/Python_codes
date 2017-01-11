mport random
import sys
random_number=random.randint(1,10)
random_number=int(random_number)
while 1:
    guess_number=input("Please enter guess number: ")
    if guess_number > random_number:
        print"guess lower"
    elif guess_number< random_number:
        print"guess higher"
    elif guess_number==random_number:
        print "you are correct"
        print" the number is ", random_number
        sys.exit()
    else:
        print"something is wrong. Please try again"
            
