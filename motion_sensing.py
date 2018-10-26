import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pripin= 7
GPIO.setup(pirpin, GPIO.IN)
encounter=2
time.sleep(3)
while counter<=4:
	if GPIO.input(pirpin):
		print("something is moving")
		os.system("fswebcam -F 4 --fps 12 -r 400*600 /home/cl216/Desktop/"+str(mass)+".jpg")
		print("smily")
		time.sleep(2)
 		encounter = encounter + 1
print("checking")
exit()