# Missão 1: Restaurando as Regras Escolares 📝 

Média_escolar = 6
Nota_aluno= int(input("Digite a nota do aluno:"))

if Nota_aluno >= Média_escolar:
    print (f"Parabéns, você foi aprovado com a média {Nota_aluno}")
else:
    print (f" Infelizmente você foi reprovado com a média {Nota_aluno}")


# Missão 2: O Sistema Eleitoral Secreto 📝 

idade_votação=16
idade_usuário= int (input("Digite sua idade:"))
if idade_usuário >= idade_votação:
    print ("Você pode votar. Faça com atenção!")
else:
    print ("Você ainda não pode votar. O voto é a partir de 16 anos.")


# Missão 3: Recuperando o Sistema de Notas 📊

nota= int (input("Digite a nota do aluno (0-100):"))
if 90<= nota <=100:
    print("Parabéns, você tirou A!")
elif 80<= nota <=89:
    print("Muito bem, você tirou B.")
elif 70<= nota <=79:
    print("Bom trabalho, você tirou C.")
elif 60<= nota <=69:
    print("Fique atento, você tirou D.")
elif 0<=nota <60:
    print("Estude um pouco mais, você tirou F.")
else:
    print("Nota inválida. Por Fvaor, insira uma nota de 0 a 100.")


# Missão 4: Restaurando a Identificação de Números ⚖️

valor_um=float(input("Digite o primeiro valor:"))
valor_dois=float(input("Digite o seundo valor:"))
print(f"A soma equivale a: {valor_um + valor_dois:.2f} ")

# Missão 5: Recuperando o Cofre de Segurança 🔒

password_ok= "Python123"
password_user=input("Digite a sua senha de acesso ao cofre:")
if password_user == password_ok:
    print("Acesso concedido! Seja bem vindo =)")
else:
    print("Acesso negado. Senha incorreta.")

# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
 
contagem=1
while contagem <=10:
    print(f"Reforçando a segurança e a contagem do sistema {contagem}")
    contagem+=1

# Missão 7: Organizando a Lista📋

lista= [8, 3, 10, 1, 5]
lista.sort()
print(lista)

# Missão 8: Acessando os Registros de Alunos 🏷️

alunos=("Ana", "Bruno", "Carla", "Daniel", "Eduardo")

print(alunos[0], alunos[4])

# Missão 9: Calculando Dobro de um Número 🛠️

def dobro(number):
    resultado = number *2
    return f"O dobro de {number} é {resultado}"
number = 5
mensagem = dobro(number)
print(mensagem)

# Missão 10: Contando Letras 🔄

name= "Tulani"
print(len(name))
