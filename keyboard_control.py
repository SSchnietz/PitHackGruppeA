from djitellopy import tello
import cv2
import threading
import keyboard
me = tello.Tello()
me.connect()
print(me.get_battery())
def stream():
    me.streamon()
    while True:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (1280, 720)) #360;240 ## 1280 x720
        cv2.imshow("Image", img)
        cv2.waitKey(1)

stream_thread = threading.Thread(target=stream, name="stream")
stream_thread.start()

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