"""Contar el número de espacio en un string dado."""
# string= "h o l a"
# def count_space(string):
#     list(string)
#     for i in string:
#         if i is " ":
#             return string.count(i)

# print(count_space("h o l a e s t o y p r a cticando"))

"""Plantear 2 formas de encontrar los números comunes entre 2 listas sin usar set."""
# list1=[1,2,3,5,6,7,8]
# list2=[1,4,3,2,5,6,7,8]
# ##Forma 1
# def common_element(list1,list2):
#     new_list=[]
#     for i in list1:
#         if i in list2:
#             new_list.append(i)
#     print(new_list)

# common_element(list1,list2)
##Forma 2

# def common_element2(list1,list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 print(i)

# common_element2(list1,list2)

"""Encontrar todos los números comprendidos entre 7 y 537 que contengan el dígito 7"""
##forma1
# numbers= [i for i in range(7,538,10)]
# print(numbers)
##forma2
# def number_with_seven():
#     for i in range(7,538,10):
#         print(i)

# number_with_seven()

"""Para los números entre 10 y 500, expresar en un diccionario el número y su respectivo dígito más alto por el cuál es divisible. 
Por ejemplo para 328 es 8."""

# numero= [i for i in range(10,501)]
# divisores=[n for n in range(1,501)]
# divisor=[]
# maximo_divisor= []
# for h in numero:
#     for i in divisores:
#         if h % i== 0:
#             divisor.append(i)
#     maximo_divisor.append(divisor[-2])
# #numeros_string= str(numero)
# # print(numero)
# # print(maximo_divisor)
# resultado= {str(numero[m]): maximo_divisor[m] for m in range(len(numero))}
# #res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
# print(resultado)

####finallllll

# numero= [i for i in range(10,501)]
# def max_divisible(numero):
#     divisores=[n for n in range(1,501)]
#     divisor=[]
#     maximo_divisor= []
#     for h in numero:
#         for i in divisores:
#             if h % i== 0:
#                 divisor.append(i)
#         maximo_divisor.append(divisor[-2])
#     resultado= {str(numero[m]): maximo_divisor[m] for m in range(len(numero))}
#     print(resultado)

# max_divisible(numero)

"""Escribir una función extrae_columna_n que reciba como parámetro una lista M y un valor n. La función debe extraer los valores 
"de la columna" n específica a la lista anidada dada. La función debe verificar que n esté en el rango permitido. Caso contrario, 
la función debe retornar una lista vacía.

Ejemplo:

M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

n = 0

Para extrae_column_n(M, n) la función retornará [1, 2, 1]"""
M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(M[0])
print(f'La PRIMERA COLUMNA es 0: {M[0]} \n La SEGUNDA COLUMNA es 1: {M[1]} \n La TERCERA COLUMNA es 2: {M[2]}')
n= int(input("Ingrese el numero de columna que necesita extraer, iniciando desde el 0... "))

def extrae_columna_n(M,n):
    for i in M:
        resultado= M[n]
        return resultado

print(extrae_columna_n(M, n))




#extrae_column_n(M, n)