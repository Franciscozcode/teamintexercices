#Create a Python program that reads a text file and counts the ocurrcences of each word using a dictionary. 
#The program should print the words and their counts.

#abrir el archivo

text = open("textingredients.txt","r")

#Crear un diccionario vacio para almacenar los datos.
list_dictionaire = dict()

for line in text:
    line = line.strip()
    line = line.lower()
    
    words = line.split(" ")

for word in words:
    if word in list_dictionaire:
        list_dictionaire[word] = list_dictionaire[word] + 1
    else:
        list_dictionaire[word] = 1

for values in list(list_dictionaire.keys()):
    print(values, ":", list_dictionaire[values])

