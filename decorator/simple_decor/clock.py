import time

def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - t0
        print(f"Elapsed : {elapsed_time:0.8f} for Function: {func.__name__} and result : {result}")
        return result
    return clocked
