import RPi.GPIO as GPIO  
import time  
# blinking function  
def blink(pin,pin2):  
        GPIO.output(pin,GPIO.HIGH)  
       	time.sleep(1)
	GPIO.output(pin2,GPIO.HIGH)
	time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)
	GPIO.output(pin2,GPIO.LOW)
	time.sleep(1)  
        return  
def blink2(pin):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)
	return
# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
GPIO.setup(15, GPIO.OUT)  
GPIO.setup(16, GPIO.OUT)
# blink GPIO17 50 times 
for i in range(0,50): 
	blink(15,16)
	#blink2(16)
GPIO.cleanup()  
 
