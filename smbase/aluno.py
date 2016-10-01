# coding: utf-8

from .grade import Grade

class Aluno:
    """
        Classe que armazena as grades de um respectivo aluno identificado por sua matrícula.
    """
    def __init__(self, matricula):
        """ Construtor

            Args:
                matricula: Matrícula do aluno
        """
        self._matricula = matricula
        self._grades = []
