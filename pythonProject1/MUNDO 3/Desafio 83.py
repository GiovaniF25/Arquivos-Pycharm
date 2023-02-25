# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expr = str(input("Digite uma expressão:"))
pilha = 0
for cont in expr:
    if cont == '(':
        pilha += 1
    if cont == ')':
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0
    print("Sua expressão é valida!!!")
else:
    print("Sua expressão é invalida!!!")