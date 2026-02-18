""" 1- Par ou ímpar
Peça um número ao usuário e diga se ele é par ou ímpar.
Conceitos: input, int, if, operador %
Regras:
Se o número for 0, mostre: "Zero é neutro" """

# numero = int(input('Insira um número: '))
# if numero == 0:
#   print('zero é neutro')
# elif numero %2 == 0:
#   print('numero par')
# else:
#   print('numero impar')

""" 2- Contador inteligente
Mostre na tela os números de 1 até N, onde N é digitado pelo usuário.
Extras: Se o usuário digitar um número menor que 1, mostre erro e pare o programa. """

# numero = int(input('digite um numero'))

# if numero< 1:
#   print('erro')
# else:
#   for i in range(1,numero+1):
#     print(i)

"""3- abuada flexível
Peça um número e mostre a tabuada dele de 1 a 10.
Formato:
7 x 1 = 7
7 x 2 = 14
.. """

# numero = int(input('insira um numero: '))
# for i in range(11):
#   resultado = i * numero 
#   print(f'{numero}x{i}={resultado}')

""" 4) Lista de compras
Peça ao usuário para digitar 5 produtos e armazene numa lista.
Depois:
Mostre todos os produtos numerados
Mostre o primeiro e o último da lista """

# entrada = input("Digite os itens separados por vírgula: ")
# lista = [item.strip() for item in entrada.split(',')]
# print(lista)
# for i in range(len(lista)):
#   print(f'{i + 1} - {lista[i]}')
# print('Último item: ', lista[0])
# print('Último item: ', lista[-1])

""" Estatísticas simples
O usuário digita vários números separados por vírgula.
Exemplo:
10,5,8,20,1
Seu programa deve mostrar:
Quantidade de números
Maior
Menor
Soma
Média """
# try:
#   entrada = input("Digite os itens separados por vírgula: ")
#   lista = [item.strip() for item in entrada.split(',')]
#   numeros = [int(item) for item in lista]
#   print(f'A lista possui {len(numeros)} números')
#   print(f'O maior número da lista é {max(numeros)}')
#   print(f'O menor número da lista é {min(numeros)}')
#   print(f'A soma da lista é {sum(numeros)}')
#   print(f'A média da lista é {sum(numeros) / len(numeros)}')
# except ValueError:
#   print('Erro: insira um numero válido')

""" Filtro de números
Dada esta lista:
numeros = [2, 5, 8, 11, 14, 17, 20]
Crie duas novas listas:
Uma só com pares
Outra só com ímpares """


# numeros = [2, 5, 8, 11, 14, 17, 20, 22, 23]
# pares = [i for i in numeros if i %2 == 0]
# impares = [i for i in numeros if i %2 != 0]
# print("Pares: ", pares)
# print("Ímpares: ", impares)    


""" Sistema de notas
Peça o nome e 3 notas de um aluno.
Guarde assim:
("Carlos", [7.5, 8.0, 6.0])
Depois:
Calcule a média
Se média >= 7 → "Aprovado"
Se média >= 5 → "Recuperação"
Senão → "Reprovado" """

# try:
#     nome = input("Digite o nome do aluno: ")

#     notas = []
#     for i in range(1, 4):
#         nota = float(input(f"Digite a nota {i}: "))
#         notas.append(nota)

#     aluno = (nome, notas)
#     media = sum(aluno[1]) / len(aluno[1])
 
#     print(f"\nAluno: {aluno[0]}")
#     print(f"Notas: {aluno[1]}")
#     print(f"Média: {media:.2f}")

#     if media >= 7:
#         print("Situação: Aprovado")
#     elif media >= 5:
#         print("Situação: Recuperação")
#     else:
#         print("Situação: Reprovado")

# except ValueError:
#     print("Erro: digite apenas números válidos para as notas")

""" Positivo, negativo ou zero
Peça um número ao usuário e diga se ele é:
positivo
negativo
zero """

# numero = int(input("Digite um numero: "))
# if numero > 0 :
#   print('Número positivo')
# elif numero == 0:
#   print('Número zero')
# else:
#   print('Número negativo')


""" Peça um número inteiro positivo e mostre a contagem regressiva até 0.
Exemplo:
Entrada: 5
Saída: 5 4 3 2 1 0 """
# try:
#   numero = int(input("Digite um numero inteiro positivo: "))
#   if numero < 0:
#     print("Erro: o número deve ser positivo!")
#   else:
#     for i in range(numero,-1,-1):
#       print(i)
# except ValueError:
#   print("Insira um número válido")

