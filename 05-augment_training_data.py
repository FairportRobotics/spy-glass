import cv2
import os
import shutil
import numpy as np
import random
from tqdm import tqdm

cleanup = True

base_dir = "./data/train/images/" # os.getcwd() + "/data/train/images/"
labels_dir = base_dir.replace("images", "labels")

conversions = {
    #"hsv": cv2.COLOR_RGB2HSV_FULL,
    "grayscale": cv2.COLOR_RGB2GRAY,
    #"hls": cv2.COLOR_RGB2HLS_FULL,
    #"lab": cv2.COLOR_RGB2LAB,
    #"luv": cv2.COLOR_RGB2LUV,
    #"bgr": cv2.COLOR_RGB2BGR,
    #"xyz": cv2.COLOR_RGB2XYZ,
    #"ycrcb": cv2.COLOR_RGB2YCrCb,
    #"yuv": cv2.COLOR_RGB2YUV
}

def add_noise(image, prob=0.5):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rnd = random.random()
            if rnd < prob:
                output[i][j] = 0
            elif rnd > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

for file_name in tqdm(os.listdir(base_dir)):
    label_file_name = file_name.replace(".jpg", ".txt")
    if "_" in file_name:
        if cleanup:        
            os.unlink(base_dir + file_name)
            os.unlink(labels_dir + label_file_name)
    else:
        # Load the image
        img = cv2.imread(base_dir + file_name)

        # Blur the image
        blurred_image = cv2.blur(img, (5, 5))
        cv2.imwrite(base_dir + file_name.replace(".jpg", "_blurred.jpg"), blurred_image)
        shutil.copy(labels_dir + label_file_name, labels_dir + label_file_name.replace(".txt", "_blurred.txt"))

        # Convert to another color space:
        for key, code in conversions.items():
            new_img = cv2.cvtColor(img, code)
            cv2.imwrite(base_dir + file_name.replace(".jpg", f"_{key}.jpg"), new_img)
            shutil.copy(labels_dir + label_file_name, labels_dir + label_file_name.replace(".txt", f"_{key}.txt"))
        
        # Add noise to the image
        noisy_img = add_noise(img)
        cv2.imwrite(base_dir + file_name.replace(".jpg", "_noisy.jpg"), blurred_image)
        shutil.copy(labels_dir + label_file_name, labels_dir + label_file_name.replace(".txt", "_noisy.txt"))
