from  time import sleep
from CORE import collector
from DATA.models import Metrics

def scheduler():

    while True:
        snapshot_2 = collector.collect_metrics()
        sleep(4)


        data = Metrics(snapshot_2.time, snapshot_2.cpu, snapshot_2.ram,
                        snapshot_2.disk,snapshot_2.net_up, snapshot_2.net_down
        )

        yield data
