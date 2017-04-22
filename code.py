#!/usr/bin/pythonw
# -*-coding:Utf-8 -*
# Test de la fonction input
ano = input("Escriba su año de nacimiento : ") #dialogue utilisateur

ano = int(ano) #transforme la variable en int

#Ma proposition initiale

if ano%4==0 and not ano%100==0:
	print ("El ano seleccionado es un ano bisesto, usted es una persona especial")
elif ano%400==0:
	print ("El ano seleccionado es un ano bisiesto, usted es una persona especial")
else:
	print ("El ano seleccionado NO es un ano bisiesto, usted es una persona ordinaria")


	