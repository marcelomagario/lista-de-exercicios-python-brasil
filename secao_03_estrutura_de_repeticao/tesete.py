numero = 223
centenas_msg = dezenas_msg = unidades_msg = ''

if numero <= 0:
    print('O número precisa ser positivo')
if numero > 1000:
    print('O número precisa ser menor que 1000')

centenas_numero = numero // 100
centenas_numero, numero = divmod(numero, 100)


if centenas_numero == 1:
    centenas_msg = '1 centena'
if centenas_numero > 1:
    centenas_msg = f'{centenas_numero} centenas'


print(centenas_msg)
