import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

good = 12
bad = 11

GPIO.setup(good, GPIO.OUT)
GPIO.setup(bad, GPIO.OUT)

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def go():
    GPIO.output(bad, 1)

if __name__ == '__main__':
    go()
