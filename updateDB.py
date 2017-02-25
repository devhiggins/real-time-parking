import RPi.GPIO as GPIO
import sqlite3
import time, datetime

current_time = "2017-02-25 11:35:47"
GPIO.setmode(GPIO.BOARD)

# button positions used on the board
# buttonA is entering cars
# buttonB is exiting cars
buttonA = 16
buttonB = 12

GPIO.setup(buttonA, GPIO.IN , pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonB, GPIO.IN , pull_up_down = GPIO.PUD_UP)
conn = sqlite3.connect("MARTA.db")
conn.commit()
c = conn.cursor()
c.execute('''INSERT INTO parking_info VALUES('North Springs', 500)''')


# while we want to receive data 
while(True):

    if GPIO.input(buttonA) == 0:
        c.execute('''UPDATE parking_info SET open_spaces = open_spaces + 1''')
        c.execute("SELECT * FROM parking_info")
        print(c.fetchone())
        time.sleep(1)

    if GPIO.input(buttonB) == 0:
        c.execute('''UPDATE parking_info SET open_spaces = open_spaces - 1''')
        c.execute("SELECT * FROM parking_info")
        print(c.fetchone())
        time.sleep(1)

    
    
