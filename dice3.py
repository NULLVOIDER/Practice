import random

while True:
	s=input("press 'r' to roll the dice and 'q' to quit")
	if(s=='r'):
		print(random.randint(1,6))
	elif(s=='q'):
		print("GOOD BYE !")
		break
	else:
		print("enter either 'r' or 'q'")