import random

def inicializar_alunos():
    return []

def escolher_aluno(alunos):
    if len(alunos) == 0:
        return None
    return random.choice(alunos)

def imprimir_grupo(numero, alunos):
    print()
    print("----")
    print("O grupo", numero, "é composto por:")
    print("----")
    print()
    for i in range(len(alunos)):
        print(alunos[i])

def formar_grupos(alunos, tamanho, num_grupos):
    grupo = []
    for i in range(num_grupos):
        for j in range(tamanho):
            aluno = escolher_aluno(alunos)
            grupo.append(aluno)
            if aluno is None:
                break
            alunos.remove(aluno)
        if len(grupo) == tamanho:
            imprimir_grupo(i+1, grupo)
            grupo = []

alunos = inicializar_alunos()

while True:
    nome = input("Digite o nome do aluno para coloca-lo a lista, e quando terminar digite 'fim': ")
    if nome.lower() == "fim"or"Fim":
        break
    alunos.append(nome)

formar_grupos(alunos, 4, 7)