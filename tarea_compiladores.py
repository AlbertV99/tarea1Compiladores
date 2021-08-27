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
token = ''
nro_linea = 1
while (caracter != EOF) :

    variable = tabla.buscar(caracter)
    linea += variable.nombre_token + ' '
    caracter = fichero.readline(1)
    if (caracter == '\n') :
        print (linea + '\n')
        linea = ''
        nro_linea += 1
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
                token = 'NUMBER'
                variable = tabla.buscar(token)
                linea += variable.nombre_token + ' '
                break
    elif (caracter == 'f') : #quiere decir que lo mas probable es que venga un falso
        lista = ['f','a','l','s','e']
        lexema = ''
        while (caracter in lista) :
            lexema += caracter
            caracter = fichero.readline(1)
        variable = tabla.buscar(lexema)
        linea += variable.nombre_token + ' '
    elif (caracter == 't') : #quiere decir que probablemente sea un true
        lista = ['t','r','u','e']
        lexema = ''
        while (caracter in lista) :
            lexema += caracter
            caracter = fichero.readline(1)
        variable = tabla.buscar(lexema)
        linea += variable.nombre_token + ' '
    lexema = ''
    #print (caracter)
fichero.close()
