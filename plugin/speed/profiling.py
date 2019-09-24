from functools import wraps
import timeit
import time


def profiling(func):
    """
    量測包裹的 function 運作時間
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = timeit.default_timer()
        result = func(*args, **kwargs)
        time_end = timeit.default_timer()
        print("------------------------------------------------------")
        print(f"［ function name ］: {func.__name__}")
        print(f"［  performance  ］: {time_end - time_start} ms")
        print("------------------------------------------------------")
        return result

    return wrapper