""" Soma até N
Peça um número N e calcule a soma de todos os números de 1 até N.
Exemplo:
Entrada: 5
Saída: 15 """

# try:
#   numero = int(input("Digite um numero inteiro positivo: "))
#   soma = 0
#   if numero < 0:
#     print("Erro: o número deve ser positivo!")
#   else:
#     for i in range(1, numero +1):
#       soma += i
#     print(soma)
# except ValueError:
#   print("Insira um número válido")

""" Dada uma lista [3, 7, 1, 9], calcule a soma sem usar sum().
Quando terminar, cole o código. """


""" lista = [3, 7, 1, 9]
soma = 0
for i in lista:
  soma = soma + i
print(soma) """


# lista = [30, 7, 1, 9, 10]
# maior = lista[0]
# for i in lista:
#   if maior < i :
#     maior = i
# print(maior)

""" Estatísticas básicas de uma lista
Dada uma lista fixa:
numeros = [4, 7, 2, 9, 5, 8, 1]
Seu programa deve calcular sem usar funções prontas (sum, max, min, len):
A soma total dos números
Quantos números existem
O maior valor
O menor valor
A média dos valores """

# numeros = [4, 7, 2, 9, 5, 8, -1, 2]
# soma = 0
# contador = 0
# maior_valor = numeros[0]
# menor_valor = numeros[0]
# for i in numeros:
#   soma += i
#   if maior_valor < i:
#     maior_valor = i
#   if menor_valor > i:
#     menor_valor = i
#   contador += 1

# print(f"Soma: {soma}")
# print(f"Menor Valor: {menor_valor}")
# print(f"Maior Valor: {maior_valor}")
# print(f"Quantidade de números: {contador}")
# print(f"A média dos valores da lista é: {soma/contador}")

""" Classificação de números
Dada a lista:
numeros = [2, 7, 10, 3, 8, 15, 6, 1, 4]
Seu programa deve percorrer a lista uma única vez e descobrir:
Quantos números são pares
Quantos são ímpares
Quantos são maiores que 5
Quantos são menores ou iguais a 5 """

# numeros = [2, 7, 10, 3, 8, 15, 6, 1, 4]
# impares = 0
# pares = 0
# qnt_maiores = 0
# qnt_menores = 0
# for i in numeros:
#     if i % 2 == 0:
#       pares += 1
#     else:
#       impares += 1
#     if i > 5 :
#       qnt_maiores += 1
#     else:
#        qnt_menores += 1
    

# print(f"A quantidade de pares é: {pares}")
# print(f"A quantidade de impares é: {impares}")
# print(f"Quantidade maior que 5 é: {qnt_maiores}")
# print(f"Quantidade menor ou igual 5 é: {qnt_menores}")


""" numeros = [12, -3, 7, -1, 0, 9, -15, 20]
Faça um programa que:
----------------------Conte quantos são positivos
----------------------Conte quantos são negativos
----------------------Conte quantos são zero
Calcule a soma apenas dos positivos
Calcule a soma apenas dos negativos
Regras:
Um único for
Vários contadores e acumuladores
Sem sum() pronta
Esse mistura classificação + soma condicional, que é um passo além do que você acabou de fazer. """

# numeros = [12, -3, 7, -1, 0, 9, -15, 20]
# zeros = 0
# positivos = 0
# negativos = 0
# soma_positivos = 0
# soma_negativos = 0
# for i in numeros:
#   if i == 0:
#     zeros += 1
#   if i > 0:
#     positivos += 1
#     soma_positivos += i
#   if i < 0:
#     negativos += 1
#     soma_negativos += i
# print(f"A quantidade de zeros é: {zeros}")
# print(f"A quantidade de positivos é: {positivos}")
# print(f"A quantidade de negativos é: {negativos}")
# print(f"A soma dos positivos é: {soma_positivos}")
# print(f"A soma dos negativos é: {soma_negativos}")



