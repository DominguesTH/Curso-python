# ##Praticando
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Problema encontrado foi {erro.__class__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte Sempre! Muito obrigado!')


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print(f'Não é possivel dividir o número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito obrigado!')
