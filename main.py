from funcoes import adc_tarefas, listar_tarefas, tarefa_concluida, exibir_por_catergoria, exibir_por_prioridade

def menu_de_comando():
    while True:
        acao=int(input('''Digite o valor de acordo com a ação que deseja: 
                    1= Adicionar tarefa, 
                    2= Vizualisar as tarefas já inseridas
                    3= Marcar tarefa como concluida 
                    4= Exibir por prioridade escolhida 
                    5= Exibir por categoria escolhida
                    0= Encerrar o programa
                    Comando= '''))
        if acao==0:
            break
        elif acao==1:
            adc_tarefas()
        elif acao==2:
            listar_tarefas()
        elif acao==3:
            tarefa_concluida()
        elif acao==4:
            exibir_por_prioridade()
        elif acao==5:
            exibir_por_catergoria()
        else:
            print('Digite um número válido!')
         

menu_de_comando()