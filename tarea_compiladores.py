import tabla_simbolos as p
EOF = ''
#declarar una variable de tipo tabla e inicializarla
tabla = p.TablaSimbolos()
tabla.iniciar_tabla()
tabla.inicializar_tabla()

fichero = open('prueba.txt', 'r')#aqui iria el nombre del archivo que se quiere analizar
caracter = fichero.readline(1)
#lista = fichero.readlines()
#cadena = ''
variable = ''
linea = ''
while (caracter != EOF) :

    variable = tabla.buscar(caracter)
    linea += variable.nombre_token + ' '
    caracter = fichero.readline(1)
    if (caracter == '\n') :
        print (linea + '\n')
        linea = ''
    elif (caracter == '"') :
        #aqui encontre una cadena
        while (True):
            caracter = fichero.readline(1)
            if (caracter == '"'):
                caracter = 'STRING'
                break
    elif (str(caracter).isnumeric()) :
        #aqui encontre un numero
        while (True):
            caracter = fichero.readline(1)
            if (caracter == '' or caracter == '\n' or caracter == ',') :
                caracter = 'NUMBER'
                break

    #print (caracter)
fichero.close()
