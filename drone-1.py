from djitellopy import Tello


tello = Tello()
tello.connect()
print('Battery:', tello.get_battery())
'''
tello.move_forward(100)

tello.land()
'''
def fly_square():
    i = 0
    while i < 4:
        tello.move_forward(100)
        tello.rotate_clockwise(90)
        print('Battery:', tello.get_battery())
        i = i + 1

def fly_triangle():
    i = 0
    while i < 3:
        tello.move_forward(100)
        tello.rotate_clockwise(120)
        print('Battery:', tello.get_battery())
        i = i + 1
    
print('Battery:', tello.get_battery())
tello.takeoff()
#fly_square()
fly_triangle()