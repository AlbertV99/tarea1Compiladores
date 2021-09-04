import tabla_simbolos as p
ARCHIVO_ENTRADA = 'prueba.txt'
ARCHIVO_SALIDA = 'salida.txt'
EOF = ''

def main():
    tabla = p.TablaSimbolos()
    tabla.iniciar_tabla()
    tabla.inicializar_tabla()
    inicializar_archivo_salida()
    with open(ARCHIVO_ENTRADA) as fichero:
        procesar_fichero(fichero,tabla)
    fichero.close()


def procesar_fichero(fichero,tabla):
    caracter = '1'
    variable = ''
    token = ''
    linea = ''
    nro_linea = 1
    while (caracter != EOF) :
        caracter = fichero.readline(1)
        variable = tabla.buscar(caracter)
        linea += variable.nombre_token + ' '
        if (caracter == '\n') :
            # print (linea + '\n') # imprimir en archivo
            escribir_linea(linea + '\n')
            linea = '' # linea nueva
            nro_linea += 1
        elif (caracter == '"') :
            #aqui encontre una cadena
            token = tabla.buscar(procesar_cadena(fichero))
            linea += token.nombre_token + ' '
        elif (str(caracter).isnumeric()) :
            #aqui encontre un numero
            token = tabla.buscar(procesar_numerico(fichero))
            linea+= token.nombre_token + ' '
        elif (caracter == 'f' or caracter == 't') : #quiere decir que lo mas probable es que venga un falso
            token = tabla.buscar(procesar_booleano(fichero,caracter))
            linea += token.nombre_token + ' '
        lexema = ''


def procesar_cadena(fichero):
    while (True):
        caracter = fichero.readline(1)
        if (caracter == '"'):
            return "STRING"
        if(caracter == EOF):
            raise Exception("Archivo terminado sin cerrar Cadena")


def procesar_numerico(fichero):
    while (True):
        caracter = fichero.readline(1)
        if ((caracter == '' or caracter == '\n' or caracter == ',') and (True)) : #agregar condicion para que siempre encuentre numeros, si encuentra algo extraño, devolver error
            return 'NUMBER'
            break
    pass


def procesar_booleano(fichero,caracter):
    lista = [['f','a','l','s','e'],['t','r','u','e']]
    booleano = caracter
    while (True) :
        caracter = fichero.readline(1)
        booleano += caracter
        if (caracter=='e' ):
            break

    if(booleano == 'false'):
        return 'false'
    if(booleano =='true'):
        return 'true'
    raise Exception ("Hubo un error, valor booleano mal escrito")

    pass

def escribir_linea(linea):
    # print(linea)
    with open(ARCHIVO_SALIDA,'a') as salida :
        salida.write(linea)
    salida.close()

def inicializar_archivo_salida():
    with open(ARCHIVO_SALIDA,'w') as salida :
        print("")
    salida.close()

# NOTE: Agregar excepcion para cuando se llega al final de la linea, y una cadena no se cierra

main()
