#Apresentação para os clientes.
print('Bem vindo(a) a empresa da Anna Dara Moraes Araujo')
#Lista vazia, variável para iniciar o valor inicial do ID e dicionário vazio.
lista_funcionarios = []
id_global = 4940680
funcionario = {}
#Função para cadastrar os funcionários.
def cadastrar_funcionario(id):
  print('-'*49)
  print('-'*11 + 'MENU CADASTRAR FUNCIONARIO' + '-'*12)
  funcionario['ID'] = id
  funcionario['Nome'] = input('Nome do funcionário: ')
  funcionario['Setor'] = input('Setor do funcionário: ')
  funcionario['Salario'] = float(input('Salário do funcionário: '))
  lista_funcionarios.append(funcionario.copy())
#Função para consultar a lista de funcionários de várias maneiras.
def consultar_funcionarios():
  while True:
    try:
      print('-'*49)
      print('-'*11 + 'MENU CONSULTAR FUNCIONARIO' + '-'*12)
      print('Escolha a opção desejada: \n1 - Consultar todos\n2 - Consultar por ID\n3 - Consultar por setor\n4 - Retornar ao menu')
      escolha = int(input('>>'))
      if escolha == 1:
        for funcionario in lista_funcionarios: #Mostra na tela todos os funcionários cadastrados.
          print('-'*49)
          print(f"ID: {funcionario['ID']}\nNome: {funcionario['Nome']}\nSetor: {funcionario['Setor']}\nSalário: {funcionario['Salario']}")
      elif escolha == 2:
        inf_id = int(input('Digite o número do ID: '))
        for funcionario in lista_funcionarios:
          if funcionario['ID'] == inf_id: #Mostra na tela as informações do ID escolhido.
            print('-'*49)
            print(f"ID: {funcionario['ID']}\nNome: {funcionario['Nome']}\nSetor: {funcionario['Setor']}\nSalário: {funcionario['Salario']}")
      elif escolha == 3:
        inf_setor = input('Informe qual setor gostaria de verificar: ')
        for funcionario in lista_funcionarios:
          if funcionario['Setor'].lower() == inf_setor.lower(): #Mostra os funcionários que trabalham no setor escolhido.
            print('-'*49)
            print(f"ID: {funcionario['ID']}\nNome: {funcionario['Nome']}\nSetor: {funcionario['Setor']}\nSalário: {funcionario['Salario']}")
      elif escolha == 4:
        return #Retorna ao Menu Pincipal.
      else:
        print('Opção inválida! Escolha a opção de 1 a 4.')
    except:
      print('Opção inválida!')
#Função para remover um funcionário da lista.
def remover_funcionario():
    try:
      print('-'*49)
      print('-'*12 + 'MENU REMOVER FUNCIONARIO' + '-'*13)
      remover = int(input('Digite o ID do funcionário que deseja remover: '))
      for funcionario in lista_funcionarios:
        if funcionario['ID'] == remover:
          lista_funcionarios.remove(funcionario)
          print('\nFuncionário removido com sucesso!')
    except:
      print('ID Inválido!')

#Programa principal
while True:
  try:
    print('-'*49)
    print('-'*17 + 'MENU PRINCIPAL' + '-'*18)
    print('Escolha a opção desejada: \n1 - Cadastrar funcionário.\n2 - Consultar funcionário.\n3 - Remover funcionário.\n4 - Encerrar programa.')
    menu = int(input('>>'))
    if menu == 1: #Acessa a função de cadastrar funcionários.
      id_global += 1
      cadastrar_funcionario(id_global)
    elif menu == 2: #Acessa a função de consultar os funcionários da lista.
      consultar_funcionarios()
    elif menu == 3: #Acessa a função de remover funcionáriosda lista.
      remover_funcionario()
    elif menu == 4: #Encerra o programa.
      print('Encerrando o programa...')
      break
    else:
      print('Opção inválida! Escolha a opção de 1 a 4.')
  except:
    print('\nOpção inválida!')