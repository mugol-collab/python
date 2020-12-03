#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 1. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual 
# operação ele deseja realizar. O resultado da operação deve ser acompanhado 
# de uma frase que diga se o número é:

# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

print('===================================================')
print('\tOperaciones definidas pelo usuario')
print('===================================================')

print('Ingrese 2 numeros')

num1 = input("Numero 1: ")
#print(type(num1))
num2 = input("Numero 2: ")
#print(type(num2))

print('\nOperações disponíveis')
print('''a. par o impar\nb. positivo ou negativoa
c. inteiro ou decimal''')

op = input('\nOperação a realizar: ')
print('tipo op: ', type(op))

if (op == "a" or op == 'A'):
    if '.' in num1:
        if (float(num1) % 2 == 0):
            print('%1.2f é par' % (float(num1)))
        else:
            print('%1.2f é impar' % (float(num1)))
    
    else:
        if (int(num1) % 2 == 0):
            print('%d é par' % (int(num1)))
        else:
            print('%d é impar' % (int(num1)))

    if '.' in num2:
        if (float(num2) % 2 == 0):
            print('%1.2f é par' % (float(num2)))
        else:
            print('%1.2f é impar' % (float(num2)))
    else:
        if (int(num2) % 2 == 0):
            print('%d é par' % (int(num2)))
        else:
            print('%d é impar' % (int(num2)))
    
elif (op == 'b' or op == 'B'):
    if '.' in num1:
        if (float(num1) > 0):
            print('%1.2f é positivo' % (float(num1)))
        else:
            print('%1.2f é negativo' % (float(num1)))
    
    else:
        if (int(num1) > 0):
            print('%d é positivo' % (int(num1)))
        else:
            print('%d é negativo' % (int(num1)))

    if '.' in num2:
        if (float(num2) > 0):
            print('%1.2f é positivo' % (float(num2)))
        else:
            print('%1.2f é negativo' % (float(num2)))
    else:
        if (int(num2) > 0):
            print('%d é positivo' % (int(num2)))
        else:
            print('%d é negativo' % (int(num2)))

elif (op == 'c' or op == 'C'):
    if '.' in num1:
        print('%1.2f é float' % (float(num1)))
    else:
        print('%d é int' % (int(num1)))

    if '.' in num2:
        print('%1.2f é float' % (float(num2)))
    else:
        print('%d é int' % (int(num2)))


    

