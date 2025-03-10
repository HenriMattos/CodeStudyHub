# Aula: 03. Estrutura de Condições e Controle

idade = float ((input("Digite sua idade: ")))

#Forma 1

if idade >= 18:
        print("Pode entrar na Festa")
else: 
    if idade < 18:
        print("Nao pode entrar na Festa")
        
#Forma 2
        
if idade >= 18:
    print("Pode entrar na Festa")
else: 
    print("Nao pode entrar na Festa")
    
#Forma 3

if idade >= 18:
    print("Pode entrar na Festa")
elif idade < 18:
    print("Nao pode entrar na Festa")
    
#Forma 4

if idade >= 18:
    print("Pode entrar na Festa")
elif idade < 17 and idade >= 16:
    print("Pode entrar na Festa acompanhado pelos pais")
else:
    print("Nao pode entrar na Festa")
    
#Forma 5

if idade >= 18:
    print("Pode entrar na Festa")
elif idade >= 17 or idade == 17:
    print("Pode entrar na Festa acompanhado por um amigo maior de idade")