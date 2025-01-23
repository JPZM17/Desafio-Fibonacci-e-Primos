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
    num_novo = num_a + num_b
    num_b = num_a
    num_a = num_novo
    i += 1
  print("Aqui esta o resultado: ")
  print(num_novo)

  pass

#--- Criar uma função recursiva que resolva Fibonacci


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
  print("2 - ")
  print("1 - Padrão")


#final
mostrar_opcoes_iniciais()
escolha_desafio = int(input())
#TENHO QUE VALIDAR A ESCOLHA

