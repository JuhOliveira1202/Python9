#Exercício 11:
#Faça um programa qeu peça uma nota, entre 0 e 20.
#Mostre uma mensagem caso o valor seja inválido e
#continue pedindo introduza um valor correto.

x= eval (input("Introduza um número"))

while x>=20:
    print("O valor não esta entre 0 e 20")
    x= eval (input("Introduza um número"))
    if x<20:
        break 
    
