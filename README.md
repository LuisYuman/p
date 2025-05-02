# 🧠 GremorySintax

Un mini compilador educativo desarrollado en Python que realiza análisis léxico y sintáctico para un lenguaje personalizado llamado **GremorySintax**. Este proyecto fue creado como parte del curso de Compiladores.

---

## 📌 Descripción

**GremorySintax** es un lenguaje de programación simple con sintaxis parecida a pseudocódigo. Permite:

- Declarar variables (`int`, `float`, `string`)
- Estructuras de control (`if`, `while`)
- Funciones (`function`)
- Entrada y salida (`input`, `print`)
- Retornos y valores booleanos

El compilador detecta errores léxicos y sintácticos, genera tablas y construye árboles de derivación.

---

## 🔧 Herramientas utilizadas

- **Python 3**
- Módulo estándar `re` para expresiones regulares
- Entrada definida directamente en el código (`codigo_prueba`)

---

## 🧩 Componentes del proyecto

### 🔍 Análisis Léxico

Se realiza con expresiones regulares y genera:

- ✅ Tokens
- ✅ Tabla de símbolos
- ✅ Tabla de errores léxicos

### 📐 Expresiones Regulares

| Tipo | Regex | Descripción |
|------|-------|-------------|
| Palabras reservadas | `\b(if|else|for|while|...)\b` | Detecta palabras del lenguaje |
| Identificadores | `\b[a-zA-Z][a-zA-Z0-9]{0,14}\b` | Letras y números (máx 15) |
| Constantes | `\d+` / `\d+\.\d+` | Enteros / Decimales |
| Cadenas | `".*?"` | Texto entre comillas |
| Comentarios | `//.*` / `/\*[\s\S]*?\*/` | Una o varias líneas |
| Operadores | `+ - * / %`, `:=`, `>= <= == !=`, etc. | Aritméticos, lógicos, relacionales |
| Símbolos | `[{}\[\]()".,;]` | Caracteres especiales |

### 🧠 Análisis Sintáctico

Simula una gramática **BNF** validando estructuras como:

```bnf
<condicional> ::= if <identificador> <operador_relacional> <constante> { <programa> }
<declaracion> ::= <tipo> <identificador> := <constante>
<funcion> ::= function <identificador> { <programa> }
