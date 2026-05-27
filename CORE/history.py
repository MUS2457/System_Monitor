def view_history(collection, n = 5) :
    if not collection:
        print("please wait until data been collected.")
        return

    count = min(n, len(collection))

    for metics in collection[-count:] :

        print(metics)


def export_history(collection, filename="history.log"):
    if not collection:
        print("No history to export.")
        return


    speed_up = collection[0].up_speed    # use speed of metric
    speed_down = collection[0].down_speed

    with open(filename, "w") as file:
        for metric in collection:
            file.write("\n---------------------------\n")
            file.write(f"timestamp: {metric.time}\n")
            file.write(f"cpu: {metric.cpu}\n")
            file.write(f"ram: {metric.ram}\n")
            file.write(f"disk total: {metric.disk[0]}\n")
            file.write(f"disk used: {metric.disk[1]}\n")
            file.write(f"disk free: {metric.disk[2]}\n")
            file.write(f"net up: {metric.net_up}\n")
            file.write(f"net down: {metric.net_down}\n")
            file.write(f"speed up: {speed_up}\n")
            file.write(f"speed down: {speed_down}\n")
            file.write("---------------------------\n")






