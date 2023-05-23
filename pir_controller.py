import RPi.GPIO as GPIO
import time

import email_sender


sensor = 15
buzzer = 18


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)


GPIO.output(buzzer,False)
print ("Initialzing PIR Sensor......")
time.sleep(13)
print ("PIR Ready...")
print (" ")
f = open("activation.txt", "r")



try:
    while True:
        f.seek(0)
        if GPIO.input(sensor) and f.read()=="active":
            f.seek(0)
            print ("Motion Detected")
            GPIO.output(buzzer,True)
            time.sleep(0.2)
            GPIO.output(buzzer,False)
            email_sender.send_mail('s.a.j.1381110@gmail.com')
            while GPIO.input(sensor):
                time.sleep(0.8)
        else:
            #GPIO.output(buzzer,False)
            time.sleep(1)
except KeyboardInterrupt:
    #GPIO.cleanup()

    f.close()
