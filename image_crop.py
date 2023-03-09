import os
import sys
import cv2
from cropimage import Cropper

cropper = Cropper()

# folder paths
img_path = "img/"
crop_path = "crop/"

isImgExist = os.path.exists(img_path)
isCropExist = os.path.exists(crop_path)

if isImgExist == False:
    sys.exit("img folder does not exist. Create img folder!")
elif isCropExist == False:
    sys.exit("crop folder does not exist. Create crop folder!")

# Save dir list to files
files = os.listdir(img_path)

# check if there is images in the img folder
if len(files) == 0:
    sys.exit("No images where found in the img folder")

for file in files:
    # Check for image file by extension
    if file.lower().endswith((".jpg",".jpeg")):
        # File names
        crop_filename = "%s%s" % (crop_path,file)
        img_filename = "%s%s" % (img_path,file)

        # Crop image with upper body
        result = cropper.crop(img_filename, True)

        # Write result into crop folder
        cv2_status = cv2.imwrite(crop_filename, result)
        if cv2_status == True:
            print("%s file has been written to crop folder" % (file))
        else:
            print("Could not write %s file to crop folder" % (file))