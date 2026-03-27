#prog que aceite o sexo de alguem, somente m e f.
sexo = 'mf'
r = 'x'
while r not in sexo:
  r = str(input('Qual o seu sexo? [M/F] ')).lower()
  if r not in sexo:
    print('Resposta inválida, tente novamente!')
if r == 'm':
  print('Sexo masculino informado com sucesso!')
else:
  print('Sexo feminino registrado com sucesso!')