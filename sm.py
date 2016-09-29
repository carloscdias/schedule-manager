#!/usr/bin/python3

from argparse import ArgumentParser

# Programa para montar a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido

def main():
	parser = ArgumentParser( description = "Monta a grade de horarios de disciplinas para um aluno da UERJ atraves de sua matricula de acordo com o metodo de alocacao escolhido" )
	
	parser.add_argument( 'matricula', help = "Matricula do aluno" )

	args = parser.parse_args()

	print( 'Matricula digitada:', args.matricula )

# End main

if __name__ == '__main__':
	main()