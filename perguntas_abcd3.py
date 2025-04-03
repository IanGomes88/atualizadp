
# editar campo de "1" e "2" colocar para campo de "Sim" e "Nao"
import os

senha=[]
justificativa = []
arquivo_usuarios= "usuarios.txt" #Arquivo onde estarão usuários e senhas


#função para cadastro de usuário
def cadastrar_usuario():
    mudid = input("Cadastre seu MudID: ")
    senha = input("Cadastre sua senha: ")

        # Verifica se o usuário já existe          #estava escrito "verificar_usuario" não leu... então vou substituir pelo nome do arquivo.
   # if senha_armazenada(mudid):
   #     print("MudID já cadastrado!")
   #     return
    # Abre o arquivo no modo de adição e salva o login e senha
    with open(arquivo_usuarios, "a") as arquivo:
        arquivo.write(f"{mudid},{senha}\n")
    print("Usuário cadastrado com sucesso!\n")

    # Função para verificar se o login e senha estão corretos
def fazer_login():
    mudid = input("Digite seu MudID: ")
    senha = input("Digite sua senha: ")
    # Abre o arquivo e verifica se o login e senha estão corretos
    with open(arquivo_usuarios, "r") as arquivo:
        for linha in arquivo:
            usuario, senha_armazenada = linha.strip().split(",")  # Separa login e senha
            if mudid == usuario and senha == senha_armazenada:
                print("Login realizado com sucesso!\n")
                return True
                justificativa.append(mudid)
    print("Login ou senha incorretos!\n")
    return False


