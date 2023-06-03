import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print('Start')
        func(*args, **kwargs)
        print('End')
        end = time.time()
        print(end - start)

    return wrapper()


def hello():
    print('Hello World!!!')


timer(hello)

