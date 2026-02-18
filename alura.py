

'''gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]


media = sum(gastos) / len(gastos)
print(media)

for i in range(len(gastos)):
    if gastos[i] > 3500:
        print(gastos[i])

print(len(gastos))'''


'''lista = list(map(int, input('Insira os valores separados por vírgula: ').split(',')))

def calcula(x):
  tam = len(x)
  soma = sum(x)
  menor = min(x)
  maior = max(x)
  return (tam, soma, menor, maior)
tam, soma, menor, maior = calcula

calcula(lista)


print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}")
'''

valor = int(input('insira um valor: '))
taboada = lambda x: x * 7
print(taboada(valor))
