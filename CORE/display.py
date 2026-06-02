import os
from CORE import scheduler
from CORE import storage

def display_latest_metrics():
    gen = scheduler.scheduler()

    while True:
        metrics = next(gen)              # get next metric
        storage.buffer_metrics(metrics)  # store it

        os.system("cls" if os.name == "nt" else "clear")
        print(metrics)

        user = input("\nPress [q] to return to menu, Enter to continue: ").strip().lower()
        if user == "q":
            return
