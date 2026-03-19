#prog qu leia duas notas de um aluno e calcule sua média. a média é 7, 5 à 6.9 recupração e menos que 5 reprova

nota1 = float(input('Qul a nota da primeira prova? '))
nota2 = float(input('Qul a nota da segunda prova? '))
media = (nota1+nota2)/2

if media >= 7:
  print('Parabéns você foi aprovado!')
elif media >=5:
  print('Atenção. Você está de recuperação!')
else:
  print('Sinto muito. Você está reprovado.')