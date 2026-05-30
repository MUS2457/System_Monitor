from CORE import scheduler
import plotext as plt
import time

def show_graph():
    cpu_history, ram_history, disk_history = [], [], []
    x = []  # time steps

    for i, metric in enumerate(scheduler.scheduler()):
        x.append(i)
        cpu_history.append(metric.cpu)
        ram_history.append(metric.ram)
        disk_history.append(metric.disk[3])

        plt.clt()
        plt.title("Live Metrics Usage")

        plt.plot(x, cpu_history, label="CPU", color="red")
        plt.plot(x, ram_history, label="RAM", color="green")
        plt.plot(x, disk_history, label="Disk", color="blue")

        plt.canvas_color("black")
        plt.axes_color("white")
        plt.ticks_color("white")
        plt.show()
        time.sleep(1)

if __name__ == "__main__":
    show_graph()
