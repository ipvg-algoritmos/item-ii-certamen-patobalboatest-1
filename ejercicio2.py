# 📝 ejercicio2.py
# 🎓 Promedio de notas
# Puntaje: 12 puntos

# Instrucciones:
# 1. Solicita cuántas notas ingresará el usuario.
# 2. Usa un ciclo para pedir las notas una por una y guárdalas en una lista.
# 3. Calcula el promedio con dos decimales.
# 4. Muestra si el promedio es suficiente para aprobar (4.0 o más) o no.
# 5. Todas las notas deben estar entre 1.0 y 7.0.

# 👇 Aquí comienza tu código

cuantas_notas = int(input("Cuantas notas deseas ingresar?: "))
notas = []
for i in range(cuantas_notas):
    while True:
        nota = float(input(f"Ingresa la {i+1}° nota entre 1 y 7:"))
        if nota >= 1.0 or nota <= 7.0:
            notas.append(nota)
            break
        else:
            print("Ingresa una nota valida entre 1 y 7")

promedio = round(sum(notas)/cuantas_notas,2)
if nota >= 4.0:
    print("Aprobaste")
else:
    print("Hay tabla")