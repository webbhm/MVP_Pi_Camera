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
  > 1 6-22 * * * /home/pi/Documents/OpenAg-MVP/python/getImage.py
## Camera Adjustment
The lights in the MVP are bright and can overwehlm some sensors.  Fortunately the Pi camera has a lot of settings.  The python code has the settings set (ISO and brightness) to the defaults.  Try changing these around if you image is washed out or not the quality you want.  In general you will likely want a low ISO number (50 or 100).
