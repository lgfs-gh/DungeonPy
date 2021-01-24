""" ITEMS """

from random import choice, randint


class Item:

    def __init__(self: object, nome: str):
        self.__nome: str = nome

    @property
    def nome(self: object):
        return self.__nome


class Ataque(Item):
    def __init__(self: object, nome: str, ataque: int):
        super().__init__(nome)
        self.__ataque: int = ataque


class Defesa(Item):
    def __init__(self: object, nome: str, defesa: int):
        super().__init__(nome)
        self.__defesa: int = defesa

# ========================================== INSTANCIA UM OBJETO DO TIPO ITEM ==========================================


def gera_item():
    nomes_atq = ['Anel',
                 'Amuleto',
                 'Cordao',
                 'Faca',
                 'Espada',
                 'Machado']
    nomes_def = ['Anel',
                 'Amuleto',
                 'Cordao',
                 'Escudo',
                 'Armadura',
                 'Capacete']
    nomes_att = ['do Dragão',
                 'do Sangue',
                 'das Sombras',
                 'Infernal',
                 'Sombrio',
                 'Divino',
                 'Sábio',
                 'Colossal',
                 'Abismal',
                 'do Aprendiz',
                 'dos Reis',
                 'Enfeitiçado',
                 'das Almas'
                 ]

    defesa_ou_ataque = randint(1,2)

    # =========================================== CHECA SE O ITEM GERADO É DE DEFESA OU ATAQUE
    # ========================================== ATRIBUI NOME AO ITEM
    # ========================================== ATENÇÃO! ATRIBUTOS DEFESA E ATAQUE EM DESUSO
    if defesa_ou_ataque == 1:
        nome_completo = f'{choice(nomes_def)} {choice(nomes_att)} | (DEF +1)'
        item = Defesa(nome=nome_completo, defesa=1)
        return item
    else:
        nome_completo = f'{choice(nomes_atq)} {choice(nomes_att)} | (ATQ +1)'
        item = Ataque(nome=nome_completo, ataque=1)
        return item
