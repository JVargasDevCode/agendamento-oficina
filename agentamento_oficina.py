fila_espera = []
trabalhos_mecanicos = []
mecanicos_disponiveis = ["Lucas", "Mateus", "Jose", "Eliel"]

def criar_agendamento(cliente, carro, ano, problema):
    ficha_cliente = f"Cliente: {cliente} | Carro: {carro} ({ano}) | Problema: {problema}"
    fila_espera.append(ficha_cliente)
    print (f'{carro} esta na lista de espera')

def atribuir_mecanico(nome_mecanico, indice_do_carro):
    if len(fila_espera) > 0 and indice_do_carro < len(fila_espera):
        carro_removido = fila_espera.pop(indice_do_carro)
        
        trabalho_atual = f"Mecânico: {nome_mecanico} {carro_removido}"
        trabalhos_mecanicos.append(trabalho_atual)
        print(f'Mecânico {nome_mecanico} começou a trabalhar no carro!')
    else:
        print ('Erro: Posição inválida ou fila de espera vazia')
    
while True:
    print ('------------- Agendamento Drides -------------\n')
    print ('1. Cadastra cliente.')
    print ('2. Atribuir carro ao Mecânico.')
    print ('3. Status da oficina.')
    print ('4. sair do sistema.')
    opcao = input('escolha uma destas opções: ')
    
    match opcao:
        case '1':
            print ('-------- Cadastro Cliente ----------\n')
            Cli = input("Digite seu nome: ")
            Car = input('Digite o modelo do carro: ')
            Ano = input('Digite o ano do carro: ')
            Prob = input('Qual o problema do carro?\n ')
            criar_agendamento(Cli, Car, Ano, Prob)
        case '2':
            print ('-------- Atribuir carro para o Mecânico --------')
            if len(fila_espera) == 0:
                print ('não nenhum carro na lista de espera ainda.')
            else:
                print(f'Mecânicos: {','.join(mecanicos_disponiveis)}!!!')
                print("-" * 30)
                print ("carro aguardando na fila")
                
                i = 0
                while i < len(fila_espera):
                  print(f"[{i}] {fila_espera[i]}")
                  i += 1
                  mec = input("\nNome do Mecânico: ")
                  num_carro = int(input("Digite o número do carro: "))
                  atribuir_mecanico(mec, num_carro)
        case '3':
            print("\n=== CARROS NA FILA DE ESPERA ===")
            if len(fila_espera) == 0:
                print("Vazia.")
            else:
                i = 0
                while i < len(fila_espera):
                    print(fila_espera[i])
                    i += 1
                    
            print("\n=== TRABALHOS COM OS MECÂNICOS ===")
            if len(trabalhos_mecanicos) == 0:
                print("Nenhum mecânico trabalhando no momento.")
            else:
                i = 0
                while i < len(trabalhos_mecanicos):
                    print(trabalhos_mecanicos[i])
                    i += 1
        case '4':
            print ('sistema esta sendo desligado')
            break
        case _:
            print ('\nOpção inválida! Digite um número de 1 a 4.')