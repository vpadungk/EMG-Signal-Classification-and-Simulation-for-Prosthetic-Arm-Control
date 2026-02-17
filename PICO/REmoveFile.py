import os

try:
    os.remove("TEST0.csv")
    print("Deleted TEST0.csv")
except OSError:
    print("File not found")
