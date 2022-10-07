from skimage import io
import matplotlib.pyplot as plt
from easyocr import Reader

# read the image stack
img = io.imread("DCLID.tif")
# show the image
import numpy as np
from PIL import Image

reader = Reader(["en"], gpu=True)


def get_regno_and_serial(image):
    # Function to get Serial Number and regno
    result = reader.readtext(image)


for i in range(0, len(img), 2):
    imlist = []
    imlist.append(Image.fromarray(img[i]))
    print(reader.readtext(img[i])[0])
    imlist.append(Image.fromarray(img[i + 1]))

    # Saves two pages of the certificate document
    imlist[0].save(
        f"test_{i+1}_record.tif",  # Change the title here
        compression="tiff_deflate",
        save_all=True,
        append_images=imlist[1:],
    )
