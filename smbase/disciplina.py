# coding: utf-8

class Disciplina:
    """Classe que armazena as informações referente a uma disciplina.

        Armazena os dados que serão inseridos nas posições da grade
    """

    def __init__(self, nome, codigo, turma, horarios, creditos, professor, preferencial, tipo, pode_cursar, trava_credito):
        """Construtor

        Args:
            nome: Nome da disciplina
            codigo: Código da disciplina
            turma: Turma
            horarios: Lista de tuplas com os horarios armazenados em pares (dia, tempo). Exemplo: ("seg", "m1")
            creditos: Quantidade de créditos da disciplina
            professor: Nome do professor que lecionará a disciplina
            preferencial: Bool que indica se a disciplina é preferencial para o aluno
            tipo: Obrigatória, eletiva definida ou eletiva restrita
            pode_cursar: Bool que indica se o aluno pode cursar a disciplina, ou seja, não há pré-requisitos pendentes
            trava_credito: credito minimo necessario para cusar a disciplina
        """
        self._nome = nome
        self._codigo = codigo
        self._turma = turma
        self._horarios = horarios
        self._creditos = creditos
        self._professor = professor
        self._preferencial = preferencial
        self._tipo = tipo
        self._pode_cursar = pode_cursar
        self._trava_credito = trava_credito

    def __str__(self):
        _str = "{} - {}\nHorários: {}".format(self._nome, self._codigo, self._horarios)
        return _str
