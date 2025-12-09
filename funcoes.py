# Definição de Dados:

# Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir

# informações como nome, descrição, prioridade e categoria. Você pode usar dicionários para representar as tarefas.
# prioridade:
# 1=pequena, 2=media, 3=grande
# categoria
# 1=pessoal,2=profissional, 3=financeiro, 4=lazer

# nome, descricao, prioridade, categoria, situação 
# Funções:
# Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
# como concluídas, exibir tarefas por prioridade ou categoria, e outras funcionalidades que desejar.
tarefas=[]

def adc_tarefas():
    nome=input('Tarefa: ')
    descrição=input('O que será feito: ')
    prioridade=int(input('Prioridade: '))
    categoria=int(input('Categoria: '))
    situação= False

    nova_tarefa={
    'Nome':nome,
    'Descrição':descrição,
    'Prioridade':prioridade,
    'Categoria':categoria,
    'Situação':situação
    }

    tarefas.append(nova_tarefa)

def listar_tarefas():
    for tarefa in tarefas:
        print(f'''
               Tarefa:{tarefa['Nome']},
               Descrição:{tarefa['Descrição']}, 
               Prioridade:{tarefa['Prioridade']}, 
               Categoria:{tarefa['Categoria']},
               Situação:{tarefa['Situação']}''')

def tarefa_concluida():
    for i in range(len(tarefas)):
     if tarefas[i]['Situação']==False:
            print( f'{i}- {tarefas[i]['Nome']}')
    escolha_usuario= int(input('Digite o número correspondente a tarefa que deseja marcar como concluida: '))
    tarefas[escolha_usuario]['Situação']=True
    print (tarefas[escolha_usuario])      

def exibir_por_prioridade():
    escolha=int(input('Digite conforme a prioridade que deseja visualizar: 1=Pequena, 2=Média, 3=Grande:'))
    for tarefa in tarefas:
        if tarefa['Prioridade']==escolha:
            print(tarefa)

def exibir_por_catergoria():
    escolha=int(input('Digite conforme a categoria que deseja visualizar: 1=Pessoal, 2=Profissional, 3=Financeiro, 4=Lazer'))
    for tarefa in tarefas:
        if tarefa['Categoria']==escolha:
            print(tarefa)
            
   
# Menu de Comandos:
# Crie um menu de comandos de linha de comando que permita ao usuário interagir com o programa.

