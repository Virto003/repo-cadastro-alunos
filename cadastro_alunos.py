import json

try:
    with open('alunos.json', 'r') as f:
        alunos = json.load(f)
except FileNotFoundError:
    alunos = []

def salvar_alunos():
    with open('alunos.json', 'w') as f:
        json.dump(alunos, f, indent=4)

while True:
    print("\n*** Cadastro de Alunos ***")
    print("1. Registrar aluno")
    print("2. Consultar aluno")
    print("3. Atualizar cadastro de aluno")
    print("4. Excluir cadastro de aluno")
    print("5. Sair do sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        matricula = int(input("Digite a matrícula do aluno: "))
        curso = input("Digite o curso do aluno: ")

        cadastro = {
            "nome": nome,
            "idade": idade,
            "matricula": matricula,
            "curso": curso
        }

        alunos.append(cadastro)
        salvar_alunos()
        print(f"O aluno(a), {nome} da matrícula {matricula} foi cadastrado com sucesso.")

    elif opcao == "2":
        matricula = int(input("Digite a matrícula do aluno que você deseja consultar: "))
        aluno_encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                resultado_nome = aluno["nome"]
                resultado_idade = aluno["idade"]
                resultado_curso = aluno["curso"]
                print(f"O aluno está cadastrado.\nNome: {resultado_nome}\nIdade: {resultado_idade}\nCurso: {resultado_curso}")
                aluno_encontrado = True
                break

        if not aluno_encontrado:
            print("O aluno não está cadastrado.")

    elif opcao == "3":
        matricula = int(input("Digite a matrícula do aluno que você deseja editar: "))
        aluno_encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                aluno_encontrado = True
                print(f"Você está editando o aluno: {aluno['nome']}")
                nome = input("Digite o novo nome do aluno (deixe em branco para não alterar): ")
                idade = input("Digite a nova idade do aluno (deixe em branco para não alterar): ")
                curso = input("Digite o novo curso do aluno (deixe em branco para não alterar): ")

                if nome:
                    aluno['nome'] = nome
                if idade:
                    aluno['idade'] = int(idade) if idade.isdigit() else aluno['idade']
                if curso:
                    aluno['curso'] = curso

                salvar_alunos()
                print("Cadastro de aluno atualizado com sucesso!")
                break

        if not aluno_encontrado:
            print("O aluno não está cadastrado.")

    elif opcao == "4":
        matricula = int(input("Digite a matrícula do aluno que você deseja excluir: "))
        aluno_encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                aluno_encontrado = True
                resultado_nome = aluno["nome"]
                resultado_idade = aluno["idade"]
                resultado_curso = aluno["curso"]
                confirmacao = input(f"Você tem certeza que deseja excluir o aluno com os seguintes dados?\nNome: {resultado_nome}\nIdade: {resultado_idade}\nCurso: {resultado_curso}\n(s/n): ")
                if confirmacao.lower() == "s":
                    alunos.remove(aluno)
                    salvar_alunos()
                    print("Aluno removido com sucesso")
                else:
                    print("Operação cancelada.")
                break

        if not aluno_encontrado:
            print("O aluno não está cadastrado.")

    elif opcao == "5":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida. Tente novamente.")
