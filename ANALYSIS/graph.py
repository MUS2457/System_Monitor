from CORE import scheduler
import plotext as plt

def show_graph():
    cpu_history, ram_history, disk_history = [], [], []
    x = []
    MAX_POINTS = 60  

    for i, metric in enumerate(scheduler.scheduler()): # x represent the metricts time each every few seconds (many sleep())
        x.append(i)  

        cpu = metric.cpu
        ram = metric.ram
        disk = metric.disk[3]  

        cpu_history.append(cpu)
        ram_history.append(ram)
        disk_history.append(disk)

        if len(x) > MAX_POINTS: #limit the gragh for better readability
            x.pop(0)
            cpu_history.pop(0)  #remove first element 
            ram_history.pop(0)
            disk_history.pop(0)


        alert = ""
        if cpu > 85:
            alert += "⚠ HIGH CPU "

        if ram > 85:
           alert += "⚠ HIGH RAM "

        if disk > 85:
           alert += "⚠ HIGH DISK "

        print(alert)


        plt.clt()  # works as frame by frame illution to make it looks like moving
        plt.title("Live Metrics Usage (Normalized 0–100%)")

      
        plt.plot(x, cpu_history, label="CPU", color="red")  # points (x, f(x))
        plt.plot(x, ram_history, label="RAM", color="green")
        plt.plot(x, disk_history, label="Disk", color="blue")

    
        plt.ylim(0, 100)    # define axes limit 
        plt.xlim(0, MAX_POINTS)


        plt.canvas_color("black")  # styling for better view
        plt.axes_color("white")
        plt.ticks_color("white")

        plt.show()
        
