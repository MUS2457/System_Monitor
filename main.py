from CORE import scheduler, storage, history

if __name__ == "__main__":
    metrics = next(scheduler.scheduler())
    coll = storage.buffer_metrics(metrics)
    for n in coll:
        print(n)