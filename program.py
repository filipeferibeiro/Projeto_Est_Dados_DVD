from functions import *
import os, time

Locadora = BST()
LDE = "Locadora de Estrutura\n"

print(LDE)
login = input("Login: ")
os.system("cls")
print(LDE)
senha = input("Senha: ")

Locadora.get_from_file()

while True:
    cond1 = True
    while cond1 == True:
        os.system("cls")
        print(LDE)
        print("Escolha uma opção:\n"
              "1 - Buscar filme\n"
              "2 - Listar todos os filmes\n"
              "3 - Adicionar filme\n"
              "4 - Remover filme\n"
              "5 - Alugar filme\n"
              "6 - Devolver filme\n"
              "7 - Sair\n")
        try:
            option = int(input())
            cond1 = False
        except ValueError:
            os.system("cls")
            print(LDE, "\nPor favor, escolha algo válido.")
            time.sleep(3)

    if option == 1: #Search movie
        os.system("cls")
        print(LDE)
        cond2 = True
        while cond2 == True:
            try:
                os.system("cls")
                print(LDE)
                type_search = int(input("Buscar filme:\n1 - Por código\n2 - Por nome\n3 - Por gênero\n4 - Voltar\n\n"))
                cond2 = False
                cond3 = True
                while cond3 == True:
                    try:
                        os.system("cls")
                        print(LDE)
                        if type_search == 1:
                            data = int(input("Código: "))
                        elif type_search == 2:
                            data = input("Nome: ").lower()
                        elif type_search == 3:
                            data = input("Gênero: ").lower()
                        elif type_search == 4:
                            cond1 = True
                            break
                        if data != "":
                            cond3 = False
                        else:
                            cond3 = True
                            os.system("cls")
                            print(LDE, "\nPor favor, informe o termo de pesquisa desejado.")
                            time.sleep(3)
                    except:
                        cond3 = True
                        os.system("cls")
                        print(LDE, "\nPor favor, informe algo válido.")
                        time.sleep(3)
                if type_search == 1 or type_search == 2: #Search movie by Code or Name
                    if Locadora.search(type_search, str(data)) is not None:
                        a, b, c, d, e = Locadora.search(type_search, data)
                        os.system("cls")
                        print(LDE)
                        print("Código do DVD:", a, "\nNome do filme:", b, "\nGênero:", c, "\nSituação:", d,
                              "\nValor do aluguel: R$", e, "\n")
                        input("Pressione enter para continuar.")
                        cond1 = True
                    else:
                        os.system("cls")
                        print(LDE, "\nNão foram encontrador filmes com o termo de pesquisa informado.")
                        time.sleep(3)
                        cond2 = True
                if type_search == 3: #Search movie by Gender
                    if Locadora.search(type_search, str(data)) == None:
                        os.system("cls")
                        print(LDE, "\nFilme não encontrado.")
                        time.sleep(3)
                        cond2 = True
                    else:
                        input("Pressione enter para continuar")
                elif type_search == 4: #To back in menu
                    cond1 = True
                    break
                else:
                    os.system("cls")
                    print(LDE, "\nPor favor, escolha algo válido.")
                    time.sleep(3)
                    cond2 = True
            except ValueError:
                os.system("cls")
                print(LDE, "\nPor favor, escolha algo válido.")
                time.sleep(3)
                cond2 = True

    elif option == 2: #List all movies
        os.system("cls")
        print(LDE)
        print("Total de filmes:", Locadora.get_total_nodes())
        print("--------------------------------------------------------------------------------------")
        Locadora.inOrderTraversal()
        input("Pressione enter para continuar.")

    elif option == 3: #Add movie
        cond4 = True
        cond5 = True
        cond6 = True
        while cond4 == True:
            while cond5 == True:
                try:
                    os.system("cls")
                    print(LDE)
                    code = int(input("Código: "))
                    cond5 = False
                except:
                    os.system("cls")
                    print(LDE, "\nPor favor, informe algo válido.")
                    time.sleep(3)
                    cond5 = True
            name = ""
            while name == "":
                os.system("cls")
                print(LDE)
                name = input("Nome: ").lower()
                if name == "":
                    os.system("cls")
                    print(LDE, "\nPor favor, informe o nome do filme.")
                    time.sleep(3)
            gender = ""
            while gender == "":
                os.system("cls")
                print(LDE)
                gender = input("Gênero: ").lower()
                if gender == "":
                    os.system("cls")
                    print(LDE, "\nPor favor, informe o gênero do filme.")
                    time.sleep(3)
            while cond6 == True:
                try:
                    os.system("cls")
                    print(LDE)
                    value = float(input("Valor: "))
                    cond6 = False
                except:
                    os.system("cls")
                    print(LDE, "\nPor favor, informe algo válido.")
                    time.sleep(3)
                    cond4 = True
            cond4 = False
        Locadora.insert(code, name, gender, "disponível", value)
        cond1 = True
        os.system("cls")
        print(LDE)
        file = open("locadora.txt", "a")
        file.write("Código do DVD: " + str(code))
        file.write("\nNome do filme: " + str(name))
        file.write("\nGênero: " + str(gender))
        file.write("\nSituação: " + "disponível")
        file.write("\nValor do aluguel: R$" + str(value))
        file.write("\n-------------------------------\n")
        file.close()
        print("Filme adicionado.")
        time.sleep(2)

    elif option == 4: #Remove movie
        os.system("cls")
        print(LDE)
        cond5 = True
        while cond5 == True:
            try:
                os.system("cls")
                print(LDE)
                type_search = int(input("Remover filme:\n1 - Por código\n2 - Por nome\n3 - Voltar\n\n"))
                cond5 = False
                os.system("cls")
                print(LDE)
                if type_search == 1: #Remove movie by Code
                    data = int(input("Código: "))
                elif type_search == 2: #Remove movie by Name
                    data = input("Nome: ").lower()
                    print(data)
                elif type_search == 3: #To back in menu
                    cond1 = True
                    break
                if type_search == 1 or type_search == 2:
                    if Locadora.search(type_search, str(data)) is not None:
                        a, b, c, d, e = Locadora.search(type_search, data)
                        os.system("cls")
                        print(LDE)
                        Locadora.remove_node(a)
                        Locadora.modify_file()
                        print("Filme removido.")
                        time.sleep(3)
                        cond1 = True
                    else:
                        os.system("cls")
                        print(LDE, "\nFilme não encontrado.")
                        time.sleep(3)
                        cond5 = True
                else:
                    os.system("cls")
                    print(LDE, "\nPor favor, escolha algo válido.")
                    time.sleep(3)
                    cond5 = True
            except ValueError:
                os.system("cls")
                print(LDE, "\nPor favor, escolha algo válido.")
                time.sleep(3)
                cond5 = True

    elif option == 5: #Rent movie
        os.system("cls")
        print(LDE)
        cond3 = True
        while cond3 == True:
            try:
                os.system("cls")
                print(LDE)
                type_search = int(input("Alugar filme:\n1 - Por código\n2 - Por nome\n3 - Voltar\n\n"))
                cond3 = False
                os.system("cls")
                print(LDE)
                if type_search == 1:
                    data = int(input("Código: "))
                elif type_search == 2:
                    data = input("Nome: ").lower()
                elif type_search == 3: #To back in menu
                    cond1 = True
                    break
                if type_search == 1 or type_search == 2: #Rent movie by Code or Name
                    if Locadora.rent(type_search, str(data)) == True:
                        os.system("cls")
                        print(LDE)
                        Locadora.modify_file()
                        print("Aluguel de filme efetuado.")
                        time.sleep(3)
                        cond1 = True
                    elif Locadora.rent(type_search, str(data)) == False:
                        os.system("cls")
                        print(LDE)
                        print("Este filme já está alugado.")
                        time.sleep(3)
                        cond1 = True
                    else:
                        os.system("cls")
                        print(LDE, "\nEste filme não está no catálogo.")
                        time.sleep(3)
                        cond3 = True
                else:
                    os.system("cls")
                    print(LDE, "\nPor favor, escolha algo válido.")
                    time.sleep(3)
                    cond3 = True
            except ValueError:
                os.system("cls")
                print(LDE, "\nPor favor, escolha algo válido.")
                time.sleep(3)
                cond3 = True

    elif option == 6: #Return movie
        os.system("cls")
        print(LDE)
        cond4 = True
        while cond4 == True:
            try:
                os.system("cls")
                print(LDE)
                type_search = int(input("Devolver filme:\n1 - Por código\n2 - Por nome\n3 - Voltar\n\n"))
                cond4 = False
                os.system("cls")
                print(LDE)
                if type_search == 1:
                    data = int(input("Código: "))
                elif type_search == 2:
                    data = input("Nome: ").lower()
                    print(data)
                elif type_search == 3: #To back in menu
                    cond1 = True
                    break
                if type_search == 1 or type_search == 2: #Return movie by Code or Name
                    if Locadora.give_back_movie(type_search, str(data)) == True:
                        os.system("cls")
                        print(LDE)
                        Locadora.modify_file()
                        print("Devolução efetuada.")
                        time.sleep(3)
                        cond1 = True
                    elif Locadora.give_back_movie(type_search, str(data)) == False:
                        os.system("cls")
                        print(LDE)
                        print("Este filme já está disponível.")
                        time.sleep(3)
                        cond1 = True
                    else:
                        os.system("cls")
                        print(LDE, "\nEste filme não está no catálogo.")
                        time.sleep(3)
                        cond4 = True
                else:
                    os.system("cls")
                    print(LDE, "\nPor favor, escolha algo válido.")
                    time.sleep(3)
                    cond4 = True
            except ValueError:
                os.system("cls")
                print(LDE, "\nPor favor, escolha algo válido.")
                time.sleep(3)
                cond4 = True

    elif option == 7: #Exit
        break
