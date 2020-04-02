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
 
       elif aposta == "Twelve":
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==12:
               saldo+=(ficha*30)
               print("A soma dos seus dados foi de {0}, você ganhou! Você agora tem {1} fichas".format(soma_dados,saldo))
           else:
               saldo-=ficha
               print ("A soma dos seus dados foi de {0}, você sua aposta, seu saldo agora é de {1}".format(soma_dados,saldo))
 
   if quantas_apostas==2:
       aposta2 = input("Suas opções de aposta são: Pass Line Bat e Field; Pass Line Bat e Any Craps; Pass Line Bat e Twelve; Field e Any Craps; Field e Twelve; Any Craps e Twelve. Qual deseja fazer?(Escreva a sua opção exatamente como esta aqui) ")
       if aposta2 == "Pass Line Bat e Field":
           print("Nesta fase, se a soma dos dados for 2, ganha o mesmo valor que apostou, se for 3, não ganha nem perde nada, se for 4,9 ou 10, vai para a fase Point e ganha o mesmo valor que apostou, se for 5,6 ou 8 iria para a fase Poin mas perde tudo no Field, se for 7, ganha a Pass Line Bat, mas perde tudo no Field e se for 11 ou 12, ganha o dobro do que apostou")
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
          
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==2:
               saldo+=ficha
               print("você tirou 2, ganhou o mesmo valor que apostou! seu saldo agora é de {0}".format(saldo))
           if soma_dados==3:
               saldo=saldo
               print("você tirou 3, seu saldo continua {0}".format(saldo))
           if soma_dados==4 or soma_dados==9 or soma_dados==10:
               saldo+=ficha
               print("Você foi para a fase Point e ganhou as fichas que apostou")
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
 
           if soma_dados==5 or soma_dados==6 or soma_dados==8:
               saldo-=saldo
               print("Você iria para fase Point, mas perdeu tudo no Field")
           if soma_dados==7:
               saldo-=saldo
               print("você tirou 7, ganhou no Pass Line Bat mas perdeu tudo no Field")
           if soma_dados==11 or soma_dados==12:
               saldo+=ficha*2
               print("Você ganhou o dobro do que apostou, seu saldo agora é de {0}".format(saldo))

        if aposta2 == "Pass Line Bat e Any Craps":
            print("Nesta fase, se a soma dos dados for 2, 3 ou 12, você ganhará seis vezes o que apostou; se for 7 ou 11, não ganha nem perde nada; se for 4,5,6,8,9 ou 10, você perde as fichas que apostou e muda para fase Point")
            dado1= random.randrange(1,7)
            dado2= random.randrange(1,7)
            soma_dados= dado1+dado2
            print(soma_dados)
            ficha = int(input("Quantas fichas deseja apostar? "))
            if soma_dados==2 or soma_dados==3 or soma_dados==12:
                saldo+=ficha*6
                print("Você ganhou seis vezes as fichas que apostou, seu saldo agora é de {0}".format(saldo))
            if soma_dados==7 or soma_dados==11:
                saldo=saldo
                print("Você não ganhou nem perdeu nada, seu saldo continua {0}".format(saldo))
            if soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
                saldo-=ficha
                print("Você foi para a fase Point e perdeu as fichas que apostou, seu saldo é de {0}".format(saldo))
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
 
       if aposta2== "Pass Line Bat e Twelve":
           print("Nesta fase, se a soma dos dados for 2 ou 3, o jogador perde duas vezes as fichas que apostou; se a soma for 4,5,6,8,9 ou 10, você perde o que apostou e vai para fase Point; se a soma for 7 ou 11, nem ganha nem perde nada e se a soma dos dados for 12, o jogador ganha vinte e nove vezes as fichas que apostou")
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==2 or soma_dados==3 :
               saldo-=ficha*2
               print("Você perdeu duas vezes o que apostou, seu saldo agora é de {0}".format(saldo))
           if soma_dados==7 or soma_dados==11:
               saldo=saldo
               print("você não ganhou nem perdeu nada, seu saldo continua {0}".format(saldo))
           if soma_dados==12:
               saldo+=ficha*29
               print("Você tirou dois seis, o seu saldo agora é de {0}".format(saldo))
           if soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10 :
               saldo-=ficha
               print("Você foi para a fase Point e perdeu as fichas que apostou, seu saldo é de {0}".format(saldo))
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

        if aposta2== "Field e Any Craps":
            print("Nesta fase do jogo, se a soma dos dados jogados for 4,9,10 ou 11, o jogador não ganha nem perde nada; se for 5,6,7 ou 8, o jogador perde tudo; se for 3 você ganha trinta e uma vezes o que apostou; se for 2, ganha trinta e duas vezes as fichas que apostou e se for 12, ganha trinta e tres vezes o que apostou.")
            dado1= random.randrange(1,7)
            dado2= random.randrange(1,7)
            soma_dados= dado1+dado2
            ficha = int(input("Quantas fichas deseja apostar? "))
            if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
                saldo-=saldo
                print("Você perdeu tudo, a soma dos seus dados foi de {0}".format(soma_dados))
            if soma_dados==3:
                saldo+=ficha*31
                print("A soma dos seus dados foi de 3, seu saldo agora é de {0}".format(saldo))
            if soma_dados==2:
                saldo+=ficha*32
                print("A soma dos seus dados foi de 2, seu saldo agora é de {0}".format(saldo))
            if soma_dados==12:
                saldo+=ficha*33
                print("A soma dos seus dados foi de 12, seu saldo agora é de {0}".format(saldo))
            if soma_dados==4 or soma_dados==9 or soma_dados==10 or soma_dados==11:
                saldo=saldo
                print("a soma dos seus dados foi de {0}, seu saldo continua {1}".format(soma_dados,saldo))
       if aposta2== "Field e Twelve":
           print("Nesta fase do jogo, se a soma dos dados for 5,6,7 ou 8, o jogador perde tudo; se for 3,4,9,10 ou 11, não ganha nem perde nada; se for 2, o jogador ganha o mesmo valor que apostou e se for 12, ganha trinta e tres vezes as fichas que apostou.")
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           print(soma_dados)
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
               saldo-=saldo
               print("a soma dos seus dados foi de {0}, você perdeu todas suas fichas".format(soma_dados))
           if soma_dados==3 or soma_dados==4 or soma_dados==9 or soma_dados==10 or soma_dados==11:
               saldo=saldo
               print("a soma dos seus dados foi de {0}, seu saldo continua {1}.".format(soma_dados,saldo))
           if soma_dados==2:
               saldo+=ficha
               print("você tirou dois uns, seu saldo agora é de {0}".format(saldo))
           if soma_dados==12:
               saldo+=ficha*33
               print("A soma dos seus dados foi de 12, seu saldo agora é de {0}".format(saldo))
 
       if aposta2=="Any Craps e Twelve":
           print("Nesta fase do jogo, se a soma dos dados forem 2 ou 3, você ganha seis vezes o que apostou; se for 6,7,8,9,10 e 11, você perde duas vezes as fichas que apostou e se for 12, você ganha trinta e sete vezes o que apostou")
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados== 2 or soma_dados==3:
               saldo+=ficha*6
               print("A soma dos seus dados foi de {0}, seu saldo agora é de {1}".format(soma_dados,saldo))
           if soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8 or soma_dados==9 or soma_dados==10 or soma_dados==11:
               saldo-=ficha*2
               print("a soma dos seus dados foi de {0}, seu saldo agora é {1}".format(soma_dados,saldo))
           if soma_dados==12:
               saldo+=ficha*37
               print("Você tirou dois seis, seu saldo agora é de {0}".format(saldo))
 
   if quantas_apostas==3:
       aposta3= input("Suas opções de aposta são: Pass Line Bat, Field e Any Craps; Pass Line Bat, Field e Twelve; Pass Line Bat, Any Craps e Twelve; Field, Any Craps e Twelve ")
        if aposta3== "Pass Line Bat, Field e Any Craps":
            print("Neste tipo de aposta, se a soma dos dados for 2, você ganha 8 vezes a aposta; se for 3, ganha sete vezes a aposta; se for 4,9 ou 10, vai para fase point; se tirar 5,6,7 ou 8, perde tudo; se for 11, ganha a aposta; se for 12, ganha 9 vezes as fichas que apostou.")
            dado1= random.randrange(1,7)
            dado2= random.randrange(1,7)
            soma_dados= dado1+dado2
            ficha = int(input("Quantas fichas deseja apostar? "))
            if soma_dados==2:
                saldo+=ficha*8
                print("você tirou dois uns, seu saldo agora é de {0}".format(saldo))
            if soma_dados==3:
                saldo+=ficha*7
                print("a sua soma dos dados foi de 3, seu saldo algora é de {0}".format(saldo))
            if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
                saldo-=saldo
                print("a soma dos seus dados foi de {0}, seu saldo agora é {1}".format(soma_dados,saldo))
            if soma_dados==11:
                saldo+=ficha
                print("a soma dos seus dados foi de 11, seu saldo agora é {0}".format(saldo))
            if soma_dados== 12:
                saldo+=ficha*9
                print("você tirou dois seis, seu saldo agora é de {0}".format(saldo))
            if soma_dados==4 or soma_dados==9 or soma_dados==10:
                print("Você foi para a fase Point ")
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

        if aposta3== "Pass Line Bat, Field e Twelve":
            print("Neste tipo de aposta, se a soma dos dados for 2 você continua com o seu saldo inalterado; se for 3, perde o que apostou; se for 4,9 ou 10, você vai para fase Point; se for 5,6,7 ou 8, você perde tudo;se for 11, ganha o que apostou; se for 12, ganha 32 vezes o que apostou. ")
            dado1= random.randrange(1,7)
            dado2= random.randrange(1,7)
            soma_dados= dado1+dado2
            print(soma_dados)
            ficha = int(input("Quantas fichas deseja apostar? "))
            if soma_dados==2 :
                saldo=saldo
                print("você tirou dois uns, o seu saldo continua {0} ".format(saldo))
            if soma_dados==3:
                saldo-=ficha
                print("Você perdeu as fichas que apostou, seu saldo agora é de {0}".format(saldo))
            if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
                saldo-=saldo
                print("a soma dos seus dados foi de {0}, você perdeu tudo".format(soma_dados))
            if soma_dados==11:
                saldo+=ficha
                print("a soma dos seus dados foi de 11, você ganhou a aposta, seu saldo agora é de {0}".format(saldo))
            if soma_dados== 12:
                saldo+=ficha*32
                print("a soma dos seus dados foi de 12, seu saldo agora é de {0}".format(saldo))
            if soma_dados==4 or soma_dados==9 or soma_dados==10:
                print("Você foi para a fase Point ")
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
       if aposta3=="Pass Line Bat, Any Craps e Twelve":
           print("Neste tipo de aposta, se os dados somarem 2 ou 3, você ganha cinco vezes o que apostou; se somarem 4,5,6,8,9 ou 10, você vai para fase Point e perde duas vezes o que apostou; se a soma dos dados dao 7 ou 11, você perde o que apostou, se a soma der 12, você ganha 29 vezes o que apostou.")
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados== 2 or soma_dados==3:
               saldo+=ficha*5
               print(" a soma dos seus dados foi de {0}, seu saldo agora é {1}".format(soma_dados,saldo))
           if soma_dados==7 or soma_dados==8:
               saldo-=ficha
               print(" a soma dos seus dados foi de {0}, seu saldo agora é {1}".format(soma_dados,saldo))
           if soma_dados==12:
               saldo+=ficha*29
               print("Você tirou dois seis, seu saldo agora é {0}".format(saldo))
           if soma_dados==4 or soma_dados==5 or soma_dados==6 or soma_dados==8 or soma_dados==9 or soma_dados==10:
               saldo-=ficha*2
               print("Você foi para a fase Point e perdeu duas vezes as fichas que apostou, seu saldo é de {0}".format(saldo))
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
 
       if aposta3=="Field, Any Craps e Twelve":
           print("Nesta opção, caso os dados somem 2, o jogador ganha oito vezes o que apostou, se somar 3, ganha sete vezes, se somar 4, 9, 10, ou 11, o jogador perde o que apostou, se somar 5, 6, 7, ou 8, você perde tudo e se somar 12 nos dados, ganhará quarenta vezes o que apostou.")
           dado1= random.randrange(1,7)
           dado2= random.randrange(1,7)
           soma_dados= dado1+dado2
           ficha = int(input("Quantas fichas deseja apostar? "))
           if soma_dados==2:
               saldo+=ficha*8
               print(" a soma dos seus dados foi 2, seu saldo agora é {0}".format(saldo))
           if soma_dados==3:
               saldo+=ficha*7
               print(" a soma dos seus dados foi 3, seu saldo agora é {0}".format(saldo))
           if soma_dados==4 or soma_dados==9 or soma_dados==10 or soma_dados==11:
               saldo-=ficha
               print(" a soma dos seus dados foi de {0}, seu saldo agora é {1}".format(soma_dados,saldo))
           if soma_dados==5 or soma_dados==6 or soma_dados==7 or soma_dados==8:
               saldo-=saldo
               print("A soma dos seus dados foi {0}, você perdeu tudo.".format(soma_dados))
           if soma_dados==12:
               saldo+=ficha*40
               print("A soma dos seus dados foi de 12, seu saldo agora é {0}".format(saldo))
 
                       