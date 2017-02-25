from time import sleep
import RPi.GPIO as GPIO
import requests

GPIO.setmode(GPIO.BOARD)

# button positions on the red board
# button 1 is car entering
# button 2 is car exiting
button1 = 16
button2 = 12

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# initialize lots
payload = {"North Springs":500}
requests.post('http://localhost:8080/api/v1/makeLot', json = payload)

# while we want to collect data
while(true):

        if GPIO.input(button1) == 0:
                payload = {"North Springs": 500}
                requests.post('http://localhost:8080/api/v1/increment', json = payload)
                sleep(.1)
                # send increment to server
        
        if GPIO.input(button2) == 0:
                payload = {"North Springs":500}
                # send decrement to server
                requests.post('http://localhost:8080/api/v1/decrement', json = payload)
                sleep(.1)
