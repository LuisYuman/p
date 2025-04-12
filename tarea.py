import re
import sys

class AnalizadorLexico:
    def __init__(self):
        self.tabla_simbolos = {}
        self.tabla_errores = []
        self.patrones = [
            (r'\b(if|else|for|print|int|true|false|bfhjk)\b', 'PALABRA RESERVADA'),
            (r'\b[a-zA-Z][a-zA-Z0-9]{0,14}\b', 'IDENTIFICADOR'),
            (r'\b\d+\b', 'CONSTANTE ENTERA'),
            (r'\b\d+\.\d+\b', 'CONSTANTE DECIMAL'),
            (r'".*?"', 'CADENA DE TEXTO'),
            (r'//.*', 'COMENTARIO DE UNA LINEA'),
            (r'/\*[\s\S]*?\*/', 'COMENTARIO MULTILINEA'),
            (r'[+\-*/]', 'OPERADOR ARITMETICO'),
            (r'&&|\|\|', 'OPERADOR LOGICO'),
            (r'!', 'OPERADOR DE NEGACION'),
            (r'::=|:=', 'OPERADOR DE ASIGNACION'),
            (r'>=|<=|<>|>|<', 'OPERADOR RELACIONAL'),
            (r'[{}\[\]()".,;]', 'SIMBOLO'),
        ]

    def analizar_codigo(self, codigo):
        tokens = []

        for num_linea, linea in enumerate(codigo.splitlines(), start=1):
            while linea:
                linea = linea.lstrip()
                for patron, tipo in self.patrones:
                    match = re.match(patron, linea)
                    if match:
                        lexema = match.group()
                        tokens.append((lexema, tipo))
                        linea = linea[len(lexema):]

                        if tipo in ['IDENTIFICADOR', 'PALABRA RESERVADA']:
                            if lexema not in self.tabla_simbolos:
                                self.tabla_simbolos[lexema] = tipo
                        break
                else:
                    self.tabla_errores.append((linea[0], num_linea, 'Caracter no reconocido'))
                    tokens.append((linea[0], 'ERROR'))
                    linea = linea[1:]

        return tokens

    def mostrar_tabla_simbolos(self):
        print("\nTabla de Simbolos:")
        for lexema, tipo in self.tabla_simbolos.items():
            print(f'{lexema}: {tipo}')

    def mostrar_tabla_errores(self):
        print("\nTabla de Errores:")
        if not self.tabla_errores:
            print("No se encontraron errores.")
        else:
            for error in self.tabla_errores:
                print(f'Linea {error[1]}: {error[0]} -> {error[2]}')

    def generar_arbol_derivacion(self, tokens):
        print("\nArbol de Derivacion:")
        i = 0
        while i < len(tokens):
            token, tipo = tokens[i]
            if token == 'if':
                print("<programa>")
                print("|-- <condicional>")
                print("|   |-- \"if\"")
                if i + 3 < len(tokens) and tokens[i+2][0] == ':=':
                    print("|   |-- <expresion>")
                    print("|   |   |-- <asignacion>")
                    print(f"|   |   |   |-- <identificador> -> {tokens[i+1][0]}")
                    print("|   |   |   |-- \":=\"")
                    print(f"|   |   |   `-- <constante> -> {tokens[i+3][0]}")
                    i += 4
                if i < len(tokens) and tokens[i][0] == '{':
                    print("|   |-- \"{\"")
                    print("|   |-- <programa>")
                    i += 1
                    while i < len(tokens) and tokens[i][0] != '}':
                        if tokens[i][0] == 'print':
                            print("|   |   `-- <impresion>")
                            print("|   |       |-- \"print\"")
                            print("|   |       `-- <expresion>")
                            if i + 3 < len(tokens):
                                print(f"|   |           |-- <identificador> -> {tokens[i+1][0]}")
                                print(f"|   |           |-- \"{tokens[i+2][0]}\"")
                                print(f"|   |           `-- <constante> -> {tokens[i+3][0]}")
                                i += 4
                        else:
                            i += 1
                    print("|   `-- \"}\"")
            else:
                i += 1

    def verificar_contra_bnf(self, tokens):
        print("\nVerificacion BNF (simulada):")
        if ('if', 'PALABRA RESERVADA') in tokens and (':=', 'OPERADOR DE ASIGNACION') in tokens:
            print("Cumple con la regla de condicional y asignacion basica")
        else:
            print("No cumple con la regla de condicional/asignacion esperada")

# Codigo de prueba
ejemplo_codigo = """
if pepe := 25 {
    print pepe + 5;
    // Comentario de prueba
    "hola mundo"
    true && false
    @
}
"""

analizador = AnalizadorLexico()
tokens = analizador.analizar_codigo(ejemplo_codigo)

# Mostrar tokens
table_output = "\nTokens detectados:" 
for token in tokens:
    table_output += f'\n{token[1]}: {token[0]}'
print(table_output)

# Mostrar tabla de simbolos
analizador.mostrar_tabla_simbolos()

# Mostrar tabla de errores
analizador.mostrar_tabla_errores()

# Generar arbol de derivacion segun tokens
analizador.generar_arbol_derivacion(tokens)

# Verificar si el codigo cumple con las reglas de BNF
analizador.verificar_contra_bnf(tokens)
