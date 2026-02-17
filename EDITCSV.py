import matplotlib.pyplot as plt

filename = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/TEST4.csv"

x = []
y = []

with open(filename, "r") as f:
    next(f)  # skip header
    i = 0
    for line in f:
        line = line.strip()
        if line:
            ts, val = line.split(",")
            x.append(i)            # index
            y.append(float(val))   # value
            i += 1

plt.axvline(x=242-60, color="r", linestyle="--", linewidth=1)
plt.axvline(x=423-60, color="r", linestyle="--", linewidth=1)
plt.axvline(x=785-60, color="r", linestyle="--", linewidth=1)
plt.axvline(x=966-60, color="r", linestyle="--", linewidth=1)
plt.axvline(x=1328-60, color="r", linestyle="--", linewidth=1)
plt.axvline(x=1511-60, color="r", linestyle="--", linewidth=1)


plt.plot(x, y)
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("ADC Data (Index vs Value)")
plt.grid(True)
plt.show()
