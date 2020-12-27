import time
from types import FunctionType


def get_exec_time(func: FunctionType):
    def wrapper(*args, **kwargs):
        btime = time.time()
        result = func(*args, **kwargs)
        etime = time.time()-btime
        print("函数<{}>，运行耗时{}秒...".format(func.__name__, round(etime, 2)))
        return result
    return wrapper


if __name__ == "__main__":
    @get_exec_time
    def a(b, c):
        for _ in range(100000000):
            b+c
    a(10, 20)
