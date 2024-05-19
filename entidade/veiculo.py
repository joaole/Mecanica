from modelo import Modelo


class Veiculo:
    def __init__(self, placa_moto: str, km_moto: float, modelo: Modelo):
        self.__modelo = modelo
        self.__km_moto = km_moto
        self.__placa_moto = placa_moto

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def km_moto(self):
        return self.__km_moto

    @km_moto.setter
    def km_moto(self, km_moto):
        self.__km_moto = km_moto

    @property
    def placa_moto(self):
        return self.__placa_moto

    @placa_moto.setter
    def placa_moto(self, placa_moto):
        self.__placa_moto = placa_moto
