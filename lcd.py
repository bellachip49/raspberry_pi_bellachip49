import RPi.GPIO as GPIO
import lcddriver
#!/user/bin/env python

lcd = lcddriver.lcd()
lcd.lcd_clear();

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

lcd.lcd_display_string("Hello World!") 
