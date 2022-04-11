CPF = '12345678900'
name = 'Guilherme Oliveira'
tel = '912345678'
user = 'guimol'

novoContato = [CPF, name, tel, user]

agenda = {CPF: {'nome': name, 'telefone': tel, 'userTwitter': user}}

for contatoChave, contatoValor in agenda.items():
    print(f"{contatoChave}: {contatoValor['nome']}, {contatoValor['telefone']} ({contatoValor['userTwitter']})")