import wiringpi2
import smbus
import time
import os
import subprocess
#import os.spawn*
import random
import dircache

from subprocess import Popen, PIPE
from wave import *
from math import *
from sys import *

wiringpi2.wiringPiSetup()
#wiringpi.piBoardRev()
wiringpi2.mcp23008Setup(65,0x20)

PI2 = 6.283185306
scale = 32767 #16-bit unsigned short
FR = 44000 #framerate

# Expansion Setup
# wiringpi2.mcp23017Setup(PIN_OFFSET,I2C_ADDR)
# General IO Examples
# wiringpi2.pinMode(6,1) // Set pin 6 to 1 ( OUTPUT )
# wiringpi2.digitalWrite(6,1) // Write 1 ( HIGH ) to pin 6
# wiringpi2.digitalRead(6) // Read pin 6 
# Bit Shifting
# wiringpi2.shiftOut(1,2,0,123) // Shift out 123 (b1110110, byte 0-255) to data pin 1, clock pin 2
# Soft Tones
# wiringpi2.softToneCreate(PIN)
# wiringpi2.softToneWrite(PIN,FREQUENCY)
#
# serial = wiringpi2.serialOpen('/dev/ttyAMA0',9600) // Requires device/baud and returns an ID
# wiringpi2.serialPuts(serial,"hello")
# wiringpi2.serialClose(serial) // Pass in ID

OUTPUT = 1
INPUT = 0

# Set pins 0, 1 and 2 to output for the 3x4 keypad
wiringpi2.pinMode(65,OUTPUT)
wiringpi2.pinMode(66,OUTPUT)
wiringpi2.pinMode(67,OUTPUT)

# Set pin 3, 4, 5 and 6 to input with the pullup resistor enabled for the 3x4 keypad
wiringpi2.pinMode(68,INPUT)
wiringpi2.pullUpDnControl(68,2)
wiringpi2.pinMode(69,INPUT)
wiringpi2.pullUpDnControl(69,2)
wiringpi2.pinMode(70,INPUT)
wiringpi2.pullUpDnControl(70,2)
wiringpi2.pinMode(71,INPUT)
wiringpi2.pullUpDnControl(71,2)

# Set pin 7 to input with the pullup resistor enabled for the phone hook switch
wiringpi2.pinMode(72,INPUT)
wiringpi2.pullUpDnControl(72,2)

# Read input pin and display the results
#print "Pin 7(72) = %d" % (wiringpi2.digitalRead(71) >> 7)

#subprocess.call(['/home/pi/WolfsonAudio/Playback_to_Lineout.sh']) 
#subprocess.call(['df', '-h'])

#subprocess.call(['/home/pi/WolfsonAudio/WolfsonAudio/Record_from_lineIn.sh']) 

while True:

  if wiringpi2.digitalRead(72): 
    print("Off The Hook")
    
    #FILENAME = random.choice(os.listdir('/home/pi/Desktop/MINGLE.V2/RECORDINGS/'))
    #ARGS = ["-Dhw:0 -r 44100 -c 2 -f S16_LE /home/pi/Desktop/MINGLE.V2/RECORDINGS/"]
    #subprocess.call(['aplay', '-Dhw:0', '-r', '48000', '-c', '2', '-f', 'S16_LE', '/home/pi/Desktop/MINGLE.V2/RECORDINGS/chinese.wav'])
    
    #p = Popen(['aplay'] + ARGS + FILENAME, stdout=PIPE)
    #p.stdout.close()
    #p.wait()
  else:
    print("On The Hook")
    subprocess.call(['killall', 'aplay'])