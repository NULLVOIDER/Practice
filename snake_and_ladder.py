import random
count=0
def my roll():
	return random.radiant(1,6)

while(count==100):
	n=input("Press ENTER to roll the dice")
	if(n=='ENTER'):
		ENTER=myroll()
		count=count+r
		print("YOU GOT",ENTER)
		print("NEW POSITION IS",count)

		if(count==8):
			count=37
			print("i got the ladder i'm climbing to the num 37")
		elif(count==11):
			count=2
			print("what the hell a snake bit me now i got back to the num 2")
		elif(count==13):
			count=34
			print("i got the ladder i'm climbing to the num 34")
		elif(count==38):
			count=9
			print("what the hell a snake bit me now i got back to the num 9")
		elif(count==40):
			count=68
			print("i got the ladder i'm climbing to the num 68")
		elif(count==52):
			count=81
			print("i got the ladder i'm climbing to the num 81")
		elif(count==65):
			count=46
			print("what the hell a snake bit me now i got back to the num 46")
		elif(count==76):
			count=97
			print("i got the ladder i'm climbing to the num 97")
		elif(count==89):
			count=70
			print("what the hell a snake bit me now i got back to the num 70")
		elif(count==93):
			count=64
			print("what the hell a snake bit me now i got back to the num 64")
leaveprogram=0
while leaveprogram != "q":
    import random
    print("This is a dice rolling program")
    print("press r to roll")
    input()
    number=random.randint(1,6)
    if number==1:
        print("[-------------]")
        print("[             ]")
        print("[      ●      ]")
        print("[             ]")
        print("[-------------]")
        print()
        print("Type 'q' to quit")
        leaveprogram=input()
    if number==2:
        print("[-------------]")
        print("[             ]")
        print("[   ●      ●  ]")
        print("[             ]")
        print("[-------------]")
        print()
        print("Type 'q' to quit")
        leaveprogram=input()
    if number==3:
        print("[-------------]")
        print("[   ●     ●   ]")
        print("[             ]")
        print("[      ●      ]")
        print("[-------------]")
        print()
        print("Type 'q' to quit")
        leaveprogram=input()
    if number==4:
        print("[-------------]")
        print("[   ●     ●   ]")
        print("[             ]")
        print("[   ●     ●   ]")
        print("[-------------]")
        print()
        print("Type 'q' to quit")
        leaveprogram=input()
    if number==5:
        print("[-------------]")
        print("[   ●     ●   ]")
        print("[      ●      ]")
        print("[   ●     ●   ]")
        print("[-------------]")
        print()
        print("Type 'q' to quit")
        leaveprogram=input()
    if number==6:
        print("[-------------]")
        print("[   ●     ●   ]")
        print("[   ●     ●   ]")
        print("[   ●     ●   ]")
        print("[-------------]")
        print()
        print("Type 'q' to quit")
        leaveprogram=input()