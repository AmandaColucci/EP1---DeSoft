#crapsinsper
import random
 
nome = input("Qual o seu nome? ")
print("Olá, {0}!".format(nome))
 
saldo = 1000
print("{0}, o seu saldo é de {1} fichas".format(nome,saldo))
print("Você está na fase Come out")

while saldo>0:
   quantas_apostas= int(input("Quantos tipos de aposta deseja fazer(1,2,3 ou 4)? "))
   if quantas_apostas==1:
       aposta = input("Suas opções de aposta são: Pass Line Bat, Field, Any Craps e Twelve. Qual deseja fazer? ")
       if aposta == "Pass Line Bat":
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==7 or soma_dados==11:
               print("Você ganhou!")
               saldo+=ficha
               print("Seu saldo é de {}".format(saldo))
           elif soma_dados==2 or soma_dados==3 or soma_dados==12:
               print(" você fez um Craps, perdeu {0} fichas".format(ficha))
               saldo-=ficha
               print("Seu saldo é de {}".format(saldo))
           else:
               print("Você foi para a fase Point")
               print("O seu objetivo agora é sortear os dados para que a soma deles seja igual a {0}".format(soma_dados))
              
               dado1_point= random.randrange(1,7)
               dado2_point= random.randrange(1,7)
               soma_dados_point=dado1_point+dado2_point
               a= True
 
               if soma_dados_point==soma_dados:
                   a= False
                   saldo+=ficha
                   print("Você ganhou! Seu saldo agora é de {0}".format(saldo))
               elif soma_dados_point == 7:
                   a= False
                   saldo==0
                   print("Você perdeu! Seu saldo agora é {0}".format(saldo))
               else:
                   while a == True:
                       print("Você ainda esta na fase Point, os dados serão jogados novamente até que você ganhe, ou tire 7 (perdendo o jogo)")
                      
                       dado1_point= random.randrange(1,7)
                       dado2_point= random.randrange(1,7)
                       soma_dados_point=dado1_point+dado2_point
                       if soma_dados_point==soma_dados:
                           a= False
                           saldo+=ficha
                           print("Você ganhou! Seu saldo agora é de {0}".format(saldo))
                       elif soma_dados_point == 7:
                           a= False
                           saldo-=saldo
                           print("Você perdeu! Seu saldo agora é {0}".format(saldo))
      
       elif aposta == "Field":
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
               saldo-=saldo
               print ("A soma dos seus dados foi de {0}, você perdeu o jogo!".format(soma_dados))
           elif soma_dados==3 or soma_dados==4 or soma_dados==9 or soma_dados==10 or soma_dados==11:
               saldo+=ficha
               print("A soma dos seus dados foi de {0}, você ganhou! Você agora tem {1} fichas".format(soma_dados,saldo))
           elif soma_dados==2:
               saldo+=(ficha*2)
               print("A soma dos seus dados foi de {0}, você ganhou! Você agora tem {1} fichas".format(soma_dados,saldo))
           else:
               saldo+=(ficha*3)
               print("A soma dos seus dados foi de {0}, você ganhou! Você agora tem {1} fichas".format(soma_dados,saldo))
 
       elif aposta == "Any Craps":
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           print(soma_dados)
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==2 or soma_dados==3 or soma_dados==12:
               saldo+=(ficha*7)
               print("A soma dos seus dados foi de {0}, você ganhou! Você agora tem {1} fichas".format(soma_dados,saldo))
           else:
               saldo-=ficha
               print ("A soma dos seus dados foi de {0}, você sua aposta, seu saldo agora é de {1}".format(soma_dados,saldo))
 
