'''
classes
- ultilizados para agrupar dados e funçoes, podendo reutilizar
- objetos sao dentro de uma classe (instancia)
'''

class Funcionarios:

    def __init__(self, nome, sobrenome, documento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.documento = documento

#criar objeto
usuario1 = Funcionarios("Amanda", "Reis", "4545454")
usuario2 = Funcionarios("Gabriel", "Furtado","44449787")

print(usuario1.nome)
