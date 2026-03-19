#contagem regressiva de 10 até 0 com 1 segundo de intervalo

import time

for i in range(10, -1, -1):
  print(i)
  time.sleep(1)
print('Feliz ano novo!')