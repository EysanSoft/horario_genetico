import copy
import numpy as np
from horario import buscarConflictos


class OptimizadorGenetico:
    def __init__(self, poblaMax=30, probMut=0.3, numElites=5, iterMaxCon=100):  # Inicializar el horario
        # Tamaño de la poblacion, 5 x 5
        self.poblaMax = poblaMax
        # Probabilidad de mutacion
        self.probMut = probMut
        # Numero de elites (mejores individuos)
        self.numElites = numElites
        # Numero maximo de iteraciones por conflicto
        self.iterMaxCon = iterMaxCon

    def poblarPoblacionInicial(self, cupos, rangoAula):
        # Llenar los cupos del horario segun la poblacion.
        self.poblacion = []
        for i in range(self.poblaMax):
            entidades = []
            for c in cupos:
                c.genPosAle(rangoAula)
                entidades.append(copy.deepcopy(c))
            self.poblacion.append(entidades)

    def mutar(self, poblacionElite, rangoAula):
        # En caso de caer en mutacion, un individuo elite aleatorio cambiara de posicion, para liberar cupo.
        posEli = np.random.randint(0, self.numElites, 1)[0]
        eliMut = copy.deepcopy(poblacionElite[posEli])
        for e in eliMut:
            pos = np.random.randint(0, 3, 1)[0]
            numMagico = np.random.rand()
            if pos == 0:
                e.numAula = self.evaluarCupoMutado(e.numAula, numMagico, rangoAula)
            if pos == 1:
                e.diaSemanal = self.evaluarCupoMutado(e.diaSemanal, numMagico, 5)
            if pos == 2:
                e.cupo = self.evaluarCupoMutado(e.cupo, numMagico, 5)
        return eliMut

    def evaluarCupoMutado(self, factorActual, magico, rangoAula):
        # Dependiendo del valor generado en la mutacion, se determina que posicion el individuo tomara segun los atributos.
        if magico > 0.5:
            if factorActual < rangoAula:
                factorActual += 1
            else:
                factorActual -= 1
        else:
            if factorActual - 1 > 0:
                factorActual -= 1
            else:
                factorActual += 1
        return factorActual

    def cruzar(self, poblacion):
        # Cruza para casteo entre elites.
        posEli1 = np.random.randint(0, self.numElites, 1)[0]
        posEli2 = np.random.randint(0, self.numElites, 1)[0]
        pos = np.random.randint(0, 2, 1)[0]
        eli1 = copy.deepcopy(poblacion[posEli1])
        eli2 = poblacion[posEli2]

        for e1, e2 in zip(eli1, eli2):
            if pos == 0:
                e1.diaSemanal = e2.diaSemanal
                e1.cupo = e2.cupo
            if pos == 1:
                e1.numAula = e2.numAula
        return eli1

    def bucleFitness(self, cupos, rangoAula):  # Formacion y ejecuccion del fitness.
        aptitud = 0  # numero de conflicto, siendo el 0 que termine con el programa.
        horarioOptimo = None
        self.poblarPoblacionInicial(cupos, rangoAula)

        for i in range(self.iterMaxCon):
            indiceElites, aptitud = buscarConflictos(self.poblacion, self.numElites)
            print('Iteracion: {} | Conflictos: {}'.format(i + 1, aptitud))
            if aptitud == 0:
                horarioOptimo = self.poblacion[indiceElites[0]]
                break

            # Se establecen los individuos de elite dentro de la poblacion.
            nuevaPoblacion = [self.poblacion[index] for index in indiceElites]

            # Cruzar entre elites, o mutar una elite.
            while len(nuevaPoblacion) < self.poblaMax:
                if np.random.rand() < self.probMut:
                    # Mutacion.
                    nuevoIndividuo = self.mutar(nuevaPoblacion, rangoAula)
                else:
                    # Cruza.
                    nuevoIndividuo = self.cruzar(nuevaPoblacion)
                nuevaPoblacion.append(nuevoIndividuo)
            self.poblacion = nuevaPoblacion  # Podar todos los menos aptos, remplazando toda la poblacion por una nueva.
        return horarioOptimo
