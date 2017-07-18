#!/usr/bin/python3

from argparse import ArgumentParser
from smbase.aluno import Aluno
from smbase.grade import Grade
import scraperdisciplina

# completo	- prioriza o maior numero de disciplinas que podem ser alocadas
def metodo_completo(matricula):
	print( 'Executando o metodo de alocacao completo...' )

# continuo	- prioriza o maior numero de disciplinas que podem ser alocadas sem que haja tempos livres na grade
def metodo_continuo(matricula):
	print( 'Executando o metodo de alocacao continuo...' )

# credito	- prioriza alocar as disciplinas que possuem o maior numero de creditos
def metodo_credito(matricula):
	print( 'Executando o metodo de alocacao credito...' )

def metodo_aleatorio(matricula, exclusas):
	print( 'Executando o metodo de alocacao aleatorio...' )
	disciplinas = scraperdisciplina.extrai_disciplinas(matricula, exclusas)

	grade = Grade(disciplinas, 'aleatorio')
	print(grade)
	grade.exportar_para_arquivo('grade-aleatoria')

# Programa para montar a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido
def main():
	# Dicionario de mapeamento dos metodos de alocacao disponiveis
	metodos = {
		'completo': metodo_completo,
		'continuo': metodo_continuo,
		'credito' : metodo_credito,
		'aleatorio': metodo_aleatorio
	}

	# Nomes dos metodos
	opcoes_metodos = list( metodos.keys() )

	# Parser de argumentos de linha de comando
	parser = ArgumentParser( description = "Monta a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido" )

	parser.add_argument( 'matricula', help = "Matricula do aluno" )
	parser.add_argument( '-m', '--metodo', default = opcoes_metodos[0], choices = opcoes_metodos, help = "Metodo de alocacao de disciplinas" )
	parser.add_argument( '-o','--obrigatorio', help = "Adicionar uma materia obrigatoriamente na grade")
	parser.add_argument( '-e', '--exclui', help = "Exclui materias das opcoes")

	args = parser.parse_args()

	print( 'Matricula:', args.matricula )
	print( 'Modo de alocacao de disciplinas:', args.metodo )
	print( Aluno( args.matricula ) )

	# Executando funcao de alocacao
	metodos[ args.metodo ](args.matricula, args.exclui.split(','))

# End main

if __name__ == '__main__':
	main()
