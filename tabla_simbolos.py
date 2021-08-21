L_CORCHETE = 256 #expresion regular = [
R_CORCHETE = 257 #expresion regular = ]
L_LLAVE = 258 #expresion regular = {
R_LLAVE = 259#expresion regular = }
COMA = 260#expresion regular = ,
DOS_PUNTOS = 261 #expresion regular = :
LITERAL_CADENA = 262#expresion regular = " .*"
LITERAL_NUM = 263#expresion regular = [0-9]+(\.[0-9]+)?((e|E)(+|-)?[0-9]+)?
PR_TRUE= 264 #expresion regular = true | TRUE
PR_FALSE = 265 #expresion regular = false | FALSE
PR_NULL = 266  #expresion regular = null | N
LITERAL_CADENA = 267
LITERAL_NUM = 268

class TipoToken :
    def __init__(self, token = '',nombre_token = '', numero = 0):
        self.nombre_token = nombre_token# esto seria el nombre del lexema
        self.lexema = token
        self.numero = numero #esto seria el comp lexico
    def __str__(self):
        cadena = ""
        cadena = ("nombre token:" + str(self.nombre_token) + '\n' +
                    "numero:" + str(self.numero))
        return cadena

class Token :

    def __init__(self, valor_cadena = '', valor_numero = 0, TipoToken = None):
        self.valor_cadena = valor_cadena
        self.valor_numero = valor_numero
        self.tipo_token = TipoToken

    def __str__(self):

        cadena = ""
        cadena = ("cadena :" + str (self.valor_cadena) + '\n' +
                    "numero :" + str(self.valor_numero) + '\n' +
                    "tipo_token :" + str(self.tipo_token))
        return cadena

#creo una clase llamada TablaSimbolos que contendra la tabla de simbolos en si
class TablaSimbolos :

    def __init__(self, tam_tabla = 50) :

        self.tabla = [TipoToken()]*tam_tabla

    #metodo para inicializar la tabla
    def iniciar_tabla (self):

        for a in list(range(len(self.tabla))):
            self.tabla[a].numero = -1
            self.tabla[a].nombre_token = ''
    #metodo que inicializa la tabla por defecto
    def inicializar_tabla (self) :

        self.insertar_en_tabla('[', 'L_CORCHETE', L_CORCHETE)
        self.insertar_en_tabla(']','R_CORCHETE' , R_CORCHETE)
        self.insertar_en_tabla('{', 'L_LLAVE', L_LLAVE)
        self.insertar_en_tabla('}','L_LLAVE', R_LLAVE)
        self.insertar_en_tabla(',','COMA', COMA)
        self.insertar_en_tabla(':','DOS_PUNTOS', DOS_PUNTOS)
        self.insertar_en_tabla('true','PR_TRUE', PR_TRUE)
        self.insertar_en_tabla('false','PR_FALSE',PR_FALSE)
        self.insertar_en_tabla('null','PR_NULL', PR_NULL)
        self.insertar_en_tabla('STRING','STRING',LITERAL_CADENA  )
        self.insertar_en_tabla('NUMBER','NUMBER',LITERAL_NUM)

    #metodo para insertar en la tabla de simbolos
    def insertar (self, entrada ):
        pos = 0
        while (self.tabla[pos].numero != -1) :
            pos += 1
            if (pos == len(self.tabla)) :
                pos = 0
        self.tabla[pos] = entrada

    #metodo previo a la insercion en la tabla de simbolos
    def insertar_en_tabla(self, token,nombre_token, numero):

        entrada = TipoToken (token,nombre_token, numero)
        self.insertar(entrada)

    def buscar (self, clave):
        pos = 0
        while (self.tabla[pos].numero != -1 and (clave != self.tabla[pos].lexema)) :
            pos += 1
            if (pos == len(self.tabla)) :
                pos = 0
        return self.tabla[pos]
