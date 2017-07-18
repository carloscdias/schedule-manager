# coding: utf-8
import re

from bs4 import BeautifulSoup
from urllib.request import urlopen
from smbase.disciplina import Disciplina


"""
TODO:
. Fazer regex aceitar caracteres acentuados
. Tratar caso em que ha mais de uma turma oferecida para uma disciplina
. Tratar erros
. Mover esse arquivo para a pasta smdataextration e permitir a importacao de Disciplina
. Remover strips() desnecessarios
. Implementar extrai_podecursar e extrai_tipo

Paginas no sistema na qual os dados estao localizados:
. nome, -> RequisitosACursar
. codigo, -> RequisitosACursar
. turma,-> HorariosTurmasDisciplina
. horarios -> HorariosTurmasDisciplina
. creditos, -> DadosDisciplina
. professor, -> HorariosTurmasDisciplina
. preferencial, -> HorariosTurmasDisciplina
. tipo, -> RequisitosACursar
. pode_cursar -> RequisitosACursar e DadosDisciplina
"""

def extrai_disciplinas(matricula, exclusas):
	"""
		Função que retorna todos as disciplinas disponiveis na pagina RequisitosACursar de um aluno.
	"""
	url = "https://www.alunoonline.uerj.br/requisicaoaluno/requisicao.php?requisicao=RequisitosACursar&matricula={0}".format(matricula)
	pattern = re.compile(r'(\w+)-(\w+)\s+([\w\s]+)', re.I) # depto, codigo, nome
	content = urlopen(url).read()

	soap = BeautifulSoup(content, 'html.parser')

	disciplinas = []
	# extrai todas as disciplinas nao cursadas
	for elem in soap.find_all('a'):
		#print(elem.get_text())
		match = pattern.search(elem.get_text())
		if match:
			nome = match.group(3).strip()
			codigo = match.group(2).strip()
			#codigo = codigo.lstrip('0') # remove zeros a esquerda
			turma = extrai_turma(codigo)
			horarios = extrai_horarios(codigo)
			creditos = extrai_creditos(codigo)
			docentes = extrai_docentes(codigo)
			preferencial = extrai_preferencial(codigo, matricula)
			tipo = ""
			pode_cursar = ""
			trava_credito = ""
			# adiciona a nova disciplina a lista de disciplinas que ainda devem ser cursadas
			if (nome not in exclusas):
				disciplinas.append( Disciplina(nome, codigo, turma, horarios, creditos, docentes, preferencial, tipo, pode_cursar, trava_credito) )

	return disciplinas

def extrai_podecursar(codigo):
	pass

def extrai_tipo(codigo):
	pass

def extrai_preferencial(codigo, matricula):
	pattern = re.compile(r'Preferencial:<\/b> (\w+)')

	url = "http://www.alunoonline.uerj.br/requisicaoaluno/requisicao.php?requisicao=HorariosTurmasDisciplina&disciplinas[0]={0}&matricula={1}".format(codigo, matricula)
	content = urlopen(url).read()

	match = pattern.search(str(content))
	preferencial = ""
	if match:
		preferencial = match.group(1).strip()
		#print(match.group(1))
	return preferencial

def extrai_docentes(codigo):
	#TODO: corrigir para aceitar nomes com acentuacao
	pattern = re.compile(r"Docente:\s+<\/b>\s+<\/div>..\s+<div\s+style=..width:80%;text-align:left;float:left;..>([(\w+\s+)+(<br>)*]+)", re.M|re.I|re.DOTALL)

	url = "http://www.alunoonline.uerj.br/requisicaoaluno/requisicao.php?requisicao=HorariosTurmasDisciplina&disciplinas[0]={0}".format(codigo)
	content = urlopen(url).read()

	match = pattern.search(str(content))
	docentes = []
	if match:
		#print(match.group(1).split('<br>'))
		docentes = match.group(1).split('<br>') # separa os docentes em uma lista
		docentes[-1] = docentes[-1].rstrip('< ') # remove '<' indesejado na ultima posicao
		docentes = [ d.strip() for d in docentes ] # remove espacos indesejados
		#print(docentes)

	return docentes

def extrai_creditos(codigo):
	pattern = re.compile(r'ditos:\s+(\d+)') # Número de créditos: (valor)

	url = "http://www.alunoonline.uerj.br/requisicaoaluno/requisicao.php?requisicao=DadosDisciplina&disciplinas[0]={0}".format(codigo)
	content = urlopen(url).read()
	#print(str(content))
	match = pattern.search(str(content))
	creditos = ""
	if match:
		#print(match.group(1))
		creditos = match.group(1).strip()
	#TODO: tratar erros
	return creditos

def extrai_turma(codigo):
	pattern = re.compile(r'TURMA:\s+<\/b>\s+(\d+)') # TURMA: </b> (valor)

	url = "http://www.alunoonline.uerj.br/requisicaoaluno/requisicao.php?requisicao=HorariosTurmasDisciplina&disciplinas[0]={0}".format(codigo)
	content = urlopen(url).read()
	#print(str(content))
	match = pattern.search(str(content))
	turma = ""
	if match:
		#print(match.group(1))
		turma = match.group(1).strip()
	#TODO: tratar erros
	return turma

def extrai_horarios(codigo):
	pattern = re.compile(r'SEG|TER|QUA|QUI|SEX|SAB|[MTN]\d') # pega dias e horarios no formato M, T ou N seguido de um digito

	url = "http://www.alunoonline.uerj.br/requisicaoaluno/requisicao.php?requisicao=HorariosTurmasDisciplina&disciplinas[0]={0}".format(codigo)
	content = urlopen(url).read()
	#print(str(content))

	match = pattern.findall(str(content), re.M)
	horarios = {}
	if match:
		# gerando tuplas (dia, horario)
		dia = None
		for elem in match:
			if elem in ("SEG", "TER", "QUA", "QUI", "SEX", "SAB"):
				dia = elem
			elif dia: # nao eh dia -> adiciona o horario
				if dia in horarios: # dia ja foi inicializado no dict
					horarios[dia].append(elem)
				else: # senao, inicializa a chave dia
					horarios[dia] = [elem]
		#for dia, hr in horarios.items():
		#	print(dia, hr)

	return horarios
