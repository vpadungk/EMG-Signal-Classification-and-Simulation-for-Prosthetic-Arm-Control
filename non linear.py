import matplotlib.pyplot as plt
import numpy as np

filename = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/TEST2.csv"

x = []
y = []

with open(filename, "r") as f:
    next(f)
    i = 0
    for line in f:
        line = line.strip()
        if line:
            ts, val = line.split(",")
            x.append(i)
            y.append(float(val))
            i += 1

y = np.array(y)

window = 30   # change this (bigger = smoother)
smooth = np.convolve(y, np.ones(window)/window, mode="same")

plt.plot(x, y, alpha=0.4, label="Raw Signal")
# plt.plot(x, smooth, linewidth=2, label="Smooth Trend")

for v in [93, 275, 455, 636, 817, 998]:
    plt.axvline(x=v, color="r", linestyle="--", linewidth=1)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("ADC Data + Smoothed Trend Line")
plt.grid(True)
plt.legend()
plt.show()
