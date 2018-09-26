a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
p=int(input("what do you want to do? 1,2,3,4,5,6: "))
def add():
	return a+b
def sub():
	return a-b
def mul():
	return a*b
def divide():
	return a/b
def remainder():
	return a%b
def sqrt():
	return a*b
if(p==1):
	print(" addition= ",add())
if(p==2):
	print(" subtraction= ",sub())
if(p==3):
	print(" multiplication= ",mul())
if(p==4):
	print("Division= ",divide())
if(p==5):
	print("remainder= ",remainder())
if(p==6):
	print("square root= ",sqrt())