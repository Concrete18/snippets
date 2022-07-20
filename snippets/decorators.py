import time


def keyboard_interrupt(func):
    """
    Catches all KeyboardInterrupt exceptions.
    Closes with a message and delayed program exit.
    """

    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            delay = 1
            print(f"\nClosing in {delay} second(s)")
            time.sleep(delay)
            exit()

    return wrapped


def benchmark(func):
    """
    Prints `func` name and a benchmark for runtime.
    """

    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = round(end - start, 2)
        print(f"{func.__name__} Completion Time: {elapsed}")
        return value

    return wrapped
