#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 5. O Hipermercado Guanabara está com uma promoção de 
# carnes que é imperdível. Confira:

#                   Até 5 Kg             Acima de 5Kg
#   Filé Bobino     R$ 10.90 por Kg      R$ 9.80 por Kg
#   Alcatra         R$ 15.90 por Kg      R$ 13.80 por Kg
#   Picanha         R$ 20.90 por Kg      R$ 17.80 por Kg

# Para atender a todos os clientes, cada cliente poderá 
# levar apenas um dos tipos de carne de promoção, porém 
# não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá
# ainda um desconto de 5% sobre o total da compra. Escreva 
# um  programa  que peça  o tipo e a quantidade de carne 
# comprada pelo usuário e gere um cupom fiscal, contendo 
# as  informações  da compra: tipo e quantidade de carne, 
# preço  total,  tipo de  pagamento,  valor do desconto e 
# valor a pagar.

print ("===================================")
print("\tHipermercado Guanabara")
print ("===================================")
print("Promocao de carne: ")
print("a. File Bobino")
print("b. Alcatra")
print("c. Picanha")

tipoCarne = input("Tipo de carne: ")
cantidad = float(input("cantidad (Kg): "))
cartao = input("Cartao Tabajara: ")
tipo = ''
preco = 0.0
precoTotal = 0.0
tipoPagamento = '' 
desconto = 0.0

if (tipoCarne == 'a'):
    tipo = "File Bobino"
    if (cantidad <= 5):
        preco = cantidad * 10.90
    else: 
        preco = cantidad * 9.80

if (tipoCarne == 'b'):
    tipo = "Alcatra"
    if (cantidad <= 5):
        preco = cantidad * 15.90
    else: 
        preco = cantidad * 13.80

if (tipoCarne == 'c'):
    tipo = "Picanha"
    if (cantidad <= 5):
        preco = cantidad * 20.90
    else: 
        preco = cantidad * 17.80

if (cartao == 'sim' or cartao == 's'):
    desconto = preco * 0.05
    precoTotal = preco - desconto
    tipoPagamento = "cartao Trabajara"
else: 
    desconto = 0.0
    precoTotal = preco
    tipoPagamento = "dinheiro"

print ("===================================")
print("Tipo de carne : %s" % (tipo))
print("Cantidad (Kg) : %0.2f" % (cantidad))
print("Preco Total   : %0.2f" % (preco))
print("Tipo de pagamento: %s" % (tipoPagamento))
print("Valor de desconto: %0.2f" % (desconto))
print("Valor a pagar: %0.2f" % (precoTotal))
print ("===================================")