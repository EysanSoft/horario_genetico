import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import prettytable
from horario import Horario
from optimizadorGenetico import OptimizadorGenetico


def mostrarHorario(horario):
    col_labels = ['Dia/Cupo', '1', '2', '3', '4', '5']
    table_vals = [[i + 1, '', '', '', '', ''] for i in range(5)]
    table = prettytable.PrettyTable(col_labels, hrules=prettytable.ALL)
    for h in horario:
        diaSemanal = h.diaSemanal
        cupo = h.cupo
        texto = 'Grupo: {} \n Clase: {} \n Aula: {} \n Docente: {}'.format(h.cursoID, h.grupoID, h.numAula, h.matriculaDocente)
        table_vals[diaSemanal - 1][cupo] = texto
    for row in table_vals:
        table.add_row(row)
    # lines = table.get_string()
    print(table)
    escribirHorario(table)
    """
    pdf = FPDF("P", "mm", "A4")
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    j = 10
    for line in lines.split('\n'):
        pdf.cell(20, 8, line, ln=j)
        j += 20
    pdf.output("Ejemplo1.pdf")
    """


def escribirHorario(horario):
    with open('horario', 'w') as w:
        w.write(str(horario))


class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("vistaHorarioGeneticoV2.ui", self)
        self.botonMate.clicked.connect(self.genMate)
        self.botonHis.clicked.connect(self.genHis)
        self.botonInfo.clicked.connect(self.genInfo)

    def genMate(self):
        # Llenar el horario, segun las clases, es decir, los cupos segun la clase.
        listaDeCupos = []
        idClase = 1201

        listaDeCupos.append(Horario(201, 1201, 11101))
        listaDeCupos.append(Horario(201, 1201, 11101))
        listaDeCupos.append(Horario(202, 1201, 11102))
        listaDeCupos.append(Horario(202, 1201, 11102))
        listaDeCupos.append(Horario(203, 1201, 11103))
        listaDeCupos.append(Horario(203, 1201, 11103))
        listaDeCupos.append(Horario(206, 1201, 11106))
        listaDeCupos.append(Horario(206, 1201, 11106))

        listaDeCupos.append(Horario(202, 1202, 11102))
        listaDeCupos.append(Horario(202, 1202, 11102))
        listaDeCupos.append(Horario(204, 1202, 11104))
        listaDeCupos.append(Horario(204, 1202, 11104))
        listaDeCupos.append(Horario(206, 1202, 11106))
        listaDeCupos.append(Horario(206, 1202, 11106))

        listaDeCupos.append(Horario(203, 1203, 11103))
        listaDeCupos.append(Horario(203, 1203, 11103))
        listaDeCupos.append(Horario(204, 1203, 11104))
        listaDeCupos.append(Horario(204, 1203, 11104))
        listaDeCupos.append(Horario(205, 1203, 11105))
        listaDeCupos.append(Horario(205, 1203, 11105))
        listaDeCupos.append(Horario(206, 1203, 11106))
        listaDeCupos.append(Horario(206, 1203, 11106))

        # Optimizacion
        OG = OptimizadorGenetico(poblaMax=50, numElites=10, iterMaxCon=600)  # Se asignan los valores...
        horarioOptimo = OG.bucleFitness(listaDeCupos, 3)

        # Visualizacion
        tuplas = []
        for individuos in horarioOptimo:
            if individuos.grupoID == (int(idClase)):
                tuplas.append(individuos)
        mostrarHorario(tuplas)

    def genHis(self):
        # Llenar el horario, segun las clases, es decir, los cupos segun la clase.
        listaDeCupos = []
        idClase = 1202

        listaDeCupos.append(Horario(201, 1201, 11101))
        listaDeCupos.append(Horario(201, 1201, 11101))
        listaDeCupos.append(Horario(202, 1201, 11102))
        listaDeCupos.append(Horario(202, 1201, 11102))
        listaDeCupos.append(Horario(203, 1201, 11103))
        listaDeCupos.append(Horario(203, 1201, 11103))
        listaDeCupos.append(Horario(206, 1201, 11106))
        listaDeCupos.append(Horario(206, 1201, 11106))

        listaDeCupos.append(Horario(202, 1202, 11102))
        listaDeCupos.append(Horario(202, 1202, 11102))
        listaDeCupos.append(Horario(204, 1202, 11104))
        listaDeCupos.append(Horario(204, 1202, 11104))
        listaDeCupos.append(Horario(206, 1202, 11106))
        listaDeCupos.append(Horario(206, 1202, 11106))

        listaDeCupos.append(Horario(203, 1203, 11103))
        listaDeCupos.append(Horario(203, 1203, 11103))
        listaDeCupos.append(Horario(204, 1203, 11104))
        listaDeCupos.append(Horario(204, 1203, 11104))
        listaDeCupos.append(Horario(205, 1203, 11105))
        listaDeCupos.append(Horario(205, 1203, 11105))
        listaDeCupos.append(Horario(206, 1203, 11106))
        listaDeCupos.append(Horario(206, 1203, 11106))

        # Optimizacion
        OG = OptimizadorGenetico(poblaMax=50, numElites=10, iterMaxCon=800)  # Se asignan los valores...
        horarioOptimo = OG.bucleFitness(listaDeCupos, 3)

        # Visualizacion
        tuplas = []
        for individuos in horarioOptimo:
            if individuos.grupoID == (int(idClase)):
                tuplas.append(individuos)
        mostrarHorario(tuplas)

    def genInfo(self):
        # Llenar el horario, segun las clases, es decir, los cupos segun la clase.
        listaDeCupos = []
        idClase = 1203

        listaDeCupos.append(Horario(201, 1201, 11101))
        listaDeCupos.append(Horario(201, 1201, 11101))
        listaDeCupos.append(Horario(202, 1201, 11102))
        listaDeCupos.append(Horario(202, 1201, 11102))
        listaDeCupos.append(Horario(203, 1201, 11103))
        listaDeCupos.append(Horario(203, 1201, 11103))
        listaDeCupos.append(Horario(206, 1201, 11106))
        listaDeCupos.append(Horario(206, 1201, 11106))

        listaDeCupos.append(Horario(202, 1202, 11102))
        listaDeCupos.append(Horario(202, 1202, 11102))
        listaDeCupos.append(Horario(204, 1202, 11104))
        listaDeCupos.append(Horario(204, 1202, 11104))
        listaDeCupos.append(Horario(206, 1202, 11106))
        listaDeCupos.append(Horario(206, 1202, 11106))

        listaDeCupos.append(Horario(203, 1203, 11103))
        listaDeCupos.append(Horario(203, 1203, 11103))
        listaDeCupos.append(Horario(204, 1203, 11104))
        listaDeCupos.append(Horario(204, 1203, 11104))
        listaDeCupos.append(Horario(205, 1203, 11105))
        listaDeCupos.append(Horario(205, 1203, 11105))
        listaDeCupos.append(Horario(206, 1203, 11106))
        listaDeCupos.append(Horario(206, 1203, 11106))

        # Optimizacion
        OG = OptimizadorGenetico(poblaMax=50, numElites=10, iterMaxCon=1000)  # Se asignan los valores...
        horarioOptimo = OG.bucleFitness(listaDeCupos, 3)

        # Visualizacion
        tuplas = []
        for individuos in horarioOptimo:
            if individuos.grupoID == (int(idClase)):
                tuplas.append(individuos)
        mostrarHorario(tuplas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())
