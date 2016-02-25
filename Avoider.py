import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 12
ECHO = 16

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(7,GPIO.OUT)

GPIO.setup(13,GPIO.OUT)

def getMeasurment():
    GPIO.output(TIRG,0)

    time.sleep(0.1)

    print ("Starting Measurment...")

    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG,0)

    while GPIO.imput(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.imput(ECHO) == 1:
        pass
    stop = time.time()

    distance = (stop - start) * 17000
    print (distance)

    if distance > 20:
        moveForward()

def moveForward():
    GPIO.output(7,True)
    GPIO.output(13,True)
    time.sleep(1)
    GPIO.output(7,False)
    GPIO.output(13,False)

getMeasurment()

GPIO.cleanup()
