import numpy as np
import os

vectors = np.genfromtxt("vectors_v2.csv", delimiter=",")
label_map = {
    "Pointing": [1, 0, 0, 0],
    "Capture": [0, 1, 0, 0],
    "ZoomIn": [0, 0, 1, 0],
    "ZoomOut": [0, 0, 0, 1]
}

input_x = np.array([]).reshape(0, 150)
input_y = np.array([]).reshape(0, 4)


def search(timestamp, arr):
    for i in range(len(arr)):
        if (arr[i, 5]) == timestamp:
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
            index = search(timestamp, vectors)
            if index == -1:
                interrupted = True
                break
            gesture_vector = np.append(gesture_vector, vectors[index, 0:5])
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
np.savetxt("gesture_input_x_v9.csv", input_x_final)
np.savetxt("gesture_input_y_v9.csv", input_y_final)
