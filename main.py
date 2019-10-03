from aluno import Aluno


aluno = Aluno()

menu=True

while menu:
    op=int(input("1- cadastrar\n"
                 "2- alterar\n"
                 "3- deletar\n"
                 "4- ler\n"
                 "5- sair\n"
                 "opção: "))

    if op==1:

        nome = input("digite o nome do aluno: ")
        sobrenome = input("digite o sobrenome do aluno: ")
        curso = input("digite o curso do aluno {0} {1}: ".format(nome, sobrenome))

        aluno.save(nome,sobrenome,curso)

    elif op==2:

        procura=input("digite o nome do aluno que se deseja atualizar: ")
        nome = input("digite o nome do aluno: ")
        sobrenome = input("digite o sobrenome do aluno: ")
        curso = input("digite o curso do aluno {0} {1}: ".format(nome, sobrenome))

        aluno.att(procura, nome, sobrenome, curso)

    elif op==3:
        find = input("digite o nome da pessoa que deseja deletar o resgistro: ")

        aluno.deleta(find)

    elif op==4:
        acha=input("digite o nome que se deja ver: ")
        aluno.ler(acha)

    elif op==5:
        menu=False