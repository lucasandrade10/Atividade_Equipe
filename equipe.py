from aluno import aluno

class equipe:
    def __init__(self, projeto):

        self.projeto = projeto
        self.lista = []

    def getProjeto(self):
        return self.projeto

    def cadastarA(self,nome,cpf):
        l = aluno(nome,cpf)
        self.lista.append(l)

    def removerA(self,cpf):
        aluno = self.procurarA(cpf)
        if aluno == None:
            return
        else:
            self.lista.remove(aluno)
    def imprimir(self):
        for i in range(len(self.lista)):
            print '\nNome da equipe: %s ' % (self.getProjeto())
            print 'Aluno %s \ncpf: %i' % (self.lista[i].getNome(),self.lista[i].getCPF())

    def procurarA(self,cpf):
        for i in range(len(self.lista)):
            if self.lista[i].getCPF() == cpf:
                return self.lista[i]
        return None

