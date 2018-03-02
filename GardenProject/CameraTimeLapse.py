# we need to use time for sleep & our file naming convention
# pyimgur is a libary for imgur - we use this to upload our
# picture and return a link
import time
from picamera import PiCamera
import pyimgur
import requests
import json

camera = PiCamera()
camera.resolution = (1920, 1080)
NameTime = (time.strftime(" %d-%m-%y_%H:%M"))
camera.vflip = True  # flip verti

FileName = NameTime + ".jpg"


# this is our funktion:
# takes a picture, upload it and save it on the device
# framecount is used to organize the filenames
def TimeLapse():
    framecount = 1
    CLIENT_ID = "fc65e40de16806a"
    im = pyimgur.Imgur(CLIENT_ID)
    while True:
        strframecount = str(framecount)
        PATH = strframecount + FileName
        camera.capture(PATH)
        framecount = framecount + 1
        print("TimeLapse picture taken:" + NameTime)  # tell user pic taken
        # 3200 = 1 time
        uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
        print(uploaded_image.link)
        post_data = {'url': uploaded_image.link}
        post_response = requests.post(url='http://garden-project-web-api.herokuapp.com/api/images', json=post_data)
        time.sleep(3200)


if __name__ == "__main__":
    TimeLapse()