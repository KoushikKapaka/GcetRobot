import Jetson.GPIO as GPIO
import time
def forward():
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(1)
    print("f")
    while(True):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        s=input()
        if s=='b':
            return 1
        if s=='q':
            return 0
        else:
            continue
def backward():
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(1)
    print("b")
    while(True):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        s=input()
        if s=='f':
            return 1
        if s=='q':
            return 0
        else:
            continue
# for 1st Motor on ENA
ENA = 33
IN1 = 35
IN2 = 37


# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize EnA, In1 and In2
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
a=0
b=0
left_pwm = GPIO.PWM(ENA, 100)
# right_pwm = GPIO.PWM(right_pins[2], 100)
GPIO.output(ENA, GPIO.HIGH)
while(True):
    s=''
    print("entered while")
    if a==0 or b==0:
        s=input()
    if s=='f' or b==1:
        print(s)
        a=forward()
        if a==0:
            GPIO.output(ENA, GPIO.LOW)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            break
    if s=='b' or a==1:
        b=backward()
        if b==0:
            GPIO.output(ENA, GPIO.LOW)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            break
GPIO.output(ENA, GPIO.LOW)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
time.sleep(1)
        
GPIO.cleanup()
