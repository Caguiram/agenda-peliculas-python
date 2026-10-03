import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import modulo_peliculas as mp


class AgendaTests(unittest.TestCase):
    def setUp(self):
        self.agenda = [{"nombre": "Ejemplo", "genero": "Familiar",
                        "duracion": 90, "anio": 2020, "clasificacion": "todos",
                        "hora": 1930, "dia": "jueves"}]

    def test_detecta_conflicto_al_cruzar_una_hora(self):
        self.assertTrue(mp.hay_conflicto(self.agenda, "jueves", 2030, 30))

    def test_permite_empezar_al_terminar_otra_pelicula(self):
        self.assertFalse(mp.hay_conflicto(self.agenda, "jueves", 2100, 30))

    def test_dias_distintos_no_entran_en_conflicto(self):
        self.assertFalse(mp.hay_conflicto(self.agenda, "viernes", 2000, 30))

    def test_reagendar_ignora_la_pelicula_actual(self):
        ok, _ = mp.reagendar_pelicula("Ejemplo", "jueves", 2000, False, self.agenda)
        self.assertTrue(ok)
        self.assertEqual(self.agenda[0]["hora"], 2000)

    def test_promedio_y_busqueda(self):
        self.assertEqual(mp.duracion_promedio(self.agenda), "01:30")
        self.assertIsNotNone(mp.buscar_pelicula("EJEMPLO", self.agenda))

    def test_rechaza_horas_invalidas(self):
        with self.assertRaises(ValueError):
            mp.hay_conflicto(self.agenda, "jueves", 1965, 30)


if __name__ == "__main__":
    unittest.main()
