#####################################
#      Copyright Steven Feind       #
#####################################

from contextlib import redirect_stderr
from djitellopy import tello
import cv2
import threading
import keyboard
#print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnter commands only if the video is available!')
me = tello.Tello()
me.connect()
print(me.get_battery())
def stream():
    me.streamon()
    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (720, 480)) #360;240 ## 1280 x720
        cv2.imshow("Image", img)
        cv2.waitKey(1)

stream_thread = threading.Thread(target=stream, name="stream")
stream_thread.start()

print("Booting command console...")
while True:
    #print("test output here")
    commandinput = input('Console command >>>')
    if commandinput == 'ff':
        me.move_forward(100)
    if commandinput == 'sff':
        me.move_forward(300)
    if commandinput == 'f':
        me.move_forward(20)
    if commandinput == 'fb':
        me.move_back(100)
    if commandinput == 'b':
        me.move_back(20)
    if commandinput == 'fu':
        me.move_up(100)
    if commandinput == 'u':
        me.move_up(20)
    if commandinput == 'fd':
        me.move_down(100)
    if commandinput == 'd':
        me.move_down(20)
    if commandinput == 'frl':
        me.rotate_counter_clockwise(90)
    if commandinput == 'rl':
        me.rotate_counter_clockwise(30)
    if commandinput == 'frr':
        me.rotate_clockwise(90)
    if commandinput == 'rr':
        me.rotate_clockwise(30)
    if commandinput == 'land':
        me.land()
    if commandinput == 'takeoff':
        me.takeoff()
    if commandinput == 'kill':
        me.land()
        break
    if commandinput == 'help':
        print('Help: f=forward, b=backward, u=up, d=down,\nrl=rotate left, rr=rotate right, land=land, takeoff=takeoff;\nfast is an amplifier, use f[cmd]')
    print('USER issued server command:', commandinput)
    print('Battery:', me.get_battery(), '%')

'''
while True:
    if keyboard.is_pressed('w') and keyboard.is_pressed('right shift'):
        me.move_forward(100)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('s') and keyboard.is_pressed('right shift'):
        me.move_back(100)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('d') and keyboard.is_pressed('right shift'):
        me.rotate_clockwise(90)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('a') and keyboard.is_pressed('right shift'):
        me.rotate_counter_clockwise(90)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('left shift') and keyboard.is_pressed('right shift'):
        me.move_down(100)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('space') and keyboard.is_pressed('right shift'):
        me.move_up(100)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('w'):
        me.move_forward(20)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('s'):
        me.move_back(20)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('esc'):
        me.land()
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('d'):
        me.rotate_clockwise(30)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('a'):
        me.rotate_counter_clockwise(30)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('space'):
        me.move_up(20)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('left shift'):
        me.move_down(20)
        print('Battery:', me.get_battery(), '%')
    if keyboard.is_pressed('p'):
        me.takeoff()
        print('Battery:', me.get_battery(), '%')
me.land()
'''
