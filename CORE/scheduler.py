from time import sleep
from CORE import collector

def scheduler():

    while True:
        snapshot_1 = collector.collect_metrics()
        sleep(1)
        snapshot_2 = collector.collect_metrics()

        # calculate speeds
        upload_speed  = (snapshot_2['net_up']   - snapshot_1['net_up'])   / (snapshot_2['timestamp'] - snapshot_1['timestamp'])
        download_speed = (snapshot_2['net_down'] - snapshot_1['net_down']) / (snapshot_2['timestamp'] - snapshot_1['timestamp'])

        data = {
            "timestamp": snapshot_2["timestamp"],
            "cpu": snapshot_2["cpu"],
            "ram": snapshot_2["ram"],
            "disk": snapshot_2["disk"],
            "upload_speed": upload_speed,
            "download_speed": download_speed
        }

        yield data
