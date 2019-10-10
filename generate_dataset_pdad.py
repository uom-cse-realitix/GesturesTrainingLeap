import numpy as np
import os

vectors_pd = np.genfromtxt("vectors_v2.csv", delimiter=",")
vectors_ad = np.genfromtxt("vectors_v3.csv", delimiter=",")

label_map = {
    "Pointing": [1, 0, 0, 0, 0],
    "Capture": [0, 1, 0, 0, 0],
    "ZoomIn": [0, 0, 1, 0, 0],
    "ZoomOut": [0, 0, 0, 1, 0],
    "Roaming": [0, 0, 0, 0, 1]
}

input_x = np.array([]).reshape(0, 270)
input_y = np.array([]).reshape(0, 5)


def search(timestamp, arr, index):
    for i in range(len(arr)):
        if (arr[i, index]) == timestamp:
            return i
    return -1


main_dir = "data"
sub_dirs = os.listdir(main_dir)

for sub_dir in sub_dirs:
    print("Generating vectors for %s..." % sub_dir)
    gestures = os.listdir(os.path.join(main_dir, sub_dir))
    count = 0
    for gesture in gestures:
        timestamps = [file.replace(".png", "") for file in os.listdir(os.path.join(main_dir, sub_dir, gesture))]
        sorted_timestamps = sorted([float(timestamp) for timestamp in timestamps])
        gesture_vector = np.array([])
        label = np.array(label_map[sub_dir])
        interrupted = False
        for timestamp in sorted_timestamps:
            index_pd = search(timestamp, vectors_pd, 5)
            index_ad = search(timestamp, vectors_ad, 4)
            if index_pd == -1 or index_ad == -1:
                interrupted = True
                break
            gesture_vector = np.append(gesture_vector, vectors_pd[index_pd, 0:5])
            gesture_vector = np.append(gesture_vector, vectors_ad[index_ad, 0:4])
        if interrupted:
            continue
        count += 1
        input_x = np.concatenate((input_x, [gesture_vector]), axis=0)
        input_y = np.concatenate((input_y, [label]), axis=0)
    print("%d gestures have been saved..." % count)

print("Shuffling the dataset...")
data = np.c_[input_x.reshape(len(input_x), -1), input_y.reshape(len(input_y), -1)]
np.random.shuffle(data)
input_x_final = data[:, :input_x.size // len(input_x)].reshape(input_x.shape)
input_y_final = data[:, input_x.size // len(input_x):].reshape(input_y.shape)
print("Saving the dataset...")
np.savetxt("gesture_input_x_v11.csv", input_x_final)
np.savetxt("gesture_input_y_v11.csv", input_y_final)
