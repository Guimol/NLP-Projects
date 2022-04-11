lista = list(range(10))
lista.append(6)
lista.insert(3,7)
lista.remove(3)
lista.append(4)

print(f"Lista: {lista}")

print(f"Qntd de 4 na lista: {lista.count(4)}")

print(f"Tres Primeiros: {lista[0:3]}")
print(f"Entre 3 e 7: {lista[3:7]}")
print(f"Pulando de 3 em 3: {lista[::3]}")
print(f"Ultimos 3: {lista[-3:]}")
print(f"Todos menos os 4 ultimos: {lista[:-4]}")

print(f"6 elemento da lista: {lista[6]}")
lista[7] = 12

print(f"Lista: {lista}")

lista.reverse()

print(f"Lista Invertida: {lista}")

lista.sort()

print(f"Lista Ordenada: {lista}")
