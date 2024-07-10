AGENDA  = {}


def mostrar_contato():
    for contato in AGENDA:
        buscar_contato(contato)
        print("-----------------------")


def buscar_contato(contato):
    print('Nome:', contato)
    print("Telefone:", AGENDA[contato]["tel"])
    print("Email:", AGENDA[contato]["email"])
    print("Endereço:", AGENDA[contato]["endereco"]) 


def inserir_editar_contato(contato, tel, email, endereco):
    AGENDA[contato] = {
        'tel':tel,
        'email':email,
        'endereco':endereco,
    }
    print('>>>> Contato {} adicionado|editado com sucesso'.format(contato))


def excluir_contato(contato):
    AGENDA.pop(contato)
    print('>>>>Contato {} excluido com sucesso'.format(contato))




AGENDA["pedro"] = {
    "tel":"98707-4578",
    "email":"pedro@gmail.com",
    "endereco":"av 5"
}

AGENDA["joao"] = {
    "tel":"97956-6548",
    "email":"joao@gmail.com",
    "endereco":"av 6"
}

print('1-Mostrar todos os contatos')
print('2-Buscar contato')
print('3-Incluir contato')
print('4-Editar contato')
print('5-Excluir contato')
print('0-Fechar agenda')
print()
opcao = input('Digite uma opção: ')
print()

if opcao == '1':
    mostrar_contato()
    print()
elif opcao == '2':
    contato = input('Digite o contato: ')
    print()
    buscar_contato(contato)
    print()
elif opcao == '3' or opcao == '4':
    contato = input('Digite o nome do contato: ')
    tel = input('Digite o telefone:')
    email = input('Digite o Email:')
    endereco = input('Digite o Endereço:')
    print()
    inserir_editar_contato(contato, tel, email, endereco)
elif opcao == '5':
    contato = input('Digite o nome do contato: ')
    print()
    excluir_contato(contato)
elif opcao == '0':
    print('Fechando o programa...')
else:
    print('Opção inválida')

