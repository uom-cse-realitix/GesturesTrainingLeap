import os
import shutil

import numpy as np

vectors = np.genfromtxt("vectors.csv", delimiter=",")

folder_count = {
    "capture": 0,
    "zoomout": 0,
    "pointing": 0,
    "zoomin": 0,
    "roaming": 0
}


def search(timestamp, arr):
    for i in range(len(arr)):
        if (arr[i, 5]) == timestamp:
            return True
    return False


# Folder containing all the images
img_dir = "/home/darshanakg/Projects/GestureDataset/images_all"
# The logs of gesture sequences generate by the JAVA program
data_files = "/home/darshanakg/Projects/GestureDataset/formatted"
# Folder to save
save_path = "/home/darshanakg/Projects/GestureDataset/gestures"

files = os.listdir(data_files)

for file in files:
    gesture = file.split('-')[0]
    print(gesture)
    timestamps = np.loadtxt(os.path.join(data_files, file), dtype=np.str)
    print(len(timestamps))
    size = len(timestamps)
    if size < 30 or size > 70:
        print("Eliminated...")
        continue
    elif size <= 39:
        filenames = [t + ".png" for t in timestamps[:30]]
        folder_count[gesture] = folder_count[gesture] + 1
        os.mkdir(os.path.join(save_path, gesture, str(folder_count[gesture])))
        for filename in filenames:
            shutil.copyfile(os.path.join(img_dir, filename),
                            os.path.join(save_path, gesture, str(folder_count[gesture]), filename))
    elif size <= 70:
        s = size - 30
        p = s // 10
        r = (s % 10) % (s // 10)
        c = (s % 10) // (s // 10)
        for i in range(p + 1):
            sindex = i * (10 + c) + (0, r)[i == p]
            filenames = [t + ".png" for t in timestamps[sindex:sindex + 30]]
            folder_count[gesture] = folder_count[gesture] + 1
            os.mkdir(os.path.join(save_path, gesture, str(folder_count[gesture])))
            for filename in filenames:
                shutil.copyfile(os.path.join(img_dir, filename),
                                os.path.join(save_path, gesture, str(folder_count[gesture]), filename))
