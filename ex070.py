""" Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continua
No final mostre:
A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de RS1000 reais
C - Qual é  onome do produto mais barato """
print('==' * 20)
print('        LOJA DOS GAFANHOTOS')
print('==' * 20)
total = totmil = menor = cont = 0
barato = ' '
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço R$'))
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('---------------- FIM DO PROGRAMA ----------------')
print('O total da compra foi R${:.2f}'.format(total))
print('Temos {} produtos custando mais de R$1000.00'.format(totmil))
print('O produto mais barato foi {} que custa R${}'.format(barato, menor))
