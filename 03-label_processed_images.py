import os
import shutil

base_dir = os.getcwd()
image_dir =  f"{base_dir}/images/processed".replace("\\", "/")
class_file = f"{image_dir}/classes.txt"

shutil.copy(f"{base_dir}/classes.txt", class_file)

os.system(f"labelImg {image_dir} {class_file} {image_dir}")