from time import sleep
import RPi.GPIO as GPIO
import requests


GPIO.setmode(GPIO.BOARD)

# button positions used on the board
# buttonA is entering cars
# buttonB is exiting cars
buttonA = 16
buttonB = 12

GPIO.setup(buttonA, GPIO.IN , pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonB, GPIO.IN , pull_up_down = GPIO.PUD_UP)

payload = {"name":"North Springs","totalSpaces":2378}
requests.post("http://192.168.0.58:8080/api/v1/makeLot", json = payload)

# while we want to receive data 
while(True):

    if GPIO.input(buttonA) == 0:
        # send increment to server
        #payload values?
        payload = {"name":"North Springs"}
        requests.post("http://192.168.0.58:8080/api/v1/increment", json = payload)
        sleep(.1)

    if GPIO.input(buttonB) == 0:
        # send decrement to server
        #payload values?
        payload = {"name":"North Springs"}
        requests.post("http://192.168.0.58:8080/api/v1/decrement", json = payload)
        sleep(.1)

    
    
