import os
from CORE import scheduler


def display_latest_metrics():
    for metrics in scheduler.scheduler() :
        os.system("cls" if os.name == "nt" else "clear")  # "nt" == windows os , n = ("cls","clear) clear terminal
        print(metrics)                                        # cmd win == n[0] , others = n[1])