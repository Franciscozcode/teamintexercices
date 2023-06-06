#Almacenar la temperatura que quiere convertir el usuario.

user_temp = int(input("Convert the temperature from Farenheit to Celsius: "))


#Usar el valor proporcionado por el usuario para aplicar la formula de conversion.

result = (user_temp-32) * 5 / 9 

print(f"The temperature is:  {result} º Celsius")

#revisar el resultado porque imprime demasiado numeros despues de la coma.