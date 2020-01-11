import Leap, thread, sys, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle','Ring', 'Pinky']
    bone_names = ['Metacarpel', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller):
        print("Motion Sensor Connected!")

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        print("Motion Sensor Disconnected")

    def on_exit(self, controller):
        print("Exited")

    # this is the meat of the code, this gets called every frame
    def on_frame(self, controller):
        frame = controller.frame()

        print("\nFrame ID: " + str(frame.id) +
              "\nTimestamp: " + str(frame.timestamp) +
              "\n# of Hands: " + str(len(frame.hands)) +
              "\n# of Fingers: " + str(len(frame.fingers)) +
              "\n# of Tools: " + str(len(frame.tools)) + 
              "\n# of Gestures: " + str(len(frame.gestures())))

def main():
    # object of class we define
    listener = LeapMotionListener()

    # object of class from Leap API
    controller = Leap.Controller()

    # uses "listener" we define, probably searches for functions with
    # the names on_*** and calls them accordingly
    controller.add_listener(listener)

    print("Press Enter to Quit")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()