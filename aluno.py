class aluno:
    def __init__(self, nome, CPF):
        self.nome = nome
        self.CPF = CPF

    def getNome(self):
        return self.nome

    def getCPF(self):
        return self.CPF

    def setNome(self, novoNome):
        self.nome = novoNome

    def setCPF(self, novoCPF):
        self.CPF = novoCPF