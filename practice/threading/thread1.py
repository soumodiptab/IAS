import threading
# func1 and func2 are thread function.
#  thread 1 is created for func1
# thread 2 is created for func2


def func1(x):
    for i in range(1, 3):
        print("hello world")


def func2(x):
    for i in range(1, 3):
        print("hello space")


t1 = threading.Thread(target=func1, args=(12,))
t2 = threading.Thread(target=func2, args=(13,))
t1.start()
t2.start()
t1.join()
t2.join()
