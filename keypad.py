import RPi.GPIO as GPIO
import time

f = open('password.txt', 'r')
password = f.read()
f.close()


L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def check_password(current_password):
    password_string = ''
    a = read_input()
    print(a, end='')
    while a != '*':
        password_string = password_string + str(a)
        a = read_input()
        print(a, end='')
    print()
    return current_password == password_string


def get_string():
    given_string = ''
    b = read_input()
    print(b, end='')
    while b != '*':
        if b == '#':
            continue
        given_string = given_string + str(b)
        b = read_input()
        print(b, end="")
    print()
    return given_string


def change_password():
    print('Enter password:')
    global password
    if check_password(password):
        print('Enter new password:')
        new_password = get_string()
        print('Reenter password:')
        if check_password(new_password):
            password = new_password
            file = open('password.txt', 'w')
            file.write(password)
            file.close()
            print('Password changed successfully!')
        else:
            print('Password did not match!')
    else:
        print('Password is incorrect!')


def read_line(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        GPIO.output(line, GPIO.LOW)
        return characters[0]
    elif GPIO.input(C2) == 1:
        GPIO.output(line, GPIO.LOW)
        return characters[1]
    elif GPIO.input(C3) == 1:
        GPIO.output(line, GPIO.LOW)
        return characters[2]
    else:
        GPIO.output(line, GPIO.LOW)
        return None


def read_input():
    while True:
        time.sleep(0.157)
        a = read_line(L1, ['1', '2', '3'])
        if a is not None:
            return a
        a = read_line(L2, ['4', '5', '6'])
        if a is not None:
            return a
        a = read_line(L3, ['7', '8', '9'])
        if a is not None:
            return a
        a = read_line(L4, ['*', '0', '#'])
        if a is not None:
            return a


def listen_keypad():
    try:
        while True:
            a = read_input()
            if a == '#':
                change_password()
            if a == '*':
                global password
                print('Enter password:')
                if check_password(password):
                    f = open("activation.txt",'r')
                    if f.read() == "active":
                        f.close()
                        f = open("activation.txt",'w')
                        f.write("not active")
                        f.close()
                        print("system deactivated")
                    else:
                        f.close()
                        f= open("activation.txt",'w')
                        f.write("active")
                        f.close()
                        print("system activated")
                else:
                    print('Password is incorrect!')
    except KeyboardInterrupt:
        print("Application stopped!")
  
  
listen_keypad()

