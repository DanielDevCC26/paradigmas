#prog que aceite o sexo de alguem, somente m e f.

r = ''
while r not in ['m', 'f']:
  r = str(input('Qual o seu sexo? ')).lower()
  if r not in ['m', 'f']:
    print('Resposta inválida, tente novamente!')
print('fim')