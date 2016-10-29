#!/usr/bin/python3

from argparse import ArgumentParser
from smbase.aluno import Aluno

# completo	- prioriza o maior numero de disciplinas que podem ser alocadas
def metodo_completo():
	print( 'Executando o metodo de alocacao completo...' )

# continuo	- prioriza o maior numero de disciplinas que podem ser alocadas sem que haja tempos livres na grade
def metodo_continuo():
	print( 'Executando o metodo de alocacao continuo...' )

# credito	- prioriza alocar as disciplinas que possuem o maior numero de creditos
def metodo_credito():
	print( 'Executando o metodo de alocacao credito...' )

# Programa para montar a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido
def main():
	# Dicionario de mapeamento dos metodos de alocacao disponiveis
	metodos = {
		'completo': metodo_completo,
		'continuo': metodo_continuo,
		'credito' : metodo_credito
	}

	# Nomes dos metodos
	opcoes_metodos = list( metodos.keys() )

	# Parser de argumentos de linha de comando
	parser = ArgumentParser( description = "Monta a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido" )
	
	parser.add_argument( 'matricula', help = "Matricula do aluno" )
	parser.add_argument( '-m', '--metodo', default = opcoes_metodos[0], choices = opcoes_metodos, help = "Metodo de alocacao de disciplinas" )
	parser.add_argument('-o','--obrigatorio',type = string ,help = "Adicionar uma materia obrigatoriamente na grade")

	args = parser.parse_args()
	
	print( 'Matricula:', args.matricula )
	print( 'Modo de alocacao de disciplinas:', args.metodo )
	print( Aluno( args.matricula ) )

	# Executando funcao de alocacao
	metodos[ args.metodo ]()

# End main

if __name__ == '__main__':
	main()
