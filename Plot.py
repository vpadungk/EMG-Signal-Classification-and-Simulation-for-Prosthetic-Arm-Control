import matplotlib.pyplot as plt

filename = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/OPEN.csv"

t = []
v = []

with open(filename, "r") as f:
    next(f)  # skip header
    for line in f:
        line = line.strip()
        if line:
            ts, val = line.split(",")
            t.append(float(ts))
            v.append(float(val))

plt.plot(t, v)
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.title("ADC Plot from CSV")
plt.grid(True)
plt.show()
