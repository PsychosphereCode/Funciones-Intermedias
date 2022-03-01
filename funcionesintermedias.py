# x = [ [5,2,3], [10,8,9] ] 
# estudiantes = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# directorio_deportes = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # # # Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].

# x[1][0]= 15
# print (x)
# # Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
# estudiantes[0]["last_name"]= "Bryant"
# print (estudiantes)
# # En el directorio_deportes, cambia "Messi" por "Andrés".
# directorio_deportes["fútbol"][0]= "Andres"
# print(directorio_deportes["fútbol"])
# # Cambia el valor 20 en z a 30.
# z[0]["y"] = 30
# print(z)


estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def recorrer_diccionario(lista):
#     for i in range (0, len(lista)):
#         salida =""
#         for key,val in lista[i].items():
#             salida += f" {key} - {val},"
#         print(salida)

# recorrer_diccionario(estudiantes)


# # debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# # un bonus para que aparezcan exactamente como se muestra a continuación)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel

# # 3 Obtener valores de una lista de diccionarios


def recorrer_diccionario2(key_name, lista):
    for i in range (0, len(lista)):
        for key,val in lista[i].items():
            if key== key_name:
                print (val)

recorrer_diccionario2('first_name', estudiantes)
recorrer_diccionario2('last_name', estudiantes)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_information(dict):
    for key,value in dict.items():
        print("-------")
        print(f"{key.upper()} {len(value)}")
        for i in range(0, len(value)):
            print(value[i])


print_information(dojo)