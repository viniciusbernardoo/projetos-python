#calcular o emprestimo no banco
print("        Banco Bradesco         ")
print("_______________________________________")
print("")
cliente=input("informe o nome do cliente :")
print("________________________________________")
print("")
print("    Valor Do emprestimo    ")
print("3% ate R$ 10,000.00        ")
print("5%  R$ 10,001.00 ate R$ 20,000.00 ")
print("7%  R$ 20,001.00 ate R$ 30,000.00 ")
print("10% mais de R$ 30,000.00")
print("")
print("_______________________________________")
#pedir o valor do emprestimo
valoremprestimo=float(input("informe o valor do emprestimo:"))
print("      formas de pagamento    ")
print("       cartão de credito  -")
print("_______________________________________")
print("1 - em 6 meses juros de 8%   ")
print("2 - em 10 meses juros de 14% ")
print("3 - em 15 meses juros de 20% ")
print("4 - em 24 meses juros de 30% ")
print("")
print("_______________________________________")
#informa as parcelas
valor=float(input("digite a opção de parcelas  - "))
print("===========================================")
#informar numro menores que 10,000.00
if valoremprestimo <=10000 and valor == 1:
    totaldejuros= valoremprestimo *0.11
    totaldejuros= totaldejuros/6
    print("o valor das parcelas é",totaldejuros)
    
if valoremprestimo <=10000 and valor == 2:
    totaldejuros=valoremprestimo *0.17
    totaldejuros= totaldejuros/10
    print("o valor das parcelas é",totaldejuros)
      
if valoremprestimo <=10000 and valor ==3:
    totaldejuros=valoremprestimo  *0.23
    totaldejuros= totaldejuros/15
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo <10000 and valor ==4:
    totaldejuros=valoremprestimo *0.33
    totaldejuros= totaldejuros/24
    print("o valor das parcelas é",totaldejuros)
#informar o numero maior que10,001.00 e menor que 20,000.00 
if valoremprestimo >10001 and valoremprestimo<20000 and  valor ==1:
    totaldejuros=valoremprestimo*0.13
    totaldejuros= totaldejuros/6 
    print("o valor das parcelas é",totaldejuros)
    
if valor >10001 and valoremprestimo <20000 and valor ==2:
    totaldejuros=valoremprestimo *0.19
    totaldejuros= totaldejuros/10
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo >10001 and valoremprestimo<20000 and valor ==3:
    totaldejuros=valoremprestimo *0.25
    totaldejuros= totaldejuros/15
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo >10001 and valoremprestimo<20000 and valor ==4:
    totaldejuros=valoremprestimo *0.35
    totaldejuros= totaldejuros/24
    print("o valor das parcelas é",totaldejuros)
 #informar numero maior que 20,001.00 e menor que 30,000.00     
if valoremprestimo >20001 and valoremprestimo<30000 and valor ==1:
    totaldejuros=valoremprestimo *0.15
    totaldejuros= totaldejuros/6
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo >20001 and valoremprestimo<30000 and valor==2:
    totaldejuros=valoremprestimo *0.21
    totaldejuros= totaldejuros/10
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo >20001 and valoremprestimo<30000 and valor ==3:
    totaldejuros=valoremprestimo *0.27
    totaldejuros= totaldejuros/15
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo >20001 and valoremprestimo<30000 and valor ==4:
    totaldejuros=valoremprestimo*0.40
    totaldejuros= totaldejuros/24
    print("o valor das parcelas é",totaldejuros)
#informar numeros maior que 30,001.00
if valoremprestimo >=30001 and valor==1:
    totaldejuros=valoremprestimo *0.18
    totaldejuros= totaldejuros/6
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo>30001 and valor==2:
    totaldejuros=valoremprestimo *0.24
    totaldejuros= totaldejuros/10
    print("o valor das parcelas é",totaldejuros)
    
if valoremprestimo>30001 and valor ==3:
    totaldejuros=valoremprestimo *0.30
    totaldejuros= totaldejuros/15
    print("o valor das parcelas é",totaldejuros)

if valoremprestimo>30001 and valor ==4:
    totaldejuros= valoremprestimo *0.40
    totaldejuros= totaldejuros/24
    print("o valor das parcelas é",totaldejuros)
#mostrar o nome do cliente e o preço final
print("o cliente",cliente,"tem o valor final de ",totaldejuros)