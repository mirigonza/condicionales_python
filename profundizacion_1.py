# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''
# Empezar aquí la resolución del ejercicio

print('Ejercicios de práctica con números')

one = int(input('Ingrese el primer número:\n'))

two = int(input('Ingrese el segundo número:\n'))
print('Ejercicios de práctica con números')

diferencia = one - two 
print("la diferencia entre one y two es",diferencia)

if diferencia > 0: 
    print("el resultado es positivo")
elif diferencia == 0:
    print("el resultado es 0") 
else:
    print("el resultaod es negativo")
    



