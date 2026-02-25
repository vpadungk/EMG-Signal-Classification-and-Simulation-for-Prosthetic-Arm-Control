import matplotlib.pyplot as plt

filename2 = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/REST.csv"
filename1 = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/Test10.csv"
filename3 = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/Test9.csv"
filename4 = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/Test7.csv"

xbar1 = [93, 275, 455, 636, 817, 998]
xbar2 = []

def SetXY(filename):
    x = []
    y = []

    dt_ms = 0.05   # 0.05 sec = 50 ms
    t = 0

    with open(filename, "r") as f:
        next(f)  # skip header

        for line in f:
            line = line.strip()
            if line:
                ts, val = line.split(",")

                x.append(t)
                y.append(float(val))

                t += dt_ms

    return x, y

# -------- Plot 1 --------
x1, y1 = SetXY(filename1)
x3, y3 = SetXY(filename3)

plt.subplot(211)
plt.plot(x1, y1, label="Test10")
plt.plot(x3, y3, label="Test9")

plt.xlabel("Time (Second)")
plt.ylabel("ADC Voltage (V)")
plt.title("ADC Data (Comparison)")
plt.legend()

plt.axvline(x=8.2, color="r", linestyle="--", linewidth=1)
plt.axvline(x=17.15, color="r", linestyle="--", linewidth=1)
# plt.axvline(x=43.35, color="r", linestyle="--", linewidth=1)
# plt.axvline(x=52.05, color="r", linestyle="--", linewidth=1)

# for i in xbar1:
#     plt.axvline(x=i, color="r", linestyle="--", linewidth=1)
plt.grid(True)

# -------- Plot 2 --------
x2, y2 = SetXY(filename2)
x4, y4 = SetXY(filename4)

plt.subplot(212)
plt.plot(x2, y2, label="Resting")
plt.plot(x4, y4, label="Test7")
plt.xlabel("Time (Second)")
plt.ylabel("ADC Voltage (V)")
plt.title("ADC Data (Second vs Voltage)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()