""" Agora vamos trabalhar com construção de lista a partir de regra.
Dada:
numeros = [5, 12, 3, 18, 7, 20, 1, 15]
Faça um programa que:
Crie uma nova lista contendo apenas os números múltiplos de 3
Crie outra lista contendo apenas os números maiores que 10
No final, mostre as duas listas
Regras:
Usar for
Usar append
Não usar list comprehension ainda """
# numeros = [5, 12, 3, 18, 7, 20, 1, 15]
# multiplos_3 = []
# maiores_10 = []
# for i in numeros:
#   if i % 3 == 0:
#     multiplos_3.append(i)
#   if i > 10:
#     maiores_10.append(i)
# print(f"A lista com os numeros multiplos de 3 é: {multiplos_3}")
# print(f"A lista com os numeros maiores que 10 é: {maiores_10}")

""" Dada a lista:
numeros = [2, 15, 7, 30, 22, 5, 18, 11, 3]
Crie três listas novas:
baixos → números menores que 10
medios → números entre 10 e 20 (inclusive)
altos → números maiores que 20
No final, mostre as três listas. """

# numeros = [2, 15, 7, 30, 22, 5, 18, 11, 3]
# baixos = []
# medios =[]
# altos = []
# for i in numeros:
#   if i < 10:
#     baixos.append(i)
#   elif i >= 10 and i <= 20:
#     medios.append(i)
#   else:
#     altos.append(i)
# print(f"Baixos: {baixos}")
# print(f"Médios: {medios}")
# print(f"Altos: {altos}")

""" Agora vamos misturar classificação + transformação.
Dada a lista:
numeros = [4, 9, 16, 25, 2, 7, 36]
Crie um programa que:
Crie uma lista chamada quadrados_perfeitos contendo apenas os números que são quadrados perfeitos
(4, 9, 16, 25, 36…)
Crie outra lista chamada outros com os números que não são quadrados perfeitos
Dica de raciocínio (sem fórmula pronta):
Um número é quadrado perfeito quando existe um número inteiro que multiplicado por ele mesmo dá exatamente aquele valor.
Exemplos:
4 → 2 × 2
9 → 3 × 3
16 → 4 × 4
Você vai precisar testar isso com lógica dentro do for. """

# numeros = [4, 9, 16, 25, 2, 7, 36]
# quadrado = []
# outros = []

# for i in numeros:
#   raiz = i ** 0.5
#   if raiz.is_integer() :
#     quadrado.append(i)
#   else :
#     outros.append(i)
# print(f"Lista de quadrados perfeitos: {quadrado}")
# print(f"Lita de outros: {outros}")

""" Agora vamos trabalhar com padrão em sequência.
Dada a lista:
numeros = [10, 20, 30, 40, 50]
Crie um programa que:
Gere uma nova lista onde cada número é a soma dele com o próximo elemento.
Exemplo esperado:
10 + 20 → 30
20 + 30 → 50
30 + 40 → 70
40 + 50 → 90
Resultado final:
[30, 50, 70, 90]
Dica importante:
Você vai precisar acessar:
o valor atual
o próximo valor da lista
Isso vai te forçar a usar índice (range(len(...))) pela primeira vez de forma realmente necessária """

# numeros = [10, 20, 30, 40, 50]
# resultado = []
# for i in range(len(numeros)-1):
#   soma = numeros[i] + numeros[i + 1]
#   resultado.append(soma)
# print(resultado)


""" Dada a lista:
numeros = [10, 20, 15, 30, 25, 40]
Crie uma nova lista contendo a diferença entre cada número e o próximo.
Exemplo:
20 − 10 = 10
15 − 20 = -5
30 − 15 = 15
25 − 30 = -5
40 − 25 = 15
Resultado esperado:
[10, -5, 15, -5, 15]
A lógica é praticamente a mesma do exercício anterior.
Só muda a operação: em vez de somar, você calcula a diferença entre vizinhos. """

# numeros = [10, 20, 15, 30, 25, 40]
# resultado = []
# for i in range(len(numeros)-1):
#   diferenca = numeros[i + 1] - numeros[i]
#   resultado.append(diferenca)
# print(resultado)

""" Dada a lista:
numeros = [10, 12, 15, 14, 18, 20, 19]
Crie um programa que conte:
quantas vezes o número aumentou em relação ao anterior
quantas vezes diminuiu
quantas vezes ficou igual
Exemplo de raciocínio:
12 > 10 → aumentou
15 > 12 → aumentou
14 < 15 → diminuiu
18 > 14 → aumentou
20 > 18 → aumentou
19 < 20 → diminuiu
Você vai usar exatamente o mesmo padrão de índice (i e i+1), mas agora só comparando e contando. """

