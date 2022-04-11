dicio = {'chave1': 'valor1', 'chave2': 17, 'chave3': list(range(3)), 'chave4': tuple(range(3)), 'chave5': {'outro': 'dict'}}


print(f"Chaves do dict: {dicio.keys()}")
print(f"Valores do dict: {dicio.values()}")
print(f"Itens do dict: {dicio.items()}")
print(f"Segundo item do dict: {list(dicio.items())[1]}")
print(f"Dict: {dicio}")

for key,value in dicio.items():
    print(f"{key} tem como valor {value}")
