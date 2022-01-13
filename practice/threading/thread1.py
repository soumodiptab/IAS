import threading
# func1 and func2 are thread function.
#  thread 1 is created for func1
# thread 2 is created for func2


def func1():
    for i in range(1, 3):
        print("hello world")


def func2():
    for i in range(1, 3):
        print("hello space")


t1 = threading.Thread(target=func1, args=())
t2 = threading.Thread(target=func2, args=())
t1.start()
t2.start()
t1.join()
t2.join()
