# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código
palabra = input("Ingresa una palabra")

def es_palindromo(texto):
    texto = texto.lower()
    texto = texto.replace(" ","")
    if texto == texto[::-1]:
        print("Tu palabra es palindromo")
    else:
        print("Sale asqueroso")

es_palindromo(palabra)