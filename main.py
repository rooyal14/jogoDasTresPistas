"""
Dividiremos a sala em três equipes, duas vão duelar e uma será a plateia(professor).

Especificar a forma de distribuição, procurar algo tecnológico para isso.

Construir o algoritmo com Switch Case, os participantes selecionam a pergunta e a gente abre na hora, digitando o número.

Ao selecionar a pergunta, conforme o usuário responde, o sistema passa as perguntas e atribui os pontos.

Acertou na primeira pista: 30 pontos
Acertou na segunda pista: 20 pontos
Acertou na terceira pista: 10 pontos

Quando vai para a plateia: 10 pontos

O sistema deve prever um placar ao finalizar as respostas. Exemplo. Perguntar em qual pista a questão foi solucionada e qual o time responsável.
"""

class Perguntas:
    perguntas = [["Bioma ", "Mata Atlântica", "Sociedade", "Ciclo da Água", "Ciclo do Fósforo", "Inversão Térmica", "Pegada de Carbono", "Efeito Estufa", "Eutrofização da água", "Decompositores"],
    ["Organismos da fauna e da flora interagindo entre si", "Vegetação densa e perene", "Interação entre indivíduos", "Precipitação", "Erosão e formação do solo", "Poluição não se dissipa", "Gerado ao longo do ciclo de vida de um produto", "Retenção de Raios Solares", "Excesso de nutrientes na água", "Podem atuar em vários níveis tróficos"],
    ["Comunidades biológicas", "Bioma mais degradado", "Mesma espécie", "Evaporação", "Assimilação", "Ocorre em dias frios", "Contém as emissões totais (diretas e indiretas)", "Tem relação com combustíveis fósseis", "Fitoplâncton se prolifera absurdamente rápido", "Reciclam Matéria Orgânica"],
    ["Conjunto de diferentes ecossistemas", "Vegetação com ou sem Araucária", "Organizados em castas ", "Condensação", "Identificado como P na tabela periódica.", "Cortina de fuligem impede a passagem de raios solares", "Gases de Efeito Estufa", "Concentração de gases poluentes na Atmosfera", "Bactérias consomem o O2 causando a morte de animais e protozoários (peixes e zooplâncton)", "Devolvem nutrientes aos produtores, que estão no primeiro nível trófico"]]

for i in range(10):
    bd = Perguntas()
    print("Pergunta Nº"+str(i+1))
    print(bd.perguntas[0][i])
    print(bd.perguntas[1][i])
    print(bd.perguntas[2][i])
    print(bd.perguntas[3][i])
    print()