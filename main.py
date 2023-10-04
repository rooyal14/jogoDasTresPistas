import time
import os

#Listas, resposta na posição [i][0]
perguntas = [["Bioma", "Organismos da fauna e da flora interagindo entre si", "Comunidades biológicas", "Conjunto de diferentes ecossistemas"],
             ["Mata Atlantica", "Vegetação densa e perene", " Bioma mais degradado", "Vegetação com ou sem Araucária"],
             ["Sociedade", "interação entre indivíduos", "mesma espécie", "organizados em castas"],
             ["Ciclo da Água", "Precipitação", "Evaporação", "Condensação"], 
             ["Ciclo do Fósforo", "Erosão e formação do solo", "Assimilação", "Identificado como P na tabela periódica"],
             ["Inversão Térmica", "Poluição não se dissipa", "Ocorre em dias frios", "cortina de fuligem impede a passagem de raios solares"],
             ["Pegada de Carbono", "Gerado ao longo do ciclo de vida de um produto", "Contém as emissões totais (diretas e indiretas)", "Gases de Efeito Estufa"],
             ["Efeito Estufa", "Retenção de Raios Solares", "Tem relação com combustíveis fósseis", "Concentração de gases poluentes na Atmosfera"],
             ["Eutrofização da água", "Excesso de nutrientes na água", "Fitoplâncton se prolifera absurdamente rápido", "Bactérias consomem o O2 causando a morte de animais e protozoários (peixes e zooplâncton)"],
             ["Decompositores", "Podem atuar em vários níveis tróficos", "Reciclam Matéria Orgânica", "Devolvem nutrientes aos produtores, que estão no primeiro nível trófico"]]
listaNumerosUsados = []
PerguntasIndividuais = []

# Funções
def verificar_resposta(resposta, palavra_correta):
    os.system('cls' if os.name=='nt' else 'clear')
    if resposta.lower() == palavra_correta.lower():
        print("     .")
        print("")
        time.sleep(1)
        print("     .")
        print("")
        time.sleep(1)
        print("     .")
        print("")
        print("   Acertou !     ")
        print("")
        print("")
        time.sleep(2)
        return True
    else:
        print("     .")
        print("")
        time.sleep(1)
        print("     .")
        print("")
        time.sleep(1)
        print("     .")
        print("")
        print("   Errado !     ")
        print("")
        print("")
        time.sleep(2)
        return False
    
def mostrar_pontos(pontosTimeUm, pontosTimeDois, plateia):
    if time == 1:
        print(f"Time 1: {pontosTimeUm} pontos")
    elif time == 2:
        print(f"Time 2: {pontosTimeDois} pontos")
    else:
        print(f"Plateia: {plateia} pontos")

def pontos_do_nivel_pergunta(estado, nivel_da_dica):
    if(estado is True and nivel_da_dica == 1): 
        return  30
    
    if(estado is True and nivel_da_dica == 2):
        return 20
    
    if(estado is True and nivel_da_dica == 3):
        return 10
    else:
        return 0
    
def mudanca_time(time):
    if time == 1 :
        return 2
    elif time == 2:
        return 1

#variaveis 
pontos_Time_Um = 0
pontos_Time_Dois = 0
plateia = 0
enquanto = True

#Inicio do jogo
os.system('cls' if os.name=='nt' else 'clear')
print( "--------------------- JOGO DAS TRÊS PISTAS ------------------------")
time.sleep(1)
print(".")
print()
time.sleep(1)
print(".")
print("")
time.sleep(1)
print(".")
print("")
time.sleep(2)

os.system('cls' if os.name=='nt' else 'clear')
print("-----------------------START !---------------------")
print("")
print("1 - Time Um | 2 - Time Dois        ")
print()
time_atual = int(input("Defina o time inicial: "))


#Loop principal

while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print()
    print(f"--------- Time {time_atual} ----------")
    print()
    escolha_pergunta = int(input("Número do cartão: "))+1
    time.sleep(2)
    os.system('cls' if os.name=='nt' else 'clear')
    if(escolha_pergunta in listaNumerosUsados):
        time.sleep(1)
        print(".")
        print()
        time.sleep(1)
        print(".")
        print("")
        time.sleep(1)
        print(".")
        print("")
        time.sleep(2)
        
        print("Não é possível repetir o cartão, escolha outro número:")
        continue
    
    else:
        listaNumerosUsados.append(escolha_pergunta)

    # Loop para apresentar dicas e coletar respostas
    for j in range(4):
        if j != 0:
            PerguntasIndividuais.append(perguntas[escolha_pergunta][j])
            print("")
            print(" ---------- Dica ---------- ")
            print("")
            print(" | ".join(PerguntasIndividuais))
            print("")
            resposta = input("Insira sua resposta:")

            # Chama a função para verificar a resposta
            resultado = verificar_resposta(resposta, perguntas[escolha_pergunta][0])
            if(time_atual == 1):
                pontos_Time_Um += pontos_do_nivel_pergunta(resultado, j)
               

            else:
               pontos_Time_Dois += pontos_do_nivel_pergunta(resultado, j)


            if resultado:
                print(f"Placar: Time 1 - {pontos_Time_Um} pontos | Time 2 - {pontos_Time_Dois} pontos | Plateia - {plateia} pontos")
                input()
                break

            if not resultado and j == 3:
                while True:
                    print()
                    resposta_plateia = input("Plateia, qual a sua resposta: ")
                    resultado_plateia = verificar_resposta(resposta_plateia, perguntas[escolha_pergunta][0])
                    time_atual = mudanca_time(time_atual)
                    plateia += pontos_do_nivel_pergunta(resultado_plateia, j)
                    if(resultado_plateia):
                        break
            else:
                enquanto = False
                time_atual = mudanca_time(time_atual)
                os.system('cls' if os.name=='nt' else 'clear')
                print(f"------ Quem vai responder é o time {time_atual}: -------   ")
                print()
            #print(f"Placar: Time 1 - {pontos_Time_Um} pontos | Time 2 - {pontos_Time_Dois} pontos | Plateia - {plateia} pontos")
    PerguntasIndividuais = []
                
    if pontos_Time_Um >= 100 or pontos_Time_Dois >= 100 or plateia >= 100:
        break


mostrar_pontos(pontos_Time_Um,pontos_Time_Dois,plateia)
