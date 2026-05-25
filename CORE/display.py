import time
import os
from CORE import storage


def display_latest_metrics():
    for collection in storage.buffer_metrics():
        os.system("cls" if os.name == "nt" else "clear")  # "nt" == windows os , n = ("cls","clear) clear terminal
        print(collection[-1])                              # cmd win == n[0] , others = n[1]
        time.sleep(4)

print(display_latest_metrics())