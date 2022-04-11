frase_original = " instituto de ciências matemáticas e de computação"
frase = frase_original + " usp"
frase = frase + " " + str(2021)
print(f"Frase: \'{frase}\'")
print(len(frase))

print(f"Frase maiuscula: \'{frase.upper()}\'")
print(f"Frase minuscula: \'{frase.lower()}\'")

frase = frase[1:]
print(f"Frase sem primeiro espaço (slicing): \'{frase}\'")

frase = frase.replace('a', 'x')
print(f"Frase \'a\' -> \'x\': \'{frase}\'")

frase = frase.split()
print(frase)
print(len(frase))

frase = ' de '.join(frase)
print(f"Frase: \'{frase}\'")

frase = frase.split('de')
print(frase)
print(len(frase))

aux = ''
for token in frase:
    if token != ' ':
        token = token.strip()
        aux = aux + token + " "
frase = aux

print(f"Frase: \'{frase}\'")

frase = frase_original.split()
frase = '\\'.join(frase)
print(f"Frase: \'{frase}\'")

#print(f"Olaaa \' \\n \'")