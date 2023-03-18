import os

print("Number of train images = ",len(os.listdir("Traffic_Management/assorted_data/images/train/")))
print("Number of train annotations = ",len(os.listdir("Traffic_Management/assorted_data/labels/train/")))

print("Number of val images = ",len(os.listdir("Traffic_Management/assorted_data/images/val/")))
print("Number of val annotations = ",len(os.listdir("Traffic_Management/assorted_data/labels/val/")))

print("Number of test images = ",len(os.listdir("Traffic_Management/assorted_data/images/test/")))
print("Number of test annotations = ",len(os.listdir("Traffic_Management/assorted_data/labels/test/")))