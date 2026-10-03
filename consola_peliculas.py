"""
Interfaz de usuario para la agenda de películas basada en consola.
"""

import modulo_peliculas as mp

agenda = [
    {
        "nombre": "Inception",
        "genero": "Thriller, Ciencia-Ficción",
        "duracion": 148,
        "anio": 2010,
        "clasificacion": "13+",
        "hora": 2100,
        "dia": "viernes"
    },
    {
        "nombre": "Shrek",
        "genero": "Familiar, Comedia",
        "duracion": 90,
        "anio": 2001,
        "clasificacion": "todos",
        "hora": 1600,
        "dia": "sabado"
    },
    {
        "nombre": "Get Out",
        "genero": "Terror",
        "duracion": 104,
        "anio": 2017,
        "clasificacion": "18+",
        "hora": 2200,
        "dia": "sabado"
    },
    {
        "nombre": "Icarus",
        "genero": "Documental",
        "duracion": 121,
        "anio": 2017,
        "clasificacion": "18+",
        "hora": 2000,
        "dia": "domingo"
    },
    {
        "nombre": "The Social Dilemma",
        "genero": "Drama",
        "duracion": 94,
        "anio": 2020,
        "clasificacion": "13+",
        "hora": 1930,
        "dia": "jueves"
    }
]

def main():
    while True:
        print("\n--- Mi Agenda de Películas ---")
        print("1. Consultar película más larga")
        print("2. Consultar duración promedio")
        print("3. Buscar estrenos después de un año")
        print("4. Contar películas 18+")
        print("5. Reagendar película")
        print("6. Decidir invitar a alguien")
        print("7. Ver toda la agenda")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            p = mp.pelicula_mas_larga(agenda)
            print(f"La pelicula mas larga es {p['nombre']} con {p['duracion']} minutos de duracion.")
        elif opcion == "2":
            promedio = mp.duracion_promedio(agenda)
            print(f"La duracion promedio de las peliculas en horas y minutos es igual a {promedio}.")
        elif opcion == "3":
            anio = int(input("Año mínimo de estreno: "))
            resultado = mp.peliculas_estreno_despues(agenda, anio)
            if resultado:
                print(f"Las peliculas estrenadas en una fecha posterior a esta son: {', '.join(resultado)}.")
            else:
                print("No hay peliculas estrenadas despues de ese año.")
        elif opcion == "4":
            cantidad = mp.contar_peliculas_18_mas(agenda)
            print(f"El numero de peliculas 18+ es: {cantidad}.")
        elif opcion == "5":
            nombre = input("Película: ")
            nuevo_dia = input("Día: ")
            nueva_hora = int(input("Hora (formato 24h, ej. 2030): "))
            respetar = input("¿Respetar preferencias personales? (s/n): ").lower() == "s"
            exito, _ = mp.reagendar_pelicula(nombre, nuevo_dia, nueva_hora, respetar, agenda)
            if exito:
                print("La pelicula fue reagendada con éxito.")
            else:
                print("La pelicula no pudo ser reagendada.")
        elif opcion == "6":
            nombre = input("Película: ")
            edad = int(input("Edad del invitado: "))
            permiso = input("¿Autorización de los padres? (s/n): ").lower() == "s"
            exito, _ = mp.puede_invitar(nombre, edad, permiso, agenda)
            if exito:
                print("Se puede invitar la persona.")
            else:
                print("No se puede invitar la persona.")
        elif opcion == "7":
            for p in agenda:
                print(p)
        elif opcion == "8":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
