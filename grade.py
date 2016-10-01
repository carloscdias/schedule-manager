# coding: utf-8

import disciplina

class Grade:
    """
        Classe que armazena os horários de cada disciplina em uma "matriz".
        Cada posição contém uma disciplina e pode ser acessada pelo dia e horário.
        Exemplo: ("seg", "m2") = "Calculo"
    """

    def __init__(self, disciplinas):
        """Construtor
            Inicializa a grade de horários com uma lista de disciplinas

            Args:
                disciplinas: Lista de disciplinas para montar a grade
        """
        self._grid = {}
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
