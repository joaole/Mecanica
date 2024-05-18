from entidade.modelo import Modelo

class CotroladorModelo:
    def __init__(self):
        self.__modelos = []

    def incluir_modelo(self, nome, quantidade_oleo, codigo):
        novo_modelo = Modelo(nome, quantidade_oleo, codigo)
        for modelo in self.__modelos:
            if modelo.codigo == novo_modelo.codigo:
                return None
        else:
            self.__modelos.append(novo_modelo)
            return novo_modelo

    def excluir_modelo(self, codigo):
        for modelo in self.__modelos:
            if modelo.codigo == codigo:
                self.__modelos.remove(modelo)
                return codigo
        else:
            return None

    def alterar_nome_modelo(self, nome, codigo):
        for modelo in self.__modelos:
            if modelo.codigo == codigo:
                modelo.nome = nome
                return modelo.nome

        else:
            return None

    def alterar_quantidade_oleo_modelo(self, quantidade_oleo, codigo):
        for modelo in self.__modelos:
            if modelo.codigo == codigo:
                modelo.quantidade_oleo = codigo
                return modelo.quantidade_oleo

    def alterar_codigo_modelo(self,novo_codigo, codigo):
        for modelo in self.__modelos:
            if modelo.codigo == codigo:
                modelo.codigo = novo_codigo
                return modelo.codigo

        else:
            return None
