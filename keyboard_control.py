import airsim
from pynput import keyboard

"""
AirSim Multirotor control using Keyboard Inputs

Usage: Launch environment and start the simulation
Launch (from another terminal): python keyboard_control.py

---------------------------------------------------------------------------

Arm    -> T
Disarm -> Y

               W                    |                   I
           (Forward)                |               (Ascend)
                                    |
     A         S         D          |        J          K           L
(Move Left)(Reverse)(Move Right)    |  (Rotate Left)(Descend)(Rotate Right)

---------------------------------------------------------------------------
"""



def on_press(key):
    try:
        if key.char == ("t"):     # Arm
          client.enableApiControl(True)
          client.armDisarm(True)
          client.takeoffAsync().join()
          print("Armed!")
        elif key.char == ("y"):     # Disarm
          client.landAsync().join()
          client.armDisarm(False)
          client.enableApiControl(False)
          print("Disarmed...")
        elif key.char == ("w"):       # Forward
          client.moveByVelocityBodyFrameAsync(3.0, 0.0, 0.0, 1.5)
        elif key.char == ("s"):     # Reverse
          client.moveByVelocityBodyFrameAsync(-3.0, 0.0, 0.0, 1.5)
        elif key.char == ("a"):     # Move Left
          client.moveByVelocityBodyFrameAsync(0.0, -2.0, 0.0, 1.5)
        elif key.char == ("d"):     # Move Right
          client.moveByVelocityBodyFrameAsync(0.0, 2.0, 0.0, 1.5)
        elif key.char == ("i"):     # Ascend
          client.moveByVelocityBodyFrameAsync(0.0, 0.0, -1.5, 1.5)
        elif key.char == ("k"):     # Descend
          client.moveByVelocityBodyFrameAsync(0.0, 0.0, 1.5, 1.5)
        elif key.char == ("j"):     # Rotate left
          client.rotateByYawRateAsync(-20.0, 1.5)
        elif key.char == ("l"):     # Rotate right
          client.rotateByYawRateAsync(20.0, 1.5)
        # else:                       # No key pressed
          # client.moveByVelocityBodyFrameAsync(0, 0, 0, 1.5).join()
          # client.hoverAsync().join()
          # print("Hovering...")
        
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    if key == keyboard.Key.esc:
        return False




if __name__ == "__main__":
  client = airsim.MultirotorClient()
  client.confirmConnection()

  with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


  listener = keyboard.Listener(
      on_press=on_press,
      on_release=on_release)
  listener.start()
