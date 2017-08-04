import picamera
import time


#Use this line for MVP 1.0
dir = '/home/pi/Documents/OpenAg-MVP/webcam/'
#Use this line for MVP 2.0
# dir = '/home/pi/MVP/pictures/'

#Create file name with timestamp
fileName=dir + time.strftime("%Y-%m-%d-%H%M%S") + '.jpg'
# print(fileName)
camera = picamera.PiCamera()

# Adjust brightness and ISO for lighting
camera.brightness=50
camera.ISO=0
camera.resolution = (2592, 1944)

# Capture an image
camera.capture(fileName)
