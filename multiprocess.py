import multiprocessing as mp
import os

#def info(title):
#    print(title)
#    print(f"{__name__=}")
#    print(f"{os.getppid()=}")
#    print(f"{os.getpid()=}")
#
#def f(name):
#    info("function f")
#    print(f"Hi {name}!")
#
#if __name__ == "__main__":
#    info("main")
#    p = mp.Process(target=f, args=("Bob",))
#    p.start()
#    p.join()

def f(l, i):
    # l.acquire() # Acquire the lock.
    try:
        print(f"Hello: {i}")
    finally:
        pass
        # l.release()

if __name__ == "__main__":
    lock = mp.Lock()

    for n in range(10):
        p = mp.Process(target=f, args=(lock, n))
        p.start()
