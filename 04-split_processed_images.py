import os
import shutil
from tqdm import tqdm

n_images = 764
training_share = 0.75

n_training = round(n_images * training_share, 0)
base_dir = "./images/processed/"
target_base_dir = "./data/"

training_set = set()
validation_set = set()


# Clean up the files and directories
if os.path.isdir(target_base_dir):
    shutil.rmtree(target_base_dir)

#'''
for file_name in os.listdir(base_dir):
    if ".txt" in file_name and "classes" not in file_name:
        if len(training_set) < n_training:
            training_set.add(file_name)
        else:
            validation_set.add(file_name)

for path_part, label_file_names in [("train", training_set),("val", validation_set)]:
    os.makedirs(f"{target_base_dir}{path_part}/labels/", exist_ok=True)
    os.makedirs(f"{target_base_dir}{path_part}/images/", exist_ok=True)
    for label_file_name in tqdm(label_file_names, desc=path_part):
        image_file_name = label_file_name.replace("txt", "jpg")
        shutil.copy(f"{base_dir}{label_file_name}", f"{target_base_dir}{path_part}/labels/{label_file_name}")
        shutil.copy(f"{base_dir}{image_file_name}", f"{target_base_dir}{path_part}/images/{image_file_name}")
#'''