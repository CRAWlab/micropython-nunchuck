import machine
import time

import nunchuck

# These pins match I2C2 on the HiBot M4
# Note that we've slow the i2c bus down to 10000, I was getting errors otherwise
nun = nunchuck.Nunchuck(machine.I2C(
        scl=machine.Pin('PF0'),
        sda=machine.Pin('PF1'),
        freq=10000
        ))

x = 0
y = 0
while True:
# You can uncomment below to have x,y change like a mass under velocity control
#     if not nun.joystick_center():
#         if nun.joystick_up():
#             y += 1
#         elif nun.joystick_down():
#             y -= 1
#         if nun.joystick_left():
#             x -= 1
#         elif nun.joystick_right():
#             x += 1
#     print(x, y, nun.joystick_x(), nun.joystick_y())

    # get the values of the joystick, the accelerometer, and buttons
    j = nun.joystick()
    a = nun.accelerator()
    b = nun.buttons()

    # Just print out the values
    print("\033[2J\033[;H") # Sending this string will clear most termianls
    print(' Reading a Wii Nunchuk with MicroPython on a HiBot M4')
    print(' ----------------------------------------------------')
    print(" Joystick: X={0: <3} Y={1: <3} \r\n Accel:    X={2: <3} Y={3: <3} Z={4: <3} \r\n Buttons:  C={5:<9} Z={6:<6}".format(
            j[0], j[1],
            a[0], a[1], a[2],
            str(b[0]), str(b[1])
            ))

    time.sleep_ms(100)
