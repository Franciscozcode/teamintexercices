#Secuenciade Fibonacci con for loop.

def fibo(term):
    if term == 0:
        return 0
    elif term == 1:
        return 1
    else:
        #almacenar el primer termino de sucesion de fibonacci.
        a = 0
        #almacenar el segundo termino de la sucesion de Fibonacci.
        b = 1
        for value in range(1, term):
            c = a + b
            a = b
            b = c
        return b

print(fibo(4))