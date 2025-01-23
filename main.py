# Fibonacci

# -- Criar uma função em sua linguagem preferida. 
# A função deve receber um numero N >= 0 (deve validar o input para a função), 
# e retornar o valor correspondente desse número na sequência Fibonacci. 
# EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
def fibonacci(n:int):
  if n < 0:
    print("Por favor, insira um numero superior a zero")
    return 
  
  num_a = 1
  num_b = 0
  i = 0

  while(i <= n):
    print("num_a: " + str(num_a))
    print("num_b: " + str(num_b))
    num_novo = num_a + num_b
    num_b = num_a
    num_a = num_novo
    i += 1

  return num_novo
  

#--- Criar uma função recursiva que resolva Fibonacci

def fibonacci_recursivo(n : int):
  if n < 0:
    print("Por favor, insira um numero superior a zero")
    return 
  if n <= 1:
    return n
  else:
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# --- Criar uma função linear que resolva Fibonacci



# Numeros Primos

#-- Criar uma função em sua linguagem preferida. 
# A função deve receber um numero N > 1 (validar o input), 
# e retornar todos os números primos até o número N. 
# EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

def numeros_primos(n: int):
  if n < 1:
    print("Por favor, insira um numero superior a um (1)")
    return 
  
  num_primos = []
  for i in range(2, n + 1):
    for j in range(2, int((i / 2)) + 1):
      if i%j == 0:
        break
    else:
      num_primos.append(i)
  
  return num_primos

#  --- Criar uma função recursiva que resolva p



# --- Criar uma função linear que resolva p




# UI

def mostrar_opcoes_iniciais():
  print("Escolha uma das opcões: ")
  print("1 - Fibonacci")
  print("2 - Numeros Primos")

def mostrar_opcoes_solucoes():
  print("Como quer executar a funcão? Escolha uma das formas a baixo")
  print("1 - Padrão")
  print("2 - Regressão")
  print("3 - Linear")
  
def mostrar_resultado( resultado):
  print("Aqui esta o resultado: ")
  print(resultado)

#final
mostrar_opcoes_iniciais()

escolha_desafio = 0
while (escolha_desafio != 1 and escolha_desafio != 2):
  escolha_desafio = int(input())
  if escolha_desafio != 1 and escolha_desafio != 2:
    print("Por favor, escolha uma opcão valida")
    mostrar_opcoes_iniciais()

mostrar_opcoes_solucoes()

escolha_solucao = 0
while (escolha_solucao != 1 and escolha_solucao != 2 and escolha_desafio != 3):
  escolha_solucao = int(input())
  if (escolha_solucao != 1 and escolha_solucao != 2 and escolha_desafio != 3):
    print("Por favor, escolha uma opcão valida")
    mostrar_opcoes_solucoes()

if escolha_desafio == 1:
  print("Digite um número, e a funcão ira mostrar qual o valor desta posicão")
  print("Na sequencia de Fibonacci!")
  num_fibonacci = int(input())
  if escolha_solucao == 1:
    mostrar_resultado(fibonacci(num_fibonacci))
  elif escolha_solucao == 2:
    mostrar_resultado(fibonacci_recursivo(num_fibonacci))
  else:
    pass
else:
  print("Digite um número e a funcão mostrara")
  print("os numeros primos que existem até ele.")
  num = int(input())
  if escolha_solucao == 1:
    mostrar_resultado(numeros_primos(num))
  elif escolha_solucao == 2:
    pass
  else:
    pass

