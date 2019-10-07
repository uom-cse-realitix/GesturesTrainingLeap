from multiprocessing import Process, Queue, cpu_count
import random
import time
import numpy as np
# import tensorflow as tf
# from tensorflow import keras

print("Initializing prediction modal...")
# model = keras.models.load_model("gesture_lstm.h5")
print("Initialization completed...")


# command_classes = ['Pointing', 'Capture', 'ZoomIn', 'ZoomOut', 'Roaming']


# start_time = time.time()
# prediction = model.predict(np.random.random(150).reshape(1, 1, 150))
# gesture = command_classes[np.argmax(prediction)]
# end_time = time.time()
# print(gesture, end_time - start_time)


def process_gesture(sequence):
    from tensorflow import keras
    model = keras.models.load_model("gesture_lstm.h5")
    command_classes = ['Pointing', 'Capture', 'ZoomIn', 'ZoomOut', 'Roaming']
    prediction = model.predict(sequence.reshape(1, 1, 150))
    gesture = command_classes[np.argmax(prediction)]
    print(gesture)


# def serve(queue):
#     works = ["task_1", "task_2"]
#     while True:
#         time.sleep(0.01)
#         queue.put(random.choice(works))
#
#
# def work(id, queue):
#     while True:
#         task = queue.get()
#         if task is None:
#             break
#         time.sleep(0.05)
#         print("%d task:" % id, task)
#     queue.put(None)
#
#
# class Manager:
#     def __init__(self):
#         self.queue = Queue()
#         self.NUMBER_OF_PROCESSES = cpu_count()
#
#     def start(self):
#         print("starting %d workers" % self.NUMBER_OF_PROCESSES)
#         self.workers = [Process(target=work, args=(i, self.queue)) for i in range(self.NUMBER_OF_PROCESSES)]
#         for w in self.workers:
#             w.start()
#
#         serve(self.queue)
#
#     def stop(self):
#         self.queue.put(None)
#         for i in range(self.NUMBER_OF_PROCESS):
#             self.workers[i].join()
#         self.queue.close()
#
#
# Manager().start()

# process_queue = Queue()
gesture_sequence = np.array([])

for i in range(1000):
    seq = np.random.rand(5)
    gesture_sequence = np.append(gesture_sequence, seq)
    if len(gesture_sequence) > 150:
        # process_queue.put(gesture_sequence[:30])
        p = Process(target=process_gesture, args=(gesture_sequence[:150],))
        gesture_sequence = gesture_sequence[100:]
        p.start()
    time.sleep(0.2)
    # print(gesture_sequence)
