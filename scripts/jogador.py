from typing import List
from stringcolor import *


class Jogador:
    """Classe que permite instanciar o objeto do tipo jogador"""

    def __init__(self: object, nivel: int = 1,
                 vida: int = 10,
                 ataque: int = 1,
                 defesa: int = 1,
                 pocao: int = 1,
                 experiencia: int = 0):
        self.__nivel: int = nivel
        self.__vida: int = vida
        self.__ataque: int = ataque
        self.__defesa: int = defesa
        self.__pocao: int = pocao
        self.__experiencia: int = experiencia
        self.__mochila: List[str] = []
        self.__derrotados: int = 0
        self.__coletados: int = 0

    # ========================================= PROPERTYS ==============================================================
    @property
    def nivel(self: object):
        return self.__nivel

    @property
    def vida(self: object):
        return self.__vida

    @property
    def ataque(self: object):
        return self.__ataque

    @property
    def defesa(self: object):
        return self.__defesa

    @property
    def pocao(self: object):
        return self.__pocao

    @property
    def experiencia(self: object):
        return self.__experiencia

    @property
    def mochila(self: object):
        return self.__mochila

    @property
    def derrotados(self: object):
        return self.__derrotados

    @property
    def coletados(self: object):
        return self.__coletados

    # =========================================== STATUS ===============================================================
    def status(self: object):
        print(cs(f'\n---- SEUS STATUS ----\n', 'yellow').bold() +
              f'Nivel {self.nivel}\n'
              f'Experiencia {self.experiencia}/100\n'
              f'Vida: {self.vida}\n'
              f'Ataque: {self.ataque}\n'
              f'Defesa: {self.defesa}\n'
              f'Pots: {self.pocao}')

    # =========================================== MOCHILA ==============================================================
    def ver_mochila(self):
        print(cs('\n----- Mochila:', 'yellow').bold())
        for item in self.mochila:
            print(f'Item: {item.nome}')

    def adicionar_na_mochila(self: object, item):
        self.__mochila.append(item)

    # =========================================== NIVEL/EXPERIENCIA ====================================================
    def ganhar_xp(self, valor):
        self.__experiencia += valor

    def subir_nivel(self):
        self.__experiencia = 0
        self.__nivel += 1
        self.__vida = 10

    # =========================================== POTIONS ==============================================================

    def ganhar_pocao(self: object, ganho: int):
        self.__pocao += ganho

    def usar_pocao(self: object):
        if self.__pocao > 0:
            self.__pocao -= 1
            self.__vida += 2
            print('\nVocê usou uma POT e ' + cs('regenerou 2 pontos', 'green').bold() + ' de vida!')
            if self.__vida > 10:
                self.__vida = 10
        else:
            print('\nVocê não tem POTS')

    # =========================================== COMBATE ==============================================================

    def receber_dano(self: object, dano: int):
        self.__vida -= dano

    # =========================================== COLETAVEIS ===========================================================

    def aumenta_ataque(self: object, bonus):
        self.__ataque += bonus

    def aumenta_defesa(self: object, bonus):
        self.__defesa += bonus

    def derrotar(self):
        self.__derrotados += 1

    def coletar(self):
        self.__coletados += 1

# ================================================ MENUS ===============================================================


def inicio():
    print('Digite ' + cs('INICIAR', '#7FFF00').bold() + ' para iniciar sua jornada\n')


def instrucao():
    print(cs('\n---- (COMANDOS)\n', 'yellow') +
          'Digite' + cs(' STATUS ', 'yellow') + 'para verificar seus status.\n'
          'Digite' + cs(' MOCHILA ', 'yellow') + 'para verificar sua mochila.\n'
          'Digite' + cs(' POT ', 'yellow') + ' para usar poção\n')


def continuar():
    print('\n1)' + bold(' CONTINUAR') + '\n' +
          '2) VER' + bold(' COMANDOS') + '\n' +
          '3) FINALIZAR PARTIDA\n')

# =========================================== INSTANCIA O JOGADOR ======================================================


personagem = Jogador()