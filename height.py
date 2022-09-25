from djitellopy import Tello


tello = Tello()
tello.connect()
print('Battery:', tello.get_battery())
setheight=int(input('add or remove height: '))
movedistance=int(input('move distance?'))
tello.takeoff()
print('Battery:', tello.get_battery())
print('height:', tello.get_height())
endheight = tello.get_height() + setheight
tello.move_up(endheight)
tello.move_forward(movedistance)
tello.land()
print('Battery:', tello.get_battery())