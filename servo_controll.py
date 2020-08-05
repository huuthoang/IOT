from pyfirmata import Arduino, util
import time
board = Arduino('COM3')
servo = board.get_pin('d:9:s')
while 1:
    servo.write(180)
    time.sleep(2)
    servo.write(0)
    time.sleep(2)  
