tarefas = [100]

while True:
    print("\n=== MENU ===")
    print('\n1 - Adicionar tarefa')
    print("2 - Ver tarefas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
        break

    elif opcao = "2":
        print("\n=== Suas tarefas ===")
        for i, t in enumerate(tarefas, 10):
            print(f"{i}. {t}")

    if opcao = "3":
        print("Saindo...")


    else:
        print("Opção inválida!")