# numeros = [10, 12, 15, 14, 18, 20, 19]
# contagem_diminuiu = 0
# contagem_aumentou = 0
# contagem_igual = 0
# for i in range(len(numeros)-1):
#   if numeros[i] > numeros[i + 1]:
#     contagem_diminuiu += 1
#     simbolo = '>'
#     print(f'{numeros[i]} {simbolo} {numeros[i + 1]}: Diminuiu')
#   elif numeros[i] < numeros[i + 1]:
#     contagem_aumentou += 1
#     simbolo = '<'
#     print(f'{numeros[i]} {simbolo} {numeros[i + 1]}: Aumentou')
#   else:
#     contagem_igual += 1 
#     simbolo = '='
#     print(f'{numeros[i]} {simbolo} {numeros[i + 1]}: Igual')
# print(f'Diminuiu {contagem_diminuiu} vezes')
# print(f'Aumentou {contagem_aumentou} vezes')
# print(f'Ficou igual {contagem_igual} vezes')


""" Encontrar o primeiro valor válido e parar
Dada a lista:
numeros = [3, 8, 4, 11, 2, 15, 6]
Crie um programa que:
Percorra a lista na ordem
Encontre o primeiro número maior que 10
Imprima esse número
Pare o laço imediatamente quando encontrar
Ou seja:
Ele NÃO deve continuar analisando o resto da lista
Assim que achar o primeiro valor que atende à condição, termina """

# numeros = [3, 8, 4, 10, 2, 1, 6]
# encontrou = False
# for i in numeros:
#   if i <= 10:
#     print(f'{i} -> Não')
#   else:
#     encontrou = True
#     print(f'{i} -> Sim')
#     break
# if not encontrou:
#   print('Nenhum número maior que 10, programa finalizado!')
  
""" Agora vamos inverter a lógica.
Dada a lista:
numeros = [12, 18, 25, 30, 7, 40]
Faça um programa que:
Encontre o primeiro número ímpar
Mostre esse número
Pare o laço
Resultado esperado:
12 -> par
18 -> par
25 -> ímpar (PARA AQUI)
Ou seja, o programa deve parar no 25 e não continuar para 30, 7, 40.
Desafio extra:
E se todos fossem pares? Como avisar isso no final? """

# numeros = [12, 18, 25, 30, 7, 40]
# encontrou_impar = False
# for i in numeros:
#   if i % 2 == 0:
#     print(f'{i} -> Par')
#   else:
#     encontrou_impar = True
#     print(f'{i} -> Ímpar')
#     break
# if not encontrou_impar:
#   print('Todos são pares')

""" Agora vamos combinar várias ideias:
Dada a lista:
numeros = [2, 4, 6, 8, 10, 11, 14, 16]
Faça um programa que:
Conte quantos números pares aparecem antes do primeiro ímpar
Pare o laço quando encontrar o primeiro ímpar
Mostre o total de pares contados até ali
Raciocínio esperado:
2 → par (conta)
4 → par (conta)
6 → par (conta)
8 → par (conta)
10 → par (conta)
11 → ímpar → PARA
Resultado:
Foram encontrados 5 números pares antes do primeiro ímpar
Esse exercício mistura:
contador
condição
break
ordem dos dados
É bem próximo de problemas reais de análise sequencial.
 """
# numeros = [2, 4, 6, 8, 10, 12, 14, 16]
# contador_pares = 0
# for i in numeros:
#   if i % 2 == 0:
#     contador_pares += 1
#     print(f'{i} -> Par')
#   else:
#     print(f'{i} -> Ímpar')
#     print(f'Foram encontrados {contador_pares} números pares antes do primeiro ímpar')
#     break
# else:
#   print(f'Nenhum ímpar na lista, foram encontrados {contador_pares} números pares')

""" numeros = [5, 7, 7, 9, 12, 12, 12, 3]
Objetivo:
Contar quantas vezes um número aparece igual ao anterior.
Dica reforçada:
Você precisa comparar pares assim:
atual
anterior
Ou seja:
numeros[i]   com   numeros[i-1]
Mas atenção:
O primeiro elemento não tem anterior.
Então o laço não deve começar do índice 0.
Esse detalhe é o coração do exercício.
 """


