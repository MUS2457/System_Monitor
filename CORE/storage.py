from CORE import scheduler

def buffer_metrics():
    collection = []

    for metrics in scheduler.scheduler():
        collection.append(metrics)
        yield collection
