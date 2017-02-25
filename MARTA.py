from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# button positions on the red board
# button 1 is car entering
# button 2 is car exiting
button1 = 16
button2 = 12

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

spaces = 500

# while we want to collect data
while(true):

        if GPIO.input(button1) == 0:
            if spaces < 500:
                 spaces += 1
				# send increment to server
                print ("car entered. Spaces available: ", spaces)
                sleep(.1)
            else if spaces == 500:
                print("lot is full")

        if GPIO.input(button2) == 0:
            if spaces > 0:
                spaces -= 1
                # send decrement to server
                print ("car exited. Spaces available: ", spaces)
                sleep(.1)
