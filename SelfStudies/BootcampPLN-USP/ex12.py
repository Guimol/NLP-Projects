file = open("teste.txt", 'w')

file.write("Escrevendo os numeros de 1 a 10: \n")
for i in range(1,11):
    file.write(str(i) + " ")

file.close()

file = open("teste.txt", 'r')

conteudo = file.read()

print(conteudo)

file.close()

print("\nNovo Arquivo\n")

file = open("teste.txt", 'w')

file.write("Escrevendo os numeros de 11 a 20: \n")
for i in range(11,21):
    file.write(str(i) + " ")

file.close()

file = open("teste.txt", 'a')

file.write("\nAdicionando ao final os numeros de 21 a 30: \n")
for i in range(21,31):
    file.write(str(i) + " ")

file.close()

file = open("teste.txt", 'r')

conteudo = file.read()

print(conteudo)

file.close()

print("\nLeitura Nova\n")

file = open("teste.txt", 'r')

conteudo = file.readlines()

i = 1
for aux in conteudo:
    print(f"Linha {i}: {aux}")
    i += 1

file.close()