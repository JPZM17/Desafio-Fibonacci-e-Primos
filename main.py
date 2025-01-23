# Fibonacci

# -- Criar uma função em sua linguagem preferida. 
# A função deve receber um numero N >= 0 (deve validar o input para a função), 
# e retornar o valor correspondente desse número na sequência Fibonacci. 
# EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

#--- Criar uma função recursiva que resolva Fibonacci

def fibonacci_recursivo(n : int):
  if not isinstance(n, int) or n < 0:
    print("Por favor, insira um numero inteiro superior a zero")
    return 
  if n <= 1:
    return n
  else:
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# --- Criar uma função linear que resolva Fibonacci

def fibonacci(n:int):
  if not isinstance(n, int) or n < 0:
    print("Por favor, insira um numero inteiro superior a zero")
    return 
  
  if n == 0:
    return 0
  elif n == 1:
    return 1

  num_a = 0
  num_b = 1

  for i in range(2, n+1):
    num_a, num_b = num_b, num_a + num_b
  
  return num_b

# Numeros Primos

#-- Criar uma função em sua linguagem preferida. 
# A função deve receber um numero N > 1 (validar o input), 
# e retornar todos os números primos até o número N. 
# EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

#  --- Criar uma função recursiva que resolva p

#para isso optei por fazer uma pequena funcão auxiliar

def eh_primo(n, divisor=None):
  if divisor is None:
        divisor = n - 1
  if n <= 1:
        return False
  if divisor == 1:
        return True
  if n % divisor == 0:
        return False
  return eh_primo(n, divisor - 1)

#funcao em si

def numeros_primos_recursiva(n : int):
  if not isinstance(n, int) or n < 1:
    print("Por favor, insira um numero inteiro superior a um (1)")
    return   
  
  #fiz outra func auxiliar
  def auxiliar(x):
    if x < 2:
      return []
    if eh_primo(x):
      return auxiliar(x - 1) + [x]
    return auxiliar(x - 1)

  return auxiliar(n)

# --- Criar uma função linear que resolva p

def numeros_primos(n: int):
  if not isinstance(n, int) or n < 1:
    print("Por favor, insira um numero inteiro superior a um (1)")
    return 
  
  num_primos = []
  for i in range(2, n + 1):
    for j in range(2, int((i / 2)) + 1):
      if i%j == 0:
        break
    else:
      num_primos.append(i)
  
  return num_primos


# UI

def mostrar_opcoes_iniciais():
  print("Escolha uma das opcões: ")
  print("1 - Fibonacci")
  print("2 - Numeros Primos")

def mostrar_opcoes_solucoes():
  print("Como quer executar a funcão? Escolha uma das formas a baixo")
  print("1 - Linear")
  print("2 - Regressiva")
  
  
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
  else:
    mostrar_resultado(fibonacci_recursivo(num_fibonacci))
else:
  print("Digite um número e a funcão mostrara")
  print("os numeros primos que existem até ele.")
  num = int(input())
  if escolha_solucao == 1:
    mostrar_resultado(numeros_primos(num))
  else:
    mostrar_resultado(numeros_primos_recursiva(num))

