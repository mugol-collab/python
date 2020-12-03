#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#             Até 5 Kg             Acima de 5 Kg
# Morango     R$ 3,50 por Kg       R$ 3,20 por Kg
# Maçã        R$ 2,80 por Kg       R$ 2,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da 
# compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% 
# sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o 
# valor a ser pago pelo cliente.

print("===================================")
print("\tFruteria")
print("===================================")

pesoMorango = float(input("Morango (Kg): "))
pesoMaca = float(input("Maca (Kg)   : "))
pesoTotal = pesoMorango + pesoMaca

precoMor = 0.0
precoMaca = 0.0
precoTotal = 0.0

PrecoFinal = 0.0

if (pesoMorango <= 5):
    precoMor = pesoMorango * 3.50
else:
    precoMor = pesoMorango * 3.20

if (pesoMaca <= 5):
    precoMaca = pesoMaca * 2.80
else:
    precoMaca = pesoMaca * 2.50

precoTotal = precoMor + precoMaca

if (pesoTotal > 8 or precoTotal > 25):
    precoFinal = precoTotal - (precoTotal * 0.1)
else:
    precoFinal = precoTotal

print("Valor a ser pago: %1.2f" % (precoFinal))