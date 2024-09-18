from simple_image_download import simple_image_download as simp
import os
import shutil

keywords = ["FRC+Robot"]

n_images = 50

# Create a simple image downloader
my_downloader = simp.Downloader()
# Change the save directory
my_downloader.directory = "./images/raw/"
# Create the directory if it doesn't exist
if not os.path.isdir(my_downloader.directory):
        os.makedirs(my_downloader.directory)

# Loop over the keywords
for keyword in keywords:
    # Create the directory if it doesn't exist
    save_path = my_downloader.directory + keyword
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    # Download the images
    my_downloader.download(keyword, n_images)
    # Move the images into the raw directory
    for file_name in os.listdir(save_path):
        shutil.move(f"{save_path}/{file_name}", my_downloader.directory + file_name)
    # Remove the empty directory
    shutil.rmtree(save_path)
