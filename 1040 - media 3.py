#Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
#Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ".
#Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0,
#imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas,
#o programa deve imprimir a mensagem "Aluno em exame.".

#No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
#Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
#Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado."
#(caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos
#(aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.



def eh_media(a, b, c, d):
    media = (a * 2 + b * 3 + c * 4 + d * 1) /10
    return media

a, b, c, d = input().split()
a, b, c, d = float(a), float(b), float(c), float(d)

if eh_media ( a, b ,c ,d)  > 6.9:
    print("Media:",f'{eh_media(a,b,c,d):.1f}')
    print("Aluno aprovado.")

elif eh_media(a,b,c,d) >= 5.0 and eh_media(a,b,c,d) < 6.9:
    print("Media:",eh_media(a,b,c,d))
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame:",e)
    if eh_media(a,b,c,d) + e / 2 > 6.9:
        print("Aluno aprovado.")
        print("Media final:",(eh_media(a,b,c,d) + e) / 2)
        

else: 
    print("Media:",f'{eh_media(a,b,c,d):.1f}')
    print("Aluno reprovado.")



# Matheus Silva























