import os
import cv2
from cropimage import Cropper

cropper = Cropper()

img_path = "img/"
crop_path = "crop/"

files = os.listdir(img_path)

for file in files:
    if file.lower().endswith((".jpg",".jpeg")):
        crop_filename = "%s%s" % (crop_path,file)
        img_filename = "%s%s" % (img_path,file)

        result = cropper.crop(img_filename, True)
        cv2.imwrite(crop_filename, result)