import storage


def history_viewer(n=5):
    
    buffer = storage.buffer_metrics()

    if not buffer:
        print("No history yet, wait for data to be collected")
        return

    count = min(n, len(buffer))

    for metric in buffer[-count:]:
        print(metric)
