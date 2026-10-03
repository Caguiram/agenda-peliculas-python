# Agenda de películas 🎬

Aplicación de consola para consultar una agenda de películas y aplicar reglas al cambiar horarios o invitar personas.

**Tecnologías:** Python 3 y biblioteca estándar. No requiere paquetes externos.

## Funcionalidades

- Consultar la película más larga y la duración promedio.
- Buscar estrenos posteriores a un año y contar películas para mayores de edad.
- Reagendar una película verificando conflictos de horario.
- Aplicar preferencias por día, género y hora.
- Evaluar reglas de edad y permiso para invitados.

## Ejecutar

```bash
python consola_peliculas.py
```

Selecciona una opción del menú. Las horas se introducen como enteros en formato de 24 horas: `1930` significa 19:30.

## Pruebas

```bash
python -m unittest discover -s tests -v
```

La comprobación de solapamientos convierte las horas HHMM a minutos antes de sumar duraciones. Incluye un caso de regresión para una película que comienza a las 19:30 y dura 90 minutos.

## Estructura y alcance

```text
consola_peliculas.py   Menú y agenda de ejemplo
modulo_peliculas.py    Consultas y reglas
tests/                Pruebas de horarios y consultas
```

Los cambios viven en memoria y se pierden al salir. La aplicación usa datos de ejemplo, no una base de datos ni una API externa. La consola conserva el alcance académico: entradas no numéricas pueden producir errores y los intervalos se comparan dentro del mismo día; no contempla reprogramaciones que crucen medianoche hacia otro día.

## Contexto

Proyecto universitario de la carpeta de entrega de **Cristian Aguirre**. Esta versión conserva la separación entre lógica y consola, añade documentación y corrige la comparación de duraciones con horas HHMM.
