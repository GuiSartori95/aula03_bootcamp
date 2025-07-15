### FOR

## Iniciante

# 1. Tabuada do 5
# Imprima a tabuada do número 5 usando for.

# for numero in range(11):
#       print(f"5 x {numero} = {5 * numero}")


# 2. Soma de 1 a 100
# Use for para somar todos os números de 1 até 100.
# soma = 0
# for i in range(1, 101):
#       soma += i
# print("soma de 1 a 100:", soma)

## Intermediário

# 3. Média de notas
# Dada a lista [7.5, 8, 9.2, 6.8], use for para calcular a média.

# lista = [7.5, 8, 9.2, 6.8, 10]
# soma = 0
# for i in lista:
#     soma += i
# media = soma / len(lista)
# print(f"A média das notas dos alunos é:", media)

# 4. Contar vogais
# Peça uma palavra ao usuário e conte quantas vogais ela tem usando for.

palavra = input("Insira uma palavra: ")

for i in palavra:
     vogais = 'aeiou'
     conta_vogal = vogais.count(i)
print(f"A palavra tem:", conta_vogal, "vogais")


## Avançado

# 5. Números primos até 100
# Liste todos os números primos de 1 a 100 usando for.

# 6. Pirâmide de asteriscos
# Peça um número e imprima uma pirâmide de * com esse número de linhas.
# Ex: n = 4

### WHILE

## Iniciante

# 1. Contador de 1 a 10
# Imprima os números de 1 a 10 usando while.

# 2. Senha correta
# Peça ao usuário para digitar uma senha até ele acertar a senha correta (ex: "admin123").


## Intermediário

# 3. Menu interativo
# Crie um menu com as opções:
# 1 - Ver saldo
# 2 - Fazer depósito
# 3 - Sair
# O menu deve continuar aparecendo até o usuário escolher "3 - Sair".

# 4. Jogo da adivinhação
# Gere um número aleatório entre 1 e 10 e peça tentativas até o usuário acertar.


## Avançado

# 5. Par ou ímpar com placar
# Usuário e computador jogam par ou ímpar.
# Quem ganhar 3 vezes primeiro vence o jogo.

# 6. Validador simples de CPF
# Peça ao usuário um CPF (apenas números) e valide:
# - Se tem exatamente 11 dígitos
# - Se os números não são todos iguais

### IF / ELSE

## Iniciante

# 1. Par ou ímpar
# Peça um número ao usuário e diga se ele é par ou ímpar.

# 2. Maior entre dois números
# Peça dois números e informe qual é o maior, ou se são iguais.


## Intermediário

# 3. Classificação de idade
# Com base na idade do usuário, classifique como:
# - Criança (0–12)
# - Adolescente (13–17)
# - Adulto (18+)

# 4. Calculadora simples
# Peça dois números e uma operação (+, -, *, /) e exiba o resultado correspondente.


## Avançado

# 5. Validador de senha forte
# Peça uma senha ao usuário e valide:
# - Pelo menos 8 caracteres
# - Pelo menos 1 número
# - Pelo menos 1 letra maiúscula
# - Pelo menos 1 caractere especial

# 6. Triângulo válido
# Peça três lados e diga se eles formam um triângulo válido.
# Regra: a soma de dois lados deve ser maior que o terceiro.