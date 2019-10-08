import numpy as np
import os
import shutil
import time

vectors = np.genfromtxt("vectors.csv", delimiter=",")

folder_count = {
    "capture": 0,
    "zoomout": 0,
    "pointing": 0,
    "zoomin": 0
}


def search(timestamp, arr):
    for i in range(len(arr)):
        if (arr[i, 5]) == timestamp:
            return True
    return False


img_dir = "/home/darshanakg/Projects/GestureDataset/images_all"
data_files = "/home/darshanakg/Projects/GestureDataset/formatted"
save_path = "/home/darshanakg/Projects/GestureDataset/gestures"
files = os.listdir(data_files)

for file in files:
    gesture = file.split('-')[0]
    print(gesture)
    timestamps = np.loadtxt(os.path.join(data_files, file), dtype=np.str)
    filenames = [t + ".png" for t in timestamps]
    folder_count[gesture] = folder_count[gesture] + 1
    os.mkdir(os.path.join(save_path, gesture, str(folder_count[gesture])))
    for filename in filenames:
        shutil.copyfile(os.path.join(img_dir, filename), os.path.join(save_path, gesture, str(folder_count[gesture]), filename))

# for sub_dir in sub_dirs:
#     print(sub_dir)
#     gestures = os.listdir(os.path.join(main_dir, sub_dir))
#     for gesture in gestures:
#         for file in os.listdir(os.path.join(main_dir, sub_dir, gesture)):
#             if not search(float(file.replace(".png", "")), vectors):
#                 os.remove(os.path.join(main_dir, sub_dir, gesture, file))
#                 print("Deleted..")