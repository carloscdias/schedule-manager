#!/usr/bin/python3

from argparse import ArgumentParser

# Programa para montar a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido

def main():
	parser = ArgumentParser( description = "Monta a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido" )
	
	parser.add_argument( 'matricula', help = "Matricula do aluno" )
	parser.add_argument( '-m', '--metodo', default = 'completo', choices = [ 'completo', 'continuo', 'credito' ], help = "Metodo de alocacao de disciplinas" )

	args = parser.parse_args()

	# completo	- prioriza o maior numero de disciplinas que podem ser alocadas
	# continuo	- prioriza o maior numero de disciplinas que podem ser alocadas sem que haja tempos livres na grade
	# credito	- prioriza alocar as disciplinas que possuem o maior numero de creditos

	print( 'Matricula:', args.matricula )
	print( 'Modo de alocacao de disciplinas:', args.modo )

# End main

if __name__ == '__main__':
	main()