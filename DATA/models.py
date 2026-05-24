from datetime import datetime

class Snapshot :
    def __init__(self, time, cpu, ram, disk, net_up, net_down):
        self.time = time
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.net_up = net_up
        self.net_down = net_down

    def __str__(self):
        dt = datetime.fromtimestamp(self.time).strftime("%Y-%m-%d %H:%M:%S")

        return (
            f"Time: {dt} | "
            f"CPU: {self.cpu}% | "
            f"RAM: {self.ram}% | "
            f"Disk total: {int(self.disk[0] / (1024 ** 2))} MiB | "
            f"Disk used: {int(self.disk[1] / (1024 ** 2))} MiB, percentage: {self.disk[3]}% | "
            f"Disk free: {int(self.disk[2] / (1024 ** 2))} MiB | "
            f"Network up: {int(self.net_up / 10 ** 6)} MB | "
            f"Network down: {int(self.net_down / 10 ** 6)} MB"
        )



class Metrics :
    def __init__(self, time, cpu, ram, disk, net_up, net_down):
        self.time = time
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.net_up = net_up
        self.net_down = net_down

    def __str__(self):
        dt = datetime.fromtimestamp(self.time).strftime("%Y-%m-%d %H:%M:%S")

        return (
            f"Time: {dt} | "
            f"CPU: {self.cpu}% | "
            f"RAM: {self.ram}% | "
            f"Disk total: {int(self.disk[0] / (1024 ** 2))} MiB | "
            f"Disk used: {int(self.disk[1] / (1024 ** 2))} MiB, percentage: {self.disk[3]}% | "
            f"Disk free: {int(self.disk[2] / (1024 ** 2))} MiB | "
            f"Network up: {int(self.net_up / 10 ** 6)} MB | "
            f"Network down: {int(self.net_down / 10 ** 6)} MB"
        )



