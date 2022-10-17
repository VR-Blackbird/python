def output_result(result, log=None):
    if log is not None:
        log.debug("Got: %r", result)


# A sample function
def add(x, y):
    return x + y


if __name__ == "__main__":
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger("test")
    p = Pool()
    p.apply_async(add, (3, 4), callback=lambda a: output_result(a, log))
    p.close()
    p.join()
