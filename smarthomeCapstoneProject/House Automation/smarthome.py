import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep
from signal import pause
import sys
import Adafruit_DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

camera = PiCamera() #start the camera
camera.rotation = 180
camera.start_preview()
#i = 0#image names numbering

doorDownstairs = 21 #GPIO21 PIN40
doorUpstairs = 20 #GPIO20 PIN38 
windowLeft = 18 #GPIO18 PIN12
windowRight= 19 #GPIO19 PIN35

sound_sensor = 17
GPIO.setup(sound_sensor, GPIO.IN)

GPIO.setup(doorDownstairs, GPIO.OUT)
GPIO.setup(doorUpstairs, GPIO.OUT)
GPIO.setup(windowLeft, GPIO.OUT)
GPIO.setup(windowRight, GPIO.OUT)
 
d0 = GPIO.PWM(doorDownstairs, 50) # GPIO 20for PWM with 50Hz
d1 = GPIO.PWM(doorUpstairs, 50) # GPIO 21 for PWM with 50Hz
wL = GPIO.PWM(windowLeft, 50) # GPIO 18 for PWM with 50Hz
wR = GPIO.PWM(windowRight, 50) # GPIO 19 for PWM with 50Hz


#Code For Automating Doors and Windows

def open_doorDown():  #Open Door Downstairs
  d0.start(2.5) 
  d0.ChangeDutyCycle(7.5)
  time.sleep(1)
  d0.stop()
  print("Door downstairs Opened")

def close_doorDown(): #Close Door Downstairs
  d0.start(2.5)
  d0.ChangeDutyCycle(2.3)
  time.sleep(1)
  d0.stop()
  print("Door downstairs Closed")

def open_doorUp():  #Open Door Upstairs
  d1.start(2.5)
  d1.ChangeDutyCycle(8.4)
  time.sleep(1)
  d1.stop()
  print("Door Upstairs Opened")


def close_doorUp():  #Close Door Upstairs
  d1.start(2.5)
  d1.ChangeDutyCycle(3.6)
  time.sleep(1)
  d1.stop()
  print("Door Upstairs Closed")

def open_windowL(): #Open Window on Left
  wL.start(2.5) 
  wL.ChangeDutyCycle(1)
  time.sleep(1)
  wL.stop()
  print("Left Window Opened")

def close_windowL():  #Open Window on Right
  wL.start(7.5) 
  wL.ChangeDutyCycle(5.8)
  time.sleep(1)
  wL.stop()
  print("Left Window Closed")

def open_windowR(): #Open Window on Right
  wR.start(2.5) 
  wR.ChangeDutyCycle(7.5)
  time.sleep(1)
  wR.stop()
  print("Right Window Opened")

def close_windowR():  #Close Window on Right
  wR.start(1) 
  wR.ChangeDutyCycle(2.1)
  time.sleep(1)
  wR.stop()
  print("Right Window Closed")
  
def close_allDoors():
  d0.start(1)
  d1.start(2.5)
  d0.ChangeDutyCycle(2.3)
  time.sleep(1)
  d0.stop()
  d1.ChangeDutyCycle(3.6)
  time.sleep(1)
  d1.stop()
  print("All doors Closed")

def open_allDoors():
  d0.start(1)
  d0.ChangeDutyCycle(7.5)
  time.sleep(1)
  d0.stop()
  d1.start(1)
  d1.ChangeDutyCycle(8.4)
  time.sleep(1)
  d1.stop()
  print("All doors Open")

def close_allWindows():
  wL.start(7.5) 
  wL.ChangeDutyCycle(5)
  time.sleep(1)
  wL.stop()
  wR.start(1) 
  wR.ChangeDutyCycle(2.1)
  time.sleep(1)
  wR.stop()
  print("All Wiindows Closed")

def open_allWindows():
  wR.start(2.5) 
  wR.ChangeDutyCycle(6.5)
  time.sleep(1)
  wR.stop()
  wL.start(2.5) 
  wL.ChangeDutyCycle(1)
  time.sleep(1)
  wL.stop()
  print("All Wiindows Open")
  
def close_all():
  d0.start(2.5)
  d1.start(2.5)
  d0.ChangeDutyCycle(2.3)
  time.sleep(1)
  d0.stop()
  d1.ChangeDutyCycle(3.6)
  time.sleep(1)
  d1.stop()
  wL.start(7.5) 
  wL.ChangeDutyCycle(5)
  time.sleep(1)
  wL.stop()
  wR.start(1) 
  wR.ChangeDutyCycle(2.1)
  time.sleep(1)
  wR.stop()
  print("All Wiindows and Doors Closed")
   
def open_all():
  d0.start(2.5)
  d0.ChangeDutyCycle(7.5)
  time.sleep(1)
  d0.stop()
  d1.start(2.5)
  d1.ChangeDutyCycle(8.4)
  time.sleep(1)
  d1.stop()
  wL.start(2.5) 
  wL.ChangeDutyCycle(1)
  time.sleep(1)
  wL.stop()
  wR.start(2.5) 
  wR.ChangeDutyCycle(6.5)
  time.sleep(1)
  wR.stop()
  print("All Wiindows and Doors Open")

#Surveillance Camera
#stop the camera when the pushbutton is pressed
def stop_camera():
    camera.stop_preview()
    #exit the program
    exit()

#takes  photo when motion is detected
def take_photo():
    camera.capture('/home/pi/Desktop/image.jpg')
    print('A photo has been taken')
       
#import requests
#url = 'http://file.api.wechat.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
#files = {'media': open('/home/pi/Desktop/image.jpg', 'rb')}
#requests.post(url, files=files)


#pause()

##Temperature Sensor

def take_temperature():  
    	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    	return ('{0:0.1f}'.format(temperature-4))
    	

#baby cry detector
def callback(sound_sensor, detector):
        if GPIO.input(sound_sensor):
            detector.detected += 1
        else:
            pass



#take_photo()
#take_temperature()
#open_doorDown()
#close_doorDown()
#open_doorUp()
#close_doorUp()
#open_windowR()
#close_windowR()
#open_windowL()
#close_windowL()
#open_allDoors()
#close_allDoors()
#open_allWindows()
#close_allWindows()
#open_all()
#close_all()
