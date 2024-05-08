#Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.
#Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.


def animal(p1, p2, p3):
    if p1=='vertebrado':
        if p2=='ave':
            if p3=='carnivoro':
                return 'aguia'
            else:
                return 'pomba'
        else:
            if p3=='onivoro':
                return 'homem'
            else:
                return 'vaca'
    else:
        if p2=='inseto':
            if p3=='hematofago':
                return 'pulga'
            else:
                return 'lagarta'
        else:
            if p3=='hematofago':
                return 'sanguessuga'
            else:
                return 'minhoca'

p1 = input()
p2 = input()
p3 = input()
print(animal(p1, p2, p3))
