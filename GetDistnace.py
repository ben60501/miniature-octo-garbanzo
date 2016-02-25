import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 12
ECHO = 16

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

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

getMeasurment()

GPIO.cleanup()
