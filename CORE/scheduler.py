from  time import sleep
from CORE import collector
from DATA.models import Metrics

def scheduler():

    while True:
        snapshot_1 = collector.collect_metrics()
        sleep(1)
        snapshot_2 = collector.collect_metrics()

        time_interval = snapshot_2.time - snapshot_1.time

        up_speed = (snapshot_2.net_up- snapshot_1.net_up)/ time_interval 
        down_speed = (snapshot_2.net_down- snapshot_1.net_down)/ time_interval

        metrics = Metrics(snapshot_2.time, snapshot_2.cpu, snapshot_2.ram,
                        snapshot_2.disk,snapshot_2.net_up, snapshot_2.net_down,
                       up_speed, down_speed
        )

        yield metrics
