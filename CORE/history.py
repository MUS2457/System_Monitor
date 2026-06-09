import os
from datetime import datetime

def view_history(collection, n = 5) :
    if not collection:
        print("Run display metrics first for data collection.")
        return

    count = min(n, len(collection))

    for metics in collection[-count:] :

        print(metics)


def export_history(collection, filename = "history.log"):
    if not collection:
        print("No history to export.")
        return


    speed_up = collection[0].up_speed    # use speed of metric
    speed_down = collection[0].down_speed
    

    with open(filename, "w") as file:
        for metric in collection:
            date = datetime.fromtimestamp(metric.time)
            tl =int(metric.disk[0] / (1024 ** 2))
            used =int(metric.disk[1] / (1024 ** 2))
            free = int(metric.disk[2] / (1024 ** 2))
            file.write("\n---------------------------\n")
            file.write(f"timestamp: {date}\n")
            file.write(f"cpu: {metric.cpu}\n")
            file.write(f"ram: {metric.ram}\n")
            file.write(f"disk total: {tl} MiB\n")
            file.write(f"disk used: {used} MiB\n")
            file.write(f"disk free: {free} MiB\n")
            file.write(f"disk percentage: {metric.disk[3]}%\n")
            file.write(f"net up: {metric.net_up}\n")
            file.write(f"net down: {metric.net_down}\n")
            file.write(f"speed up: {speed_up}\n")
            file.write(f"speed down: {speed_down}\n")
            file.write("---------------------------\n")


def read_history(filename="history.log"):

    if not os.path.isfile(filename):
        print("file not found, please view history first.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    if not content.strip():
        print("history file is empty.")
        return

    print(content)


if __name__ == "__main__":
    read_history()




