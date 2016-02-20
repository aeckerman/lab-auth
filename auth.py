import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

good = 12
bad = 11

on = GPIO.HIGH
off = GPIO.LOW

GPIO.setup(good, GPIO.OUT)
GPIO.setup(bad, GPIO.OUT)

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def go():
	password = input('Password: ')

	if password == 'boyroom':
		GPIO.output(good, on)
	if password != 'boyroom':
		GPIO.output(bad, on)

	sleep(100)

if __name__ == '__main__':
    go()
    GPIO.cleanup()
