# MVP_Pi_Camera
Plug in for using the Raspberry Pi Camera
This is an alternative option to using a USB webcam to capture images.  The main difference is it uses the picamera python library instead of fswebcam.
For references, see the following articles:
https://www.raspberrypi.org/documentation/usage/webcams/
http://picamera.readthedocs.io/en/release-1.10/recipes1.html
## Install
  - Install the picamera library:
> sudo apt-get install fswebcam
  - Drag and drop the python code in this repository to the MVP python directory.  For ver 1.0 this is /home/pi/Documents/OpenAg-MVP/python
  - Edit cron to replace the image capture instructions
  - From a terminal window, type:
  > crontab -e
  - Delete the line that says:
  > 1 6-22 * * * /home/pi/Documents/OpenAg-MVP/scripts/webcam.sh
  -  Replace it with the following:
  1 6-22 * * * /home/pi/Documents/OpenAg-MVP/python/getImage.py

