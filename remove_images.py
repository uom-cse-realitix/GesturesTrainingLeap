import os
import shutil
import numpy as np

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
files = os.listdir(data_files)

count = 0

for file in files:
    gesture = file.split('-')[0]
    print(gesture)
    timestamps = np.loadtxt(os.path.join(data_files, file), dtype=np.str)
    size = len(timestamps)
    for timestamp in timestamps:
        if os.path.isfile(os.path.join(img_dir, timestamp + ".png")):
            count += 1
            os.remove(os.path.join(img_dir, timestamp + ".png"))


print("%d files were removed..." % count)
