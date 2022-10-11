from fileinput import filename
from skimage import io
import matplotlib.pyplot as plt
from easyocr import Reader
import re

# read the image stack
img = io.imread("DCLID_1.tif")
# show the image
import numpy as np
from PIL import Image

reader = Reader(["en"], gpu=True)


def common_replacements(string):
    string = string.replace("]", "1")
    string = string.replace(" L", "1")
    string = string.replace(" ", "")
    string = string.replace("DI", "D1")
    string = string.replace("B4", "84")
    return string


def get_filename(image):
    # Function to get Serial Number and regno
    results = reader.readtext(image, paragraph=False)
    regno = results[0][1]
    serialno = results[2][1]
    name = regno + "_" + serialno
    filename = common_replacements(name)
    return filename


for i in range(0, len(img), 2):
    imlist = []
    imlist.append(Image.fromarray(img[i]))
    # print(reader.readtext(img[i])[0])
    imlist.append(Image.fromarray(img[i + 1]))

    # Saves two pages of the certificate document
    filename = get_filename(img[i])
    name = f"{filename}.tif"
    print(name)
    imlist[0].save(
        name,  # Change the title here
        compression="tiff_deflate",
        save_all=True,
        append_images=imlist[1:],
    )

    # print(top_left)
    # print(bottom_right)
    # cropped_img = Image.fromarray(img[i])
    # cropped_img = cropped_img.crop(
    #     (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
    # )
    # cropped_img.save(f"cropped_{name}")
