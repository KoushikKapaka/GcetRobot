import Jetson.GPIO as GPIO
from time import sleep
def forward():
    print('f')
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    sleep(1)
    print("f")
    while(True):
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        s=input()
        if s=='b':
            return 1
        elif s=='q':
            return 0
        elif s=='r':
            return 2
        elif s=='l':
            return 3
        else:
            continue
def left():
    print('l')
    while(True):
        left_pwm.ChangeDutyCycle(50)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        right_pwm.ChangeDutyCycle(50)
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        s=input()
        if s=='f':
            return 1
        elif s=='b':
            return -1
        elif s=='q':
            return 0
        elif s=='r':
            return 2
        else:
            continue
def right():
    print('r')
    while(True):
        left_pwm.ChangeDutyCycle(50)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        right_pwm.ChangeDutyCycle(50)
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        s=input()
        if s=='f':
            return 1
        elif s=='b':
            return -1
        elif s=='l':
            return 3
        elif s=='q':
            return 0
        else:
            continue
def backward():
    print('b')
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN4, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    sleep(1)
    while(True):
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN4, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        s=input()
        if s=='f':
            return 1
        elif s=='q':
            return 0
        elif s=='r':
            return 2
        elif s=='l':
            return 3
        else:
            continue

# motor 1
ENA = 32
IN1 = 35
IN2 = 37
# motor 2
ENB=33
IN3=7
IN4=11
# setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENB, GPIO.HIGH)
left_pwm = GPIO.PWM(ENA, 255)
right_pwm = GPIO.PWM(ENB, 255)
left_pwm.start(0)
right_pwm.start(0)

a=0
b=0
r=0
l=0
# left_pwm = GPIO.PWM(ENA, 100)
# right_pwm = GPIO.PWM(ENB, 100)
# GPIO.output(ENA, GPIO.HIGH)
# GPIO.output(ENB, GPIO.HIGH)
while(True):
    s=''
    print("entered while")
    if a==0 and b==0:
        s=input()
    if s=='f' or b==1:
        b=0
        print(s)
        a=forward()
        if a==0:
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.LOW)
            break
        if a==2:
            r=1
            l=0
        if a==3:
            l=1
            r=0
        
    if(s=='b' or a==1 ):
        a=0
        b=backward()
        if b==0:
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.LOW)
            break
        if b==2:
            r=1
            l=0
        if b==3:
            l=1
            r=0
    if r==1:
        r=right()
        if r==0:
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.LOW)
            break
        if r==3:
            l=1
        if r==-1:
            a=1
        if r==1:
            b=1
    if l==1:
        l=left()
        if l==0:
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.LOW)
            GPIO.output(IN3, GPIO.LOW)
            GPIO.output(IN4, GPIO.LOW)
            break
        if l==1:
            b=1
        if l==-1:
            a=1
        if l==2:
            r=1
            l=0

    
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
sleep(1)
        
        
# Stop
# GPIO.output(ENA, GPIO.HIGH)
# GPIO.output(IN1, GPIO.LOW)
# GPIO.output(IN2, GPIO.LOW)
# time.sleep(1)

# # Forward
# GPIO.output(IN1, GPIO.HIGH)
# GPIO.output(IN2, GPIO.LOW)
# time.sleep(1)

# # Stop
# GPIO.output(IN1, GPIO.LOW)
# GPIO.output(IN2, GPIO.LOW)
# time.sleep(1)

# # Backward
# GPIO.output(IN1, GPIO.LOW)
# GPIO.output(IN2, GPIO.HIGH)
# time.sleep(1)

# # Stop
# GPIO.output(ENA, GPIO.LOW)
# GPIO.output(IN1, GPIO.LOW)
# GPIO.output(IN2, GPIO.LOW)
# time.sleep(1)

GPIO.cleanup()