# numeros = [5, 7, 7, 9, 12, 12, 12, 3]
# contador = 0
# for i in range(len(numeros) -1):
#   if numeros[i] == numeros[i+1]:
#     contador += 1
# print(f'Foram encontradas {contador} repetições consecutivas' )

""" Dada a lista:
numeros = [5, 5, 5, 2, 2, 7, 7, 7, 7, 3]
Seu programa deve descobrir:
Qual foi a maior sequência de números iguais consecutivos.
Entenda o que isso significa
Olhe a lista por blocos:
5, 5, 5 → sequência de tamanho 3
2, 2 → sequência de tamanho 2
7, 7, 7, 7 → sequência de tamanho 4
3 → sequência de tamanho 1
A maior sequência é a do número 7, com tamanho 4.
Saída esperada
Maior sequência consecutiva: 4
Dicas importantes (sem entregar a fórmula)
Você vai precisar de duas variáveis principais:
Uma que conta a sequência atual
(quantos iguais seguidos você está vendo agora)
Uma que guarda a maior sequência já encontrada """

# numeros = [5, 5, 5, 2, 2, 7, 7, 7, 7, 3]
# sequencia_atual = 1
# maior_sequencia = 1
# for i in range(len(numeros) -1):
  
#   if numeros[i] == numeros[i+1]:
#     sequencia_atual += 1
#   else:
#      if sequencia_atual > maior_sequencia:
#         maior_sequencia = sequencia_atual
#      sequencia_atual = 1
# if sequencia_atual > maior_sequencia:
#       maior_sequencia = sequencia_atual
# print(maior_sequencia)

""" Dada a lista:
numeros = [5, 5, 5, 2, 2, 7, 7, 7, 7, 3, 3, 8]
Crie uma nova lista que mantenha apenas um valor de cada sequência consecutiva.
O que isso significa
Você não quer remover todos os repetidos da lista inteira.
Você quer remover só os repetidos que estão colados.
Exemplo:
5, 5, 5  → vira só 5
2, 2     → vira só 2
7, 7, 7, 7 → vira só 7
3, 3     → vira só 3
8        → continua 8 """
# numeros = [5, 5, 5, 2, 2, 7, 7, 7, 7, 3, 3, 8]

# lista_filtrada = [] 
# lista_filtrada.append(numeros[0])

# for i in range(len(numeros) - 1):
#   if numeros[i] == numeros[i + 1]:
#     continue
#   else:
#      lista_filtrada.append(numeros[i + 1])
# print(lista_filtrada)

""" Agora faça o contrário.
Dada a mesma lista:
[5, 5, 5, 2, 2, 7, 7, 7, 7, 3, 3, 8]
Crie uma nova lista contendo:
o número
e quantas vezes ele apareceu consecutivamente
Resultado esperado:
[(5, 3), (2, 2), (7, 4), (3, 2), (8, 1)]
Ou seja:
5 apareceu 3 vezes seguidas
2 apareceu 2 vezes seguidas
7 apareceu 4 vezes seguidas
3 apareceu 2 vezes seguidas
8 apareceu 1 vez """

# numeros = [5, 5, 5, 2, 2, 7, 7, 7, 7, 3, 3, 8,9,9]

# lista_contada = [] 
# contagem = 1


# for i in range(len(numeros) - 1):
#   if numeros[i] == numeros[i + 1]:
#     contagem += 1
    
#   else:
#      lista_parcial = (numeros[i],contagem)
#      contagem = 1
#      lista_contada.append(lista_parcial)
     
# maior_qtd = 0
# numero_maior = 0

# for numero, quantidade in lista_contada:
#     if quantidade > maior_qtd:
#         maior_qtd = quantidade
#         numero_maior = numero

# print(f"Número com maior sequência: {numero_maior} ({maior_qtd} vezes)")


""" Dada a lista:
numeros = [4, 7, 4, 2, 7, 4, 3, 7, 7, 2]
Você deve descobrir:
qual número aparece mais vezes na lista inteira
e quantas vezes ele aparece
Resultado esperado
Nesse caso:
4 aparece 3 vezes
7 aparece 4 vezes
2 aparece 2 vezes
3 aparece 1 vez
Saída:
Número que mais se repete: 7 (4 vezes) """

# numeros = [1,1,1,1,5,5,5,5,5,1,5,3,9,8,7,6,5,4,3,2,1] 
# maior_qtd = 0
# numero_mais_frequente = 0

