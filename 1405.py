try : 
    numero = int(input("digite um número :"))
    resultado = 10 / numero 
    print(f"Resultado:{resultado}")
    break
except ValueError:
    print("error :entrada invalida")
except ZeroDivisionError :
    print("erro : divisão por zero")

# aula do dia 14/05/2025 sobre tratamento de excessões;
# como fazer para perdir que o usuario continue o codigo após o erro;