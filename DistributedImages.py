import os
from math import e

from sklearn.model_selection import train_test_split
import shutil

# get all the images and annotation files in two lists
images = []
annotations = []
for i in os.listdir("Traffic_Management/data/"):
    if ".txt" in i:
        annotations.append(os.path.join("Traffic_Management/data/", i))
    elif ".DS_Store" in i:
        pass
    else:
        images.append(os.path.join("Traffic_Management/data/", i))

# sort the files so that the order of images and annotations are same
images.sort()
annotations.sort()

print("Number of images", len(images), "\nNumber of annotation files", len(annotations))

# Split the dataset into train-valid-test splits
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations,
                                                                                test_size=0.2, random_state=1)
val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations,
                                                                              test_size=0.5, random_state=1)

print("Training:", len(train_images), ";Validation: ", len(val_images), ";Test:", len(test_images))

# create additional folders


if not os.path.isdir("Traffic_Management/assorted_data"):
    os.mkdir("Traffic_Management2/assorted_data")

if not os.path.isdir("Traffic_Management/assorted_data/images"):
    os.mkdir("Traffic_Management2/assorted_data/images")

if not os.path.isdir("Traffic_Management/assorted_data/labels"):
    os.mkdir("Traffic_Management2/assorted_data/labels")

if not os.path.isdir("Traffic_Management/assorted_data/images/train"):
    os.mkdir("Traffic_Management2/assorted_data/images/train")

if not os.path.isdir("Traffic_Management/assorted_data/images/val"):
    os.mkdir("Traffic_Management2/assorted_data/images/val")

if not os.path.isdir("Traffic_Management/assorted_data/images/test"):
    os.mkdir("Traffic_Management2/assorted_data/images/test")

if not os.path.isdir("Traffic_Management/assorted_data/labels/train"):
    os.mkdir("Traffic_ManagementTraffic_Management2/assorted_data/labels/train")

if not os.path.isdir("Traffic_Management/assorted_data/labels/val"):
    os.mkdir("Traffic_Management2/assorted_data/labels/val")

if not os.path.isdir("Traffic_Management/assorted_data/labels/test"):
    os.mkdir("Traffic_Management2/assorted_data/labels/test")


# Utility function to move images
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        #         print(f,destination_folder)
        try:
            shutil.copy(f, destination_folder)
        except e:
            print(e)
            pass
            # print(f,"Already there")
            # assert False


# Move the splits into their folders
move_files_to_folder(train_images, 'Traffic_Management/assorted_data/images/train/')
move_files_to_folder(val_images, 'Traffic_Management/assorted_data/images/val/')
move_files_to_folder(test_images, 'Traffic_Management/assorted_data/images/test/')
move_files_to_folder(train_annotations, 'Traffic_Management/assorted_data/labels/train/')
move_files_to_folder(val_annotations, 'Traffic_Management/assorted_data/labels/val/')
move_files_to_folder(test_annotations, 'Traffic_Management/assorted_data/labels/test/')