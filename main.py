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
    ["organismos da fauna e da flora interagindo entre si", "Vegetação densa e perene", "interação entre indivíduos", "Precipitação", "Erosão e formação do solo", "Assimilação", "", "", "", ""],
    ["comunidades biológicas", "Bioma mais degradado", "", "", "", "", "", "", "", "", ""],["conjunto de diferentes ecossistemas", "Vegetação com ou sem Araucária", "", "", "", "", "", "", "", ""]]

print(Perguntas().perguntas[1][0])