# for i in numeros:
#   qtd = numeros.count(i)
#   if qtd > maior_qtd:
#     maior_qtd = qtd
#     numero_mais_frequente = i
# print(numero_mais_frequente)


""" Encontrar todos os números que se repetem
Dada a lista:
numeros = [4, 7, 4, 2, 7, 4, 3, 7, 7, 2, 9]
Você deve descobrir:
quais números aparecem mais de uma vez
sem repetir o mesmo número na resposta
Resultado esperado
Números que se repetem: [4, 7, 2]
Porque:
4 aparece 3 vezes
7 aparece 4 vezes
2 aparece 2 vezes
3 aparece 1 vez → ignora
9 aparece 1 vez → ignora """

# numeros = [4, 7, 4, 2, 7, 4, 3, 7, 7, 2, 9,]

# lista = []

# for i in numeros:
#   qtd = numeros.count(i)
#   if i not in lista and qtd != 1:
#     lista.append(i)
# print(lista)

""" Dada a mesma lista:
numeros = [4, 7, 4, 2, 7, 4, 3, 7, 7, 2, 9]
Crie uma nova lista contendo apenas os números que aparecem UMA única vez.
Resultado esperado:
[3, 9]
Porque:
4 → repete → fora
7 → repete → fora
2 → repete → fora
3 → aparece 1 vez → entra
9 → aparece 1 vez → entra """

# numeros = [4, 7, 4, 2, 7, 4, 3, 7, 7, 2, 9]
# lista = []
# for i in numeros:
#   qtd = numeros.count(i)
#   if i not in lista and qtd == 1:
#     lista.append(i)
# print(lista)

""" Agora vamos trabalhar com transformação da lista.
Dada:
numeros = [10, 15, 20, 25, 30, 35]
Crie uma nova lista onde:
Se o número for par → divide por 2
Se for ímpar → multiplica por 2
Resultado esperado:
[5, 30, 10, 50, 15, 70]
Porque:
10 → par → 10/2 = 5
15 → ímpar → 15*2 = 30
20 → 10
25 → 50
30 → 15
35 → 70 """

# numeros = [10, 15, 20, 25, 30, 35]
# lista = []

# for i in numeros:
#   if i % 2 == 0:
#     lista.append(i // 2)
#   else:
#     lista.append(i * 2)
# print(lista)

""" Dada a lista:
numeros = [3, 8, 15, 2, 9, 20, 7]
Crie três listas novas:
uma com números menores que 10
uma com números entre 10 e 15 (inclusive)
uma com números maiores que 15
Resultado esperado:
menores_10 = [3, 8, 2, 9, 7]
entre_10_15 = [15]
maiores_15 = [20]
Dica:
Você já fez algo muito parecido antes.
Vai usar múltiplos if/elif e três listas """

# numeros = [3, 8, 15, 2, 9, 20, 7]
# menores_10 = []
# entre_10_15 = []
# maiores_15 = []

# for i in numeros:
#   if i < 10:
#     menores_10.append(i)
#   elif 10 <= i <= 15:
#     entre_10_15.append(i)
#   else:
#     maiores_15.append(i)
# print(f'menores_10: {menores_10}')
# print(f'entre_10_15: {entre_10_15}')
# print(f'maiores_15: {maiores_15}')

""" Dada a lista:
numeros = [10, 20, 30, 40, 50]
Crie uma nova lista onde:
cada posição contém a soma do número com o índice dele
Ou seja:
posição 0 → 10 + 0 = 10
posição 1 → 20 + 1 = 21
posição 2 → 30 + 2 = 32
posição 3 → 40 + 3 = 43
posição 4 → 50 + 4 = 54
Resultado final:
[10, 21, 32, 43, 54]
Dica:
Aqui você não pode usar só:
for i in numeros:
Porque você precisa do índice e do valor ao mesmo tempo.
Pense em usar:
range(len(numeros))
Assim você consegue acessar:
o índice
e o valor naquela posição. """
numeros = [10, 20, 30, 40, 50]
lista = []
#for i in range(len(numeros)):
#   soma = (numeros[i] + i)
#   lista.append(soma)
# print(lista)

