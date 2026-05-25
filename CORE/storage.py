from CORE import scheduler

def buffer_metrics():
    collection = []

    for metrics in scheduler.scheduler():
        collection.append(metrics)
        yield collection

from history import history_viewer

history_viewer()