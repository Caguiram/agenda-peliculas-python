"""
Modulo de funciones para manejar la agenda de películas.
"""

def buscar_pelicula(nombre, agenda):
    for pelicula in agenda:
        if pelicula["nombre"].lower() == nombre.lower():
            return pelicula
    return None

def pelicula_mas_larga(agenda):
    return max(agenda, key=lambda p: p["duracion"])

def duracion_promedio(agenda):
    total = sum(p["duracion"] for p in agenda)
    promedio = total // len(agenda)
    horas = promedio // 60
    minutos = promedio % 60
    return f"{horas:02d}:{minutos:02d}"

def peliculas_estreno_despues(agenda, anio):
    return [p["nombre"] for p in agenda if p["anio"] > anio]

def contar_peliculas_18_mas(agenda):
    return sum(1 for p in agenda if p["clasificacion"] == "18+")

def _hora_a_minutos(hora):
    horas, minutos = divmod(hora, 100)
    if not (0 <= horas < 24 and 0 <= minutos < 60):
        raise ValueError("La hora debe estar en formato HHMM válido.")
    return horas * 60 + minutos


def hay_conflicto(agenda, dia, hora, duracion, ignorar_nombre=None):
    hora_ini = _hora_a_minutos(hora)
    hora_fin = hora_ini + duracion
    for p in agenda:
        if ignorar_nombre and p["nombre"].lower() == ignorar_nombre.lower():
            continue
        if p["dia"].lower() == dia.lower():
            p_ini = _hora_a_minutos(p["hora"])
            p_fin = p_ini + p["duracion"]
            if not (hora_fin <= p_ini or hora_ini >= p_fin):
                return True
    return False

def violaciones_preferencias(pelicula, nuevo_dia, nueva_hora):
    generos = [g.strip().lower() for g in pelicula["genero"].split(",")]
    hora = nueva_hora
    if "documental" in generos and hora >= 2200:
        return True
    if "drama" in generos and nuevo_dia.lower() == "viernes":
        return True
    if nuevo_dia.lower() in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
        if hora >= 2300 or hora < 600:
            return True
    return False

def reagendar_pelicula(nombre, nuevo_dia, nueva_hora, respetar_preferencias, agenda):
    pelicula = buscar_pelicula(nombre, agenda)
    if not pelicula:
        return False, "Película no encontrada."
    if hay_conflicto(agenda, nuevo_dia, nueva_hora, pelicula["duracion"], ignorar_nombre=nombre):
        return False, "Conflicto con otra película en la agenda."
    if respetar_preferencias and violaciones_preferencias(pelicula, nuevo_dia, nueva_hora):
        return False, "No cumple tus preferencias personales."
    pelicula["dia"] = nuevo_dia
    pelicula["hora"] = nueva_hora
    return True, "Película reagendada con éxito."

def puede_invitar(nombre, edad_invitado, tiene_permiso, agenda):
    pelicula = buscar_pelicula(nombre, agenda)
    if not pelicula:
        return False, "Película no encontrada."
    generos = [g.strip().lower() for g in pelicula["genero"].split(",")]
    clasificacion = pelicula["clasificacion"]
    if edad_invitado >= 18:
        return True, "Puedes invitarlo."
    if "terror" in generos and edad_invitado < 15:
        return False, "No puedes invitar a menores de 15 a ver Terror."
    if edad_invitado <= 10 and "familiar" not in generos:
        return False, "Solo puedes invitarlo si la película es Familiar."
    clasificaciones = {"todos": 0, "7+": 7, "13+": 13, "16+": 16, "18+": 18}
    edad_requerida = clasificaciones.get(clasificacion, 100)
    if edad_invitado < edad_requerida and "documental" not in generos:
        if not tiene_permiso:
            return False, "Necesita permiso de los padres."
    return True, "Puedes invitarlo."
