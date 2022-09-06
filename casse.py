'''
classes
- ultilizados para agrupar dados e funçoes, podendo reutilizar
- objetos sao dentro de uma classe (instancia)
'''

from datetime import datetime
class Funcionarios:

    def __init__(self, nome, sobrenome, documento, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.documento = documento
        self.ano_nascimento = ano_nascimento
    

    def nome_completo(self):
        return self.nome + " " + self.sobrenome
        
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        idade_funcionario = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


#criar objeto
usuario1 = Funcionarios("Amanda", "Reis", "4545454", 1990)
usuario2 = Funcionarios("Gabriel", "Furtado","44449787", 2018)

print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.documento(usuario1))

