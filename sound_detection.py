import RPi.GPIO as GPIO
import time

import email_sender


sensor = 11
buzzer = 18


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)


GPIO.output(buzzer,False)
print ("Initialzing Sound Detection Sensor......")
time.sleep(5)
print ("Sound Detection Ready...")
print (" ")
f = open("activation.txt", "r")

def callback(sensor):
    f.seek(0)
    if GPIO.input(sensor) and f.read()=="active":
        print ("Sound Detected")
        GPIO.output(buzzer,True)
        time.sleep(0.3)
        GPIO.output(buzzer,False)
        email_sender.send_mail('s.a.j.1381110@gmail.com')
        f.seek(0)

    else:
        #GPIO.output(buzzer,False)
        print ("Sound Detected")


GPIO.add_event_detect(sensor, GPIO.BOTH, bouncetime=3000)
GPIO.add_event_callback(sensor, callback)
while True:
    time.sleep(1)
    
f.close()