""" Dada a lista:
numeros = [10, 20, 30, 40, 50, 60]
Crie uma nova lista contendo:
a diferença entre o número atual e o anterior
Ou seja:
20 − 10 = 10
30 − 20 = 10
40 − 30 = 10
50 − 40 = 10
60 − 50 = 10
Resultado:
[10, 10, 10, 10, 10]
Dica importante:
Você precisa acessar:
numeros[i]     e     numeros[i-1]
Então o laço não pode começar do 0.
Porque o primeiro elemento não tem anterior. """

# numeros = [10, 20, 30, 40, 50, 60]
# sub = []
# for i in range(1, (len(numeros))):
#   sub.append(numeros[i] - numeros[i - 1])
# print(sub)

""" Dada a lista:
numeros = [10, 22, 21, 35, 30, 31, 50]
Crie uma lista com o tipo de variação entre elementos consecutivos:
"subiu" se o atual > anterior
"desceu" se o atual < anterior
"igual" se forem iguais
Resultado esperado:
['subiu', 'desceu', 'subiu', 'desceu', 'subiu', 'subiu']
Dica: mesmo padrão de índice (for i in range(1, len(numeros))), mas agora você compara e adiciona strings em vez de números. """

# numeros = [10, 22, 21, 35, 30, 31, 50]
# lista = []
# for i in range(len(numeros)-1):
#   if numeros[i] < numeros[i+1]:
#     lista.append('Subiu')
#   elif numeros[i] > numeros[i+1]:
#     lista.append('Desceu')
#   else:
#     lista.append('Manteu')
# print(lista)

""" Usando essa mesma lista:
numeros = [10, 22, 21, 35, 30, 31, 50]
Conte:
quantas vezes subiu
quantas vezes desceu
quantas vezes manteve
Saída esperada:
Subiu: 4
Desceu: 2
Manteve: 0
Dica:
Você já fez algo parecido várias vezes:
criar contadores
aumentar conforme a condição acontece
Só que agora, em vez de guardar em lista, você vai só contar. """

# numeros = [10, 22, 21, 35, 30, 31, 50]
# subiu = 0
# desceu = 0
# manteve = 0

# for i in range(1, len(numeros)):
#   if numeros[i] > numeros[i-1]:
#     subiu += 1
#   elif numeros[i] < numeros[i-1]:
#     desceu += 1 
#   else:
#     manteve += 1
# print(f'Subiu: {subiu}')
# print(f'Desceu: {desceu}')
# print(f'Manteve: {manteve}')

""" Com a mesma lista:
numeros = [10, 22, 21, 35, 30, 31, 50]
Calcule:
o total de variações (já é len(numeros)-1)
a porcentagem de vezes que subiu
a porcentagem de vezes que desceu
a porcentagem de vezes que manteve
Saída esperada (aprox.):
Total de variações: 6
Subiu: 66.67%
Desceu: 33.33%
Manteve: 0.00%
Dica: porcentagem = (contador / total) * 100. Formate com duas casas decimais. """

# numeros = [10, 22, 21, 35, 30, 31, 50]
# subiu = 0
# desceu = 0
# manteve = 0
# for i in range(1, len(numeros)):
#   if numeros[i] > numeros[i-1]:
#     subiu += 1
#   elif numeros[i] < numeros[i-1]:
#     desceu += 1
#   else:
#     manteve += 1
# total_variacao = subiu + desceu + manteve
# pct_subiu = (subiu / total_variacao) * 100     
# pct_desceu = (desceu / total_variacao) * 100
# pct_manteve = (manteve / total_variacao) * 100

# print(f'Total de variações: {total_variacao}')
# print(f'subiu: {pct_subiu:.2f}')
# print(f'Desceu: {pct_desceu:.2f}')
# print(f'Manteve: {pct_manteve:.2f}')


estoque = {
  "Arroz": {"quantidade": 30, "preco": 25.00},
  "feijao": {"quantidade":15, "preco": 18.50},
  "Macarrao": {"quantidade":50, "preco": 10.00},
  "oleo": {"quantidade":10, "preco": 22.00},
  "acucar": {"quantidade":40, "preco": 8.00},
  "cafe": {"quantidade":5, "preco": 30.00}
}
import pandas
estoque_com_desconto = {
  nome: {
    "quantidade": dados["quantidade"],
    "preco": dados["preco"] * 0.9 if dados["preco"] > 20 else dados['preco']
  }
 for nome, dados in estoque.items()
}
print(pandas.DataFrame(estoque_com_desconto))
