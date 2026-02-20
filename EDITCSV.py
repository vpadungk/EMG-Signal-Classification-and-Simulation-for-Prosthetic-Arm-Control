import matplotlib.pyplot as plt

filename1 = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/OPEN.csv"
filename2 = "/home/vpadungk/Desktop/Project 0/EMG-Signal-Classification-and-Simulation-for-Prosthetic-Arm-Control/TEST4.csv"

xbar1 = [93, 275, 455, 636, 817, 998]
xbar2 = []

def SetXY(filename):
    x = []
    y = []
    with open(filename, "r") as f:
        next(f)  # skip header
        i = 0
        for line in f:
            line = line.strip()
            if line:
                ts, val = line.split(",")
                x.append(i)
                y.append(float(val))
                i += 1
    return x, y


# -------- Plot 1 --------
x1, y1 = SetXY(filename1)
# plt.subplot(211)
plt.plot(x1, y1)
plt.xlabel("Index")
plt.ylabel("ADC Value (/100)")
plt.title("ADC Data (Index vs Voltage)")
plt.axvline(x=94, color="r", linestyle="--", linewidth=1)
plt.axvline(x=291, color="r", linestyle="--", linewidth=1)
plt.axvline(x=1435, color="r", linestyle="--", linewidth=1)

# for i in xbar1:
#     plt.axvline(x=i, color="r", linestyle="--", linewidth=1)
plt.grid(True)

# # -------- Plot 2 --------
# x2, y2 = SetXY(filename2)
# plt.subplot(212)
# plt.plot(x2, y2)
# plt.xlabel("Index")
# plt.ylabel("ADC Value (/100)")
# plt.title("TEST3.csv (Index vs Voltage)")
# plt.grid(True)

plt.tight_layout()
plt.show()