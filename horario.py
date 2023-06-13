import numpy as np


class Horario:
    def __init__(self, cursoID, grupoID, matriculaDocente):  # Define un nuevo individuo al horario.
        self.cursoID = cursoID  # Informatica
        self.grupoID = grupoID  # Grupo B
        self.matriculaDocente = matriculaDocente  # 193286 - Ing. Ivan
        self.numAula = 0
        self.diaSemanal = 0
        self.cupo = 0

    def genPosAle(self, rangoAula):  # Define el aula y la posicion dentro del horario.
        self.numAula = np.random.randint(1, rangoAula + 1, 1)[0]
        self.diaSemanal = np.random.randint(1, 6, 1)[0]
        self.cupo = np.random.randint(1, 6, 1)[0]


def buscarConflictos(poblacion, grupoElite): # Nuestra creacion del fenotipo.
    conflictos = []
    numIndi = len(poblacion[0])
    for p in poblacion:
        contadorConflictos = 0
        for i in range(0, numIndi - 1):
            for j in range(i + 1, numIndi):
                # Comprobar que el curso no disponga el mismo horario y aula que otro curso, prioritario...
                if p[i].numAula == p[j].numAula and p[i].diaSemanal == p[j].diaSemanal and p[i].cupo == p[j].cupo:
                    contadorConflictos += 1
                # Comprobar que el curso no se imparta dos veces hacia el mismo grupo.
                if p[i].grupoID == p[j].grupoID and p[i].diaSemanal == p[j].diaSemanal and p[i].cupo == p[j].cupo:
                    contadorConflictos += 1
                # Comprobar que el docente no imparta el curso de otro docente.
                if p[i].matriculaDocente == p[j].matriculaDocente and p[i].diaSemanal == p[j].diaSemanal and p[i].cupo == p[j].cupo:
                    contadorConflictos += 1
                # Comprobar que el grupo no le toque la misma clase que otro grupo en el mismo dia.
                if p[i].grupoID == p[j].grupoID and p[i].cursoID == p[j].cursoID and p[i].diaSemanal == p[j].diaSemanal:
                    contadorConflictos += 1
        conflictos.append(contadorConflictos)
    index = np.array(conflictos).argsort()
    return index[: grupoElite], conflictos[index[0]]
