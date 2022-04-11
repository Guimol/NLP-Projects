file = open('qbdata.txt', 'r')

linhas = file.readlines()

for linha in linhas:
    linha = linha.split(' ')
    if(linha[2] == 'QB,'):
        print(f"{linha[0]} {linha[1]} teve valor {linha[len(linha) - 1]}")