"""
Programa del profe CodinEric para calcular los promedios de los alumnos y
guardar todo en su archivo historico
"""

class MiExcepcion(Exception):
    def __init__(self, msg):
        self.msg = msg


class AlumnoHistorico:
    """clase para manejar mi historico de alumnos"""

    def _get_prom(self, notas):
        """Funcion que recive una lista de notas, calcula el promedio y
        devuelve la misma lista con el promedio agregado"""

        prom = 0
        for nota in notas:
            try:
                prom = prom + int(nota)
            except ValueError:
                print("Enviar E-mail")
                raise MiExcepcion("Se ejecuto mi excepcion")
            finally:
                print("Cerramos todos los modulos y conexiones a la base de datos")

        return prom / len(notas)

    def append_historico(self, year):
        """funcion con la logica principal"""
        self.year = year
        self.fn_actual = f"notas_{year}.csv"

        with open(self.fn_actual, "r") as inf:
            notas_str = inf.read()
            notas_lst = notas_str.split("\n")

            proms = []
            for alumno_notas_str in notas_lst:
                alumno_notas = alumno_notas_str.split(",")
                notas = alumno_notas[1:]
                alumno_notas.append(self._get_prom(notas))
                proms.append(alumno_notas)

            print(proms)


if __name__ == "__main__":
    al_hist = AlumnoHistorico()
    al_hist.append_historico("2019")
