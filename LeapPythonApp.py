import Leap, thread, sys, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import serial

arduinoData = serial.Serial('COM6', baudrate=9600, timeout=1)

def sortFirst(val): 
    return int(val[0]) 

class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle','Ring', 'Pinky']
    bone_names = ['Metacarpel', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    notes = ['c', 'C', 'd', 'D', 'e', 'f', 'F', 'g', 'G', 'a']

    oldFingerHeights = [1,1,1,1,1,1,1,1,1,1]
    newFingerHeights = [1,1,1,1,1,1,1,1,1,1]
    fingerHeightsDelta = []
    count = 0
    threshold = 18

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
        # start of a new set, set the old height to the last height we had
        if self.count is 0:
            self.oldFingerHeights = self.newFingerHeights
        self.count +=1

        frame = controller.frame()

        """print("\nFrame ID: " + str(frame.id) +
              "\nTimestamp: " + str(frame.timestamp) +
              "\n# of Hands: " + str(len(frame.hands)) +
              "\n# of Fingers: " + str(len(frame.fingers)) +
              "\n# of Tools: " + str(len(frame.tools)) + 
              "\n# of Gestures: " + str(len(frame.gestures())))"""
        fingerPositions = []
        if len(frame.hands) != 2:
            self.count = 0
            return
        
        if frame.hands[0].is_left:
            fingers = frame.hands[0].pointables
            fingers.append(frame.hands[1].pointables)
        else:
            fingers = frame.hands[1].pointables
            fingers.append(frame.hands[0].pointables)
        # now have a list of pointables from left hand to right hand
        
        for finger in fingers:
            fingerPositions.append(finger.tip_position)
        fingerPositions.sort(key=sortFirst)
        
        # every 15 frames we subtract the last frame's height from this frame's height
        if self.count is 15:
            self.newFingerHeights = []
            self.fingerHeightsDelta = []
            self.count = 0
            # getting all the new finger heights
            for finger in fingerPositions:
                self.newFingerHeights.append(finger[1])
            for i in range(len(self.newFingerHeights)):
                self.fingerHeightsDelta.append(self.oldFingerHeights[i] - self.newFingerHeights[i])
        
        if len(self.fingerHeightsDelta) > 0:
            if max(self.fingerHeightsDelta) > self.threshold:
                #print( self.fingerHeightsDelta.index(max(self.fingerHeightsDelta)) )
                fingerPressed = self.notes[self.fingerHeightsDelta.index(max(self.fingerHeightsDelta))]
                arduinoData.write(fingerPressed)
            else:
                fingerPressed = 'n'
                arduinoData.write(fingerPressed)
        
        """if hand.palm_position[0] > 0:
            print("\nright")
            #print("\n" + str(hand.palm_position[0]))
            arduinoData.write(str(chr(97)))"""
        """else:
            print("\nleft")
            arduinoData.write(str(chr(98)))"""

        #print handType + " Hand ID: " + str(hand.id) + " Palm X Position: " + str(hand.palm_position[0])

        #normal = hand.palm_normal
        #direction = hand.direction

        #print("Pitch: " + str(direction.pitch * Leap.RAD_TO_DEG) + " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) + " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG))

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

    
    


    #arduinoData.write

if __name__ == "__main__":
    main()