# Menu principal
while True:
        print("1. Cadastrar seu MudID")
        print("2. Fazer login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            fazer_login()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


ehs=("Houve ocorrência de EHS?")
resposta=input("Houve ocorrência de EHS?\n 1 - Sim\n 2 - Não\n")
if resposta == "1":
    positivo= input("Qual foi a ocorrência?\n")
    justificativa.append(ehs)
    justificativa.append(positivo)
    

qualidade=("Houve ocorrência de Qualidade?")
resposta=input("Houve ocorrência de Qualidade?\n 1 - Sim\n 2 - Não\n")
if resposta == "1":
    positivo= input("Qual foi a ocorrência?\n")
    justificativa.append(qualidade)
    justificativa.append(positivo)
    

empilhadeira=("Foi realizado o Checklist nas Empilhadeiras?")
resposta=input("Foi realizado o Checklist nas Empilhadeiras?\n 1 - Sim\n 2 - Não\n")
if resposta == "1":
    positivo= input("Necessário carregar ou resisão/manutenção?\n")
    justificativa.append(empilhadeira)
    justificativa.append(positivo)
    
elif resposta == "2":
    negativo= input("Porque não foi realizado o Checklist nas Empilhadeiras?\n")
    justificativa.append(empilhadeira)
    justificativa.append(negativo)
    

resposta=input("Estamos em Campanha?\n 1 - Sim\n 2 - Não\n")
if resposta == "1":

    #Se for 1 seguiremos com o código, se for 2 iremos para fora de campanha que é o momento de limpar o setor

    safety=("Foi realizado o Checklist de Safety Startup?")
    resposta=input("Foi realizado o Checklist de Safety Startup?\n 1 - Sim\n 2 - Não\n")
    if resposta == "1":
        positivo= input("Alguma falha durante o teste?\n")
        justificativa.append(safety)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= input("Porque não foi realizado o Checklist de Safety Startup?\n")
        justificativa.append(safety)
        justificativa.append(negativo)

    quebraajuste=("Houve quebra ou ajuste significativo em equipamento?")
    resposta=input("Houve quebra ou ajuste significativo em equipamento?\n 1 - Sim\n 2 - Não\n")
    if resposta == "1":
        positivo= input("Conte de forma direta o que ocorreu e quais as medidas tomadas, adicione também o tempo estimado em cada atividade e se foi necessário abertura de ACR:\n")
        justificativa.append(quebraajuste)
        justificativa.append(positivo)

    estacao1=("bulk alocado na Estação 1?")
    resposta=input("Bulk alocado na Estação 1?\n 1 - Sim\n 2 - Não\n 3 - Não aplicavel\n")
    if resposta == "1":
        positivo= input("Qual o número do bulk?\n")
        justificativa.append(estacao1)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= input("Porque não temos bulk alocado na Estação 1?\n")
        justificativa.append(estacao1)
        justificativa.append(negativo)
        
    elif resposta == "3":
        print("Não aplicável")

    estacao2=("bulk alocado na Estação 2?")
    resposta=input("Bulk alocado na Estação 2?\n 1 - Sim\n 2 - Não\n 3 - Não aplicavel\n")
    if resposta == "1":
        positivo= input("Qual o número do bulk?\n")
        justificativa.append(estacao2)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= input("Porque não temos bulk alocado na Estação 2?\n")
        justificativa.append(estacao2)
        justificativa.append(negativo)
        
    elif resposta == "3":
        print("Não aplicável")

    bulksdefora=("Quantos Bulk de fora?")
    positivo= input("Quantos Bulk de fora?\n")
    justificativa.append(bulksdefora)
    justificativa.append(positivo)

    pedirbulk=("Necessário pedir bulk?")
    resposta=input("Necessário pedir bulk?\n 1 - Sim\n 2 - Não\n")
    if resposta == "1":
        positivo= input("Foi solicitado o bulk para que horas?\n")
        justificativa.append(pedirbulk)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= print("NÃO\n")
        justificativa.append(pedirbulk)
        justificativa.append(negativo)

    carbonatos=("Quantos carbonatos fabricados e quantos aprovados?")
    positivo= input("Quantos carbonatos fabricados e quantos aprovados?\n")
    justificativa.append(carbonatos)
    justificativa.append(positivo)

    pedircarbonato=("Necessário pedir Carbonato?")
    resposta=input("Necessário pedir Carbonato?\n 1 - Sim\n 2 - Não\n")
    if resposta == "1":
        positivo= input("Foi solicitado o Carbonato para que horas?\n")
        justificativa.append(pedircarbonato)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= print("NÃO\n")
        justificativa.append(pedircarbonato)
        justificativa.append(negativo)

    bulksfabriados=("Quantos Bulk fabricados no turno?")
    positivo= input("Quantos Bulk fabricados no turno?\n")
    justificativa.append(bulksfabriados)
    justificativa.append(positivo)

    carbonatosecamos=("Quantos Carbonatos Secamos no turno?\n")
    positivo=input("Quantos Carbonatos Secamos no turno?\n")
    justificativa.append(carbonatosecamos)
    justificativa.append(positivo)

    processos=("Processos em andamento durante a passagem de turno?")
    resposta=input("Processos em andamento durante a passagem de turno?\n 1 - Sim\n 2 - Não\n")
    if resposta == "1":
        positivo= input("Quais processos estão em andamento?\n")
        justificativa.append(processos)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= print("NÃO\n")
        justificativa.append(processos)
        justificativa.append(negativo)
    pendencias=("Pendências no SAP?")
    resposta=input("Pendências no SAP?\n 1 - Sim\n 2 - Não\n")
    if resposta == "1":
        positivo= input("Quais pendências no SAP?\n")
        justificativa.append(pendencias)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= print("NÃO\n")
        justificativa.append(pendencias)
        justificativa.append(negativo)
    pasx=("Pendências no sistema de PASX?")
    resposta=input("Pendências no sistema de PASX?\n 1 - Sim\n 2 - Não\n")
    if resposta == "1":
        positivo= input("Quais pendências no sistema de PASX?\n")
        justificativa.append(pasx)
        justificativa.append(positivo)
        
    elif resposta == "2":
        negativo= print("NÃO\n")
        justificativa.append(pasx)
        justificativa.append(negativo)

print(justificativa)

# editar campo de "1" e "2" colocar para campo de "Sim" e "Nao"