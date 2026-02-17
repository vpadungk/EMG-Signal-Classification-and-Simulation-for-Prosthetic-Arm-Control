from machine import Pin, ADC
import time

pot = ADC(Pin(26)) 

window_size = 100  # number of samples for moving average
values = []

while True:
    emg = pot.read_u16()

    # add new value to list
    values.append(emg)

    # keep only the last 'window_size' samples
    if len(values) > window_size:
        values.pop(0)

    # compute moving average
    avg_emg = sum(values) / len(values)

    print(avg_emg/100)
    time.sleep(0.05)