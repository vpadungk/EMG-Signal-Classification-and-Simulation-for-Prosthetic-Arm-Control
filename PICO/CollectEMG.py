from machine import Pin, ADC
from time import sleep, time
import os

Filename = "TEST0.csv"
header = "Timestamp,Value\n"

ADC_Port = 26
Button = Pin(14, Pin.IN, Pin.PULL_UP)

Window_Size = 5000
value = []
rows = []
ts = 0


def writeCSV(filename, Rows):
    with open(filename, "a") as f:
        for r in Rows:
            f.write("{},{}\n".format(r[0], r[1]))
    print("Wrote", len(Rows), "rows to", filename)


def ReadADC(pin, window_size=5):
    global value, ts

    pot = ADC(pin)
    emg = pot.read_u16()

    value.append(emg)
    if len(value) > window_size:
        value.pop(0)

    avg_emg = sum(value) / len(value)

    ts = time()
    voltage = avg_emg * 3.3 / 65535
    return [ts, voltage]


def main():
    global rows, value

    logging = False
    last_state = 1

    print("Files in directory:", os.listdir())
    print("Press button GPIO14 to start/stop logging")

    while True:
        current_state = Button.value()

        if last_state == 1 and current_state == 0:
            sleep(0.05)
            if Button.value() == 0:
                logging = not logging

                if logging:
                    print("Logging STARTED")
                    value = []
                    rows = []
                else:
                    print("Logging STOPPED")
                    if len(rows) > 0:
                        writeCSV(Filename, rows)
                        rows = []

                while Button.value() == 0:
                    sleep(0.01)

        last_state = current_state

        if logging:
            data = ReadADC(ADC_Port, Window_Size)
            print(data)

            rows.append(data)

            if len(rows) >= 20:
                writeCSV(Filename, rows)
                rows = []

        sleep(0.05)


try:
    with open(Filename, "r") as f:
        pass
except:
    with open(Filename, "w") as f:
        f.write(header)
    print("Created file:", Filename)

main()