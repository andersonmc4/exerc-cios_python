import random 

pergunta = str(input("Faça uma pergunta: "))

pergunta = random.randint(1, 9)

if pergunta ==1:
  print("Sim - definitivamente.")
elif pergunta ==2:
  print("É decididamente SIM")
elif pergunta ==3:
  print("Sem dúvida.")
elif pergunta ==4:
  print("Resposta nebulosa, tente novamente.")
elif pergunta ==5:
  print("Pergunte novamente mais tarde.")
elif pergunta ==6:
  print("Melhor não contar agora.")
elif pergunta ==7:
  print("Minhas fontes dizem que não.")
elif pergunta ==8:
  print("As perspectivas não são tão boas.")
elif pergunta ==9:
  print("Muito duvidoso.")              