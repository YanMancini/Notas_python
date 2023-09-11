import os
from time import sleep

os.system("cls")
print ("Media de quatro notas")

sleep(1.5)

os.system("cls")

nt1=123
nt2=123
nt3=123
nt4=123

while nt1<0 or nt1>100:
      nt1=int(input("Digite sua primeira nota: "))
      os.system("cls")

while nt2<0 or nt2>100:
      nt2=int(input("Digite sua segunda nota: "))
      os.system("cls")

while nt3<0 or nt3>100:
      nt3=int(input("Digite sua terceira nota: "))
      os.system("cls")

while nt4<0 or nt4>100:
      nt4=int(input("Digite sua quarta nota: "))
      os.system("cls")


media=(nt1+nt2+nt3+nt4)/4

os.system("cls")

if media>59:
   print("você foi aprovado com a média:",media)

elif media<40:
     print("você foi reprovado com a média:",media)
     
elif media>39 and media<59:
     print("Você esta de recuperação com a média:",media)
