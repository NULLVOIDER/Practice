import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("Press R to roll the dice")
	if(n=='R'):
		R=myroll()
		count=count+R
		print("YOU GOT",R)
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