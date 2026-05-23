import psutil
import time

def collect_metrics():
    timestamp = int(time.time())


    cpu = psutil.cpu_percent(interval=0)  # instant cpu snapshot (no averaging delay)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/')   # root (psutil maps '/' to system drive on Windows)

    # network counters since boot (used to compute speed)
    network = psutil.net_io_counters()
    net_up = network.bytes_sent
    net_down = network.bytes_recv

    return {
        "timestamp": timestamp,
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "net_up": net_up,
        "net_down": net_down
    }
