# -*- coding: utf-8 -*-
# 2. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da 
# pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve 
# ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
# "Assassino". Caso contrário, ele será classificado como "Inocente".

print("===========================================")
print("\tInvestigação Crime")
print("===========================================")
print("Responda sim ou não as seguintes perguntas:")

contSim = 0
contNao = 0

print("contSim: %d" % (contSim))
print("contNão: %d" % (contNao))

resp = input("a. Telefonou para a víctima? ")

if (resp == 'sim' or resp == 'Sim' or resp  == 'SIM'):
    contSim += 1
elif (resp == 'não' or resp == 'nao' or resp == 'Nao' or resp == 'NAO'):
    contNao += 1
else:
    print("Resposta não válida")

resp = input("b. Esteve no local do crime? ")

if (resp == 'sim' or resp == 'Sim' or resp  == 'SIM'):
    contSim += 1
elif (resp == 'não' or resp == 'nao' or resp == 'Nao' or resp == 'NAO'):
    contNao += 1
else:
    print("Resposta não válida")

resp = input("c. Mora perto da vítima? ")

if (resp == 'sim' or resp == 'Sim' or resp  == 'SIM'):
    contSim += 1
elif (resp == 'não' or resp == 'nao' or resp == 'Nao' or resp == 'NAO'):
    contNao += 1
else:
    print("Resposta não válida")

resp = input("d. Devia para a vítima? ")

if (resp == 'sim' or resp == 'Sim' or resp  == 'SIM'):
    contSim += 1
elif (resp == 'não' or resp == 'nao' or resp == 'Nao' or resp == 'NAO'):
    contNao += 1
else:
    print("Resposta não válida")

resp = input("e. Já trabalhou com a vítima? ")

if (resp == 'sim' or resp == 'Sim' or resp  == 'SIM'):
    contSim += 1
elif (resp == 'não' or resp == 'nao' or resp == 'Nao' or resp == 'NAO'):
    contNao += 1
else:
    print("Resposta não válida")

clasificacao = ''

if (contSim == 2):
    clasificacao = 'Suspeita'
elif (contSim > 2 and contSim < 5):
    clasificacao = 'Cúmplice'
elif (contSim == 5):
    clasificacao = 'Assassino'
else:
    clasificacao = 'Inocente'

print("contSim: %d" % (contSim))
print("contNão: %d" % (contNao))

print("A pessoa é %s" % (clasificacao))