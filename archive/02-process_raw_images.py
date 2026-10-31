import hashlib
import os
from PIL import Image

def hash(img):
    return hashlib.md5(img.tobytes()).hexdigest()

for dirs, subdir, files in os.walk("./images/raw"):
    for file in files:
        try:
            img = Image.open(f"{dirs}/{file}")
            img = img.convert("RGB")
            img.save("./images/processed/" + hash(img) + ".jpg")
        except:
            print(f"ERROR: Could not standardize {file}")