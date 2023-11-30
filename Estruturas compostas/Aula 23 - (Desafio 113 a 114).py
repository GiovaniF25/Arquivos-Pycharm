#ERROS EXEÇÕES E SEUS TRATAMENTOS

# Se eu colocar o try e depois um except, quando eu rodar nao vai aparecer mas aquela mensagem vermelha, ele vai mostrar a
# mensagem que eu escrevi no print em baixo do except
try:
    a = int(input('Denominador: '))
    b = int(input('Numerador: '))
    r = a/b
except Exception as erro:
    print(f'ERRO! Problema encontrado foi {erro.__class__} ')
else:
    print(f'O resultado é {r}')
finally: #opcional, mensagem final
    print('Volte sempre, muito obrigado')

#ou

try:
    a = int(input('Denominador: '))
    b = int(input('Numerador: '))
    r = a/b
except(ValueError, TypeError):
    print(f'ERRO! (tivemos um problema com os valores que voce digitou')
except ZeroDivisionError:
    print('Não é possível dividir um númeor por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu nao informar os dados')
