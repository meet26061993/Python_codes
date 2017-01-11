
import sys

def numberdetector(a):
    k="Is the number"+str(a-1)+"?"
    r=input(k)
    if r==1:
        g="Your guess number is"+str(a-2)+"."
        print g
        sys.exit()
    elif r==3:
        g="Your guess number is"+a-1+"."
        print g
        sys.exit()
    else:
        print"You are a fucking moron."
        
    
print"I will try to guess your number. guess number between 1 and 10."
print"Instructions: Press 1 to go lower, press 2 to go higher or press 3 if I detect your number perfectly."
r=input("Is the number 5?")
if r==1:
    r=input("Is the number 2?")
    if r==1:
        numberdetector(2)
    elif r==2:
        numberdetector(5)
    elif r==3:
        print"Your guess number is 2."
        sys.exit()
    else:
        print"sorry wrong input."
elif r==2:
    r=input("Is the number 8?")
    if r==1:
        numberdetector(8)
    elif r==2:
        numberdetector(11)
    elif r==3:
        print"Your guess number is 8."
        sys.exit()
    else:
        print"sorry wrong input."
elif r==3:
    print"Your guess number is 5."
else: 
    print"It is a wrong input."
    
