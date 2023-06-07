#Create a Python decorator called timer that measures the time taken to execute a function.
# Use this decorator on a function that sorts a list of random numbers and prints the sorted list.

import time
#funcion para medir el tiempo de ejecucion.
def lap(arg):
    start = time.time()
    end = time.time()
    print(end-start)

# Array de numeros desordenados.
numbers = [1,9,4,5,6,7,3,32,43,26,23,27,94,72,93,6,26,42,54,26,82,62,84,71]

#funcion anonima para ordernar los numeros.
order_list = sorted(numbers, key=lambda x: x)

lap(print(order_list))
