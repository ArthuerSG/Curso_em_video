n = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(n.upper()))
print('Seu nome em minúsculas é {}'.format(n.lower()))
print('Seu nome tem ao todo {} de letras'.format(len(n) - n.count(' ')))
#print('O Seu primeiro nome tem {} de letras'.format(n.find(' ')))
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))