# Assignment no.2: Simple Data


# Table of Contents
# ------------------------------
# 1. Variables and print
# --
# 2. Input and string operators
# --
# 3. Input and cast
# --
# 4. Operations and operands
# --
# 5. Remainder


# 1. Variables and print
# -----------------------------------------------------------------

# a - declarar uma variável contendo a nossa string
foo = 'The quick brown fox jumps over the lazy dog'

# b - declarar uma função que vai receber uma string como argumento
def inline_words(str):

    # separar cada palavra da string e metê-la numa lista
    list_of_words = str.split()

    # para cada palavra da posição n da lista de palavras
    # guardar essa palavra numa tabela  de simbolos local
    # e imprimir essas palavras na mesma linha
    for (n, word) in enumerate(list_of_words):
        locals()[f'palavra{n}'] = word
        print(word, end=' ')

# c - chamar a função
inline_words(foo)


print('\n--\n')


# 2. Input and string operators
# -----------------------------------------------------------------

# a - declarar as vars que recebem o input do header
#     e do texto respetivamente
header_tag = input('Escreva aqui o tipo de header: ')
header_txt = input('Escreva aqui o texto: ')

# b - print do resultado injetando as variaveis criadas
#     anteriormente numa formatted string
print(f'<{header_tag}>{header_txt}</{header_tag}>')


print('\n--\n')


# 3. Input and cast
# -----------------------------------------------------------------

# a - declarar a var que recebe o input do tipo Int
user_input = input('Introduza um valor numérico: ')

# b - declarar uma função que recebe um parâmetro <n>
#     e imprime o resultado de n + nn + nnn
def funky_sum(n):

    one_number = int(n)
    two_numbers = int(n * 2)
    three_numbers = int(n * 3)

    print(f'{one_number} + {two_numbers} + {three_numbers} = {one_number + two_numbers + three_numbers}')

# c - chamar a função
funky_sum(user_input)


print('\n--\n')


# 4. Operations and operands
# -----------------------------------------------------------------

# a - declarar variáveis que recebem o input do utilizador
user_pr_amount = int(input('Principal Amount: '))
user_in_rate = float(input('Interest Rate: '))
user_frq = int(input('Frequency: '))

# b - declarar uma função que recebe como parâmetro essas variáveis
#     (quantia principal, juros e frequência de pagamento) e devolve
#     o resultado da aplicação da fórmula
def final_amount(pr_amount, in_rate, frq):
    return pr_amount * ((1 + (in_rate/frq))) ** (frq * 2)

# c - print da chamada da função com o resultado
print('Final amount: ', final_amount(user_pr_amount, user_in_rate, user_frq))


print('\n--\n')


# 5. Remainder
# -----------------------------------------------------------------

# a - fazer import do módulo <datetime>
import datetime

# b - declarar uma função que calcula e imprime a hora do
#     alarme tendo em conta as horas e os minutos introduzidos
#     pelo user
def set_alarm(hour, minute):

    # objeto datetime do dia de hoje
    today = datetime.datetime.now()
    # objeto datetime para o alarme
    alarm = today + datetime.timedelta(hours=hour, minutes=minute)

    # converter para String e formatar em hora:minuto:segundo
    curr_time = today.strftime('%H:%M:%S')
    alarm_time = alarm.strftime('%H:%M:%S')

    # imprimir resultado
    print(f'Agora: {curr_time} \nAlarme: {alarm_time}')


# c - declarar variaveis que guardam input do user (horas e minutos
#     até ao alarme disparar e chamar a func com esse input
hours_to_trigger = int(input('Hora(s): '))
minutes_to_trigger = int(input('Minuto(s): '))
set_alarm(hours_to_trigger, minutes_to_trigger)

