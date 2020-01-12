#import serial

#arduinoData = serial.Serial('COM6', baudrate=9600, timeout=1)
#while True:
 #   arduinoData.write('1')


from time import sleep
import serial
ser = serial.Serial('COM5', 9600, timeout=1) # Establish the connection on a specific port
counter = 97 # Below 32 everything in ASCII is gibberish
while True:
     #counter +=1
     ser.write(str(chr(110))) # Convert the decimal number to ASCII then send it to the Arduino
     print ser.readline() # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
     if counter == 255:
        counter = 32