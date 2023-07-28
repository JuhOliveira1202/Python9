#Exercício 12:
#Faça um programa que receba e valide as seguintes informações:
#   - Nome: maior que 3 caracteres;
#   - idade: entre o e 100;
#   - Salário: maior que zero;
#   - Sexo: "f" ou "m";
#   - Estado Civil: "s", "c", "v", "d";
#Use a função len(string) para saber o tamanho de um texto (número de carcateres).

nome = input("Insira o seu nome aqui")
while len(nome) <=3:
    nome = input("O nome tem de conter mais de 3 caracteres")


idade = int (input("Insira a sua idade"))
while idade<0 or idade>100:
    idade = input("A sua idade não é compativel com a pedida")

    
salario = float(input("Insira aqui o seu salário mensal"))
while salario<0:
    salario = float(input("O seu salário tem que ser superior a 0"))

    
sexo = input("Sexo (f ou m)")
while sexo!='f' and sexo!='m':
    sexo=input("Sexo(\"f\" ou \"m\")")
    

estado_civil = input("Estado Civil s, c, v, d")
while estado_civil!='c' and estado_civil != 's' and estado_civil !='v' and estado_civil!='d':
    estado_civil = input("estado civil s, c, v, d,")
    
