"""
Generador de alumnos y notas aleatorio
El resultado es guardado en notas_{year}.csv
"""

import json
import numpy as np
from random import randint

YEAR = 2019
NALUMNOS = 30
NNOTAS = 3

ARCHIVO_SALIDA = f"notas_{YEAR}.csv"
ARCHIVO_NOMBRES = "nombres.json"


class GeneradorAlumnos:
    """Clase para generar notas de alumnos"""

    def _get_names(self):
        with open(ARCHIVO_NOMBRES, "r") as fn:
            names = json.load(fn)

        return np.random.choice(names, NALUMNOS)

    def _get_random_nota(self):
        return str(randint(1, 10))

    def _store_in_csv(self, alumnos):
        alumno_nota_str = [",".join(alumno_nota) for alumno_nota in alumnos]
        alumnos_str = "\n".join(alumno_nota_str)

        with open(ARCHIVO_SALIDA, "w") as fout:
            fout.write(alumnos_str)

    def generar_alumnos_notas(self):
        nombres = self._get_names()
        alumnos = []
        for nombre in nombres:
            alumno_nota = [nombre]
            for nota in range(NNOTAS):
                alumno_nota.append(self._get_random_nota())

            alumnos.append(alumno_nota)

        self._store_in_csv(alumnos)


ga = GeneradorAlumnos()

print(ga.generar_alumnos_notas())
