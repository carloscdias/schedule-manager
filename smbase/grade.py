# coding: utf-8

from .disciplina import Disciplina

class Grade:
    """
        Classe que armazena os horários de cada disciplina em uma "matriz".
        Cada posição contém uma disciplina e pode ser acessada pelo dia e horário.
        Exemplo: ("seg", "m2") = "Calculo"
    """

    def __init__(self, disciplinas = None):
        """Construtor
            Inicializa a grade de horários com uma lista de disciplinas

            Args:
                disciplinas (opcional): Lista de disciplinas para montar a grade
        """
        self._grid = {}

        for dia in [ 'seg', 'ter', 'qua', 'qui', 'sex', 'sab' ]:
            for char_horario in 'mtn':
                for numero_horario in range( 1, 7 ):
                    self._grid[( dia, char_horario + str( numero_horario ) )] = ''

        if disciplinas:
            for d in disciplinas:
                self.add_disciplina(d)

    def add_disciplina(self, disciplina):
        """Adiciona uma disciplina na grade
            Percorre a lista de horários da disciplina atribuindo-a ao respetivo tempo

            Args:
                disciplina: uma disciplina
        """
        for (dia, hr) in disciplina._horarios:
            self._grid[(dia, hr)] = disciplina
