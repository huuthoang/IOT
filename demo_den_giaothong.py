# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:37:43 2020

@author: huuthoang
"""
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
board.digital[3].write(1)
board.digital[7].write(1)
"""while True:
    for i in range(3,7):
        board.digital[i].write(1)
    time.sleep(10)
    for i in range(3,7):
        board.digital[i].write(0)
    for i in range(3,7):
        board.digital[i].write(1)
    time.sleep(15)
    for i in range(3,7):
        board.digital[i].write(0)
    for i in range(3,7):
        board.digital[i].write(1)
    time.sleep(5)
    for i in range(3,7):
        board.digital[i].write(0)"""
