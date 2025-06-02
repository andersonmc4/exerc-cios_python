print('============================')
print('=======Chapéu-seletor=======')
print('============================')

grifinoria = 0
corvinal = 0
lufa_lufa = 0
sonserina = 0
#~~~~~~~~~~~~~~~~~~Questao1~~~~~~~~~~~~~~~~~~
print("Você gosta do amanhecer ou do anoitecer?")
print("1) Amanhecer")
print("2) Anoitecer")
resposta1= int(input("Digite 1 ou 2: "))
if resposta1==1:
  grifinoria +=1
  corvinal +=1
elif resposta1 == 2:
  lufa_lufa +=1
  sonserina +=1
else:
  print("Entrada errada")
#~~~~~~~~~~~~~~~~~~Questao2~~~~~~~~~~~~~~~~~~
print("\n(Questao 2)\nQuando eu morrer, quero que as pessoas se lembrem de mim como:")
print("1) O bom")
print("2) O Grande")
print("3) O Sábio")
print("4) O Ousado")
resposta2 = int(input("Digite uma das quatro opções:"))
if resposta2 ==1:
  lufa_lufa +=2
elif resposta2 ==2:
  sonserina +=2
elif resposta2 ==3:
  corvinal +=2
elif resposta2 ==4:
  grifinoria +=2
else:
  print("Entrada Errada")
#~~~~~~~~~~~~~~~~~~Questao3~~~~~~~~~~~~~~~~~~
print('\n(Questao 3)\n Que tipo de instrumento agrada mais ao seu ouvido?')
print('1) O Violino')
print('2) A Trombeta')
print('3) O Piano')
print('4) O Tambor')
resposta3 = int(input("Digite uma das quatro opções: "))
if resposta3 == 1:
  sonserina +=4
elif resposta3 == 2:
  lufa_lufa +=4
elif resposta3 == 3:
  corvinal +=4
elif respota3 == 4 :
  grifinoria += 4

#~~~~~~~~~~~~~~~~~~Pontuação~~~~~~~~~~~~~~~~~~

print('=======================')
print('=======Pontuação=======')
print('=======================')

if grifinoria >= lufa_lufa >= corvinal >= sonserina:
  print("A pontuação de Grifinória é ", grifinoria)
elif corvinal >= grifinoria >= lufa_lufa >= sonserina:
  print("A pontuaçaõ de Corvinal é ", corvinal)  
elif lufa_lufa >= grifinoria >= corvinal >= sonserina:
  print("A pontuaçaõ de Corvinal é ", lufa_lufa)
elif sonserina >= grifinoria >= lufa_lufa >= corvinal:
  print("A pontuaçaõ de Corvinal é ", sonserina)
