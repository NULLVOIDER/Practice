 import RPi.GPIO as GPIO  
 import time 
 led = 11  
 GPIO.setmode( GPIO.BOARD)  
 GPIO.setup( led, GPIO.OUT)
 pwm_led = GPIO.PWM( led, 50) 
 pwm_led.start(100)  
 try:  
   while True:  
     duty_s = raw_input("Enter Brightness Value (0 to 100):") 
     duty = int(duty_s)  
     pwm_led.ChangeDutyCycle(duty)  
     time.sleep(0.5)  
 except KeyboardInterrupt:  
   print "Exiting Program"  
 except:  
   print "Error Occurs, Exiting Program"  
 finally:  
   GPIO.cleanup()  