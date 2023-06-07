import time

numbers = [1,9,4,5,6,7,3,32,43,26,23,27,94,72,93,6,26,42,54,26,82,62,84,71]

def lap(*arg):
    start = time.time()
    order_list = sorted(*arg, key=lambda x: x)
    end = time.time()
    print(order_list)
    print(end - start)


lap(numbers)
