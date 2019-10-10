import numpy as np
import os

vectors = np.genfromtxt("vectors.csv", delimiter=",")


def search(timestamp, arr):
    for i in range(len(arr)):
        if (arr[i, 5]) == timestamp:
            return True
    return False


main_dir = "data"
sub_dirs = os.listdir(main_dir)


for sub_dir in sub_dirs:
    print(sub_dir)
    gestures = os.listdir(os.path.join(main_dir, sub_dir))
    for gesture in gestures:
        for file in os.listdir(os.path.join(main_dir, sub_dir, gesture)):
            if not search(float(file.replace(".png", "")), vectors):
                os.remove(os.path.join(main_dir, sub_dir, gesture, file))
                print("Deleted..")