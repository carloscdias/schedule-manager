# coding: utf-8

from .disciplina import Disciplina

class Grade:
    """
        Classe que armazena os horários de cada disciplina em uma "matriz".
        Cada posição contém uma disciplina e pode ser acessada pelo dia e horário.
        Exemplo: ("seg", "m2") = "Calculo"
    """

    def __init__(self, disciplinas = None, metodo = None):
        """Construtor
            Inicializa a grade de horários com uma lista de disciplinas

            Args:
                disciplinas (opcional): Lista de disciplinas para montar a grade
        """
        self._grid = {}

        for dia in [ 'SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB' ]:
            for char_horario in 'MTN':
                for numero_horario in range( 1, 7 ):
                    self._grid[( dia, char_horario + str( numero_horario ) )] = ''

        if disciplinas:
            if metodo == 'aleatorio':
                self.monta_grade_metodo_aleatorio(disciplinas)
            elif metodo == 'completo':
                self.monta_grade_metodo_completo(disciplinas)
            elif metodo == 'credito':
                self.monta_grade_metodo_credito(disciplinas)
            elif metodo == 'continuo':
                self.monta_grade_metodo_continuo(disciplinas)

    def monta_grade_metodo_completo(self, disciplinas):
        pass

    def monta_grade_metodo_continuo(self, disciplinas):
        pass

    def monta_grade_metodo_credito(self, disciplinas):
        pass

    def monta_grade_metodo_aleatorio(self, disciplinas):
        for d in disciplinas:
            if self.pode_incluir(d):
                self.add_disciplina(d)

    def pode_incluir(self, disciplina):
        for dia in disciplina._horarios:
            for hr in disciplina._horarios[dia]:
                if self._grid[(dia, hr)] != "":
                    return False
        return True

    def add_disciplina(self, disciplina):
        """Adiciona uma disciplina na grade
            Percorre a lista de horários da disciplina atribuindo-a ao respetivo tempo

            Args:
                disciplina: uma disciplina
        """
        for dia in disciplina._horarios:
            for hr in disciplina._horarios[dia]:
                self._grid[(dia, hr)] = disciplina
