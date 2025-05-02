def procesar_instruccion(tokens, i, nivel):
    """
    Procesa una instrucción del árbol de derivación.
    """
    if i >= len(tokens):
        # Si el índice está fuera del rango, no procesar más
        print("Error sintáctico: Índice fuera de rango")
        return i

    token, tipo = tokens[i]
    indent = "|   " * nivel

    if token in ['int', 'float', 'string']:
        # Declaraciones de variables
        print(f"{indent}<declaracion>")
        print(f"{indent}|-- \"{token}\"")
        if i + 1 < len(tokens) and tokens[i+1][1] == 'IDENTIFICADOR':
            print(f"{indent}|-- <identificador> -> {tokens[i+1][0]}")
            i += 2
            if i < len(tokens) and tokens[i][0] == ':=':
                print(f"{indent}|-- \":=\"")
                i += 1
                if i < len(tokens) and tokens[i][1] in ['CONSTANTE ENTERA', 'CONSTANTE DECIMAL', 'CADENA DE TEXTO']:
                    print(f"{indent}`-- <valor> -> {tokens[i][0]}")
                    i += 1
                else:
                    print(f"{indent}Error sintáctico: Falta valor después de ':='")
            else:
                print(f"{indent}Error sintáctico: Falta operador ':=' en la declaración")
        else:
            print(f"{indent}Error sintáctico: Falta identificador después de '{token}'")

    elif token == 'if':
        # Condicionales
        print(f"{indent}<condicional>")
        print(f"{indent}|-- \"if\"")
        i += 1
        if i + 2 < len(tokens) and tokens[i+1][1] == 'OPERADOR RELACIONAL':
            print(f"{indent}|-- <condicion>")
            print(f"{indent}|   |-- <identificador> -> {tokens[i][0]}")
            print(f"{indent}|   |-- <operador_relacional> -> {tokens[i+1][0]}")
            print(f"{indent}`-- <constante> -> {tokens[i+2][0]}")
            i += 3
        else:
            print(f"{indent}Error sintáctico: Condición incompleta en 'if'")
            return i + 1
        if i < len(tokens) and tokens[i][0] == '{':
            print(f"{indent}|-- \"{{\"")
            i += 1
            print(f"{indent}|-- <programa>")
            while i < len(tokens) and tokens[i][0] != '}':
                i = procesar_instruccion(tokens, i, nivel + 1)
            if i < len(tokens) and tokens[i][0] == '}':
                print(f"{indent}`-- \"}}\"")
                i += 1
            else:
                print(f"{indent}Error sintáctico: Falta '}}' para cerrar el bloque 'if'")
        else:
            print(f"{indent}Error sintáctico: Falta '{{' después de la condición 'if'")

    elif token == 'while':
        # Ciclos
        print(f"{indent}<ciclo>")
        print(f"{indent}|-- \"while\"")
        i += 1
        if i + 2 < len(tokens) and tokens[i+1][1] == 'OPERADOR RELACIONAL':
            print(f"{indent}|-- <condicion>")
            print(f"{indent}|   |-- <identificador> -> {tokens[i][0]}")
            print(f"{indent}|   |-- <operador_relacional> -> {tokens[i+1][0]}")
            print(f"{indent}`-- <constante> -> {tokens[i+2][0]}")
            i += 3
        else:
            print(f"{indent}Error sintáctico: Condición incompleta en 'while'")
            return i + 1
        if i < len(tokens) and tokens[i][0] == '{':
            print(f"{indent}|-- \"{{\"")
            i += 1
            print(f"{indent}|-- <programa>")
            while i < len(tokens) and tokens[i][0] != '}':
                i = procesar_instruccion(tokens, i, nivel + 1)
            if i < len(tokens) and tokens[i][0] == '}':
                print(f"{indent}`-- \"}}\"")
                i += 1
            else:
                print(f"{indent}Error sintáctico: Falta '}}' para cerrar el bloque 'while'")
        else:
            print(f"{indent}Error sintáctico: Falta '{{' después de la condición 'while'")

    elif token == 'print':
        # Impresiones
        print(f"{indent}<impresion>")
        print(f"{indent}|-- \"print\"")
        if i + 1 < len(tokens):
            print(f"{indent}`-- <identificador> -> {tokens[i+1][0]}")
            i += 2
        else:
            print(f"{indent}Error sintáctico: Falta identificador después de 'print'")

    elif token == 'input':
        # Entrada de datos
        print(f"{indent}<entrada>")
        print(f"{indent}|-- \"input\"")
        if i + 1 < len(tokens):
            print(f"{indent}`-- <identificador> -> {tokens[i+1][0]}")
            i += 2
        else:
            print(f"{indent}Error sintáctico: Falta identificador después de 'input'")

    elif token in ['true', 'false']:
        # Valores booleanos
        print(f"{indent}<booleano>")
        print(f"{indent}`-- \"{token}\"")
        i += 1

    elif token == 'return':
        # Retorno
        print(f"{indent}<retorno>")
        print(f"{indent}|-- \"return\"")
        i += 1
        if i < len(tokens) and tokens[i][1] in ['IDENTIFICADOR', 'CONSTANTE ENTERA', 'CONSTANTE DECIMAL', 'CADENA DE TEXTO']:
            print(f"{indent}`-- <valor> -> {tokens[i][0]}")
            i += 1
        else:
            print(f"{indent}Error sintáctico: Falta valor después de 'return'")

    elif token in ['begin', 'end']:
        # Bloques
        print(f"{indent}<bloque>")
        print(f"{indent}`-- \"{token}\"")
        i += 1

    else:
        # Token inesperado
        print(f"{indent}Error sintáctico: Token inesperado '{token}'")
        i += 1

    return i