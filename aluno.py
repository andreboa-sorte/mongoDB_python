from pymongo import MongoClient

from conexao import MongoConnect

class Aluno():

    conexao = None

    def __init__(self):
        self.conexao = MongoConnect()

    def save(self, nome, sobrenome, curso):

        aluno = {'nome': nome, 'sobrenome': sobrenome, 'curso': curso}
        self.conexao.save(aluno)

    def att(self, procura, nome, sobrenome, curso):
        aluno = {'nome': nome, 'sobrenome': sobrenome, 'curso': curso}
        self.conexao.att({"nome": procura}, {"$set": aluno})

    def deleta(self, find):
        self.conexao.deleta({"nome": find})

    def ler(self, acha):
        self.conexao.ler({"nome":acha},{"_id":0})


