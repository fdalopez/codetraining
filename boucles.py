#!/usr/bin/pythonw
# -*-coding:Utf-8 -*
var= input ("escriba un numero :")

# On garde la variable contenant le nombre dont on veut la table de multiplication
i = 0 # C'est notre variable compteur que nous allons incrémenter dans la boucle

while i < 10: # Tant que i est strictement inférieure à 10
    print i + 1, "*", var, "=", (i + 1) * var
    i += 1 # On incrémente i de 1 à chaque tour de boucle


