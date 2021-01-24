from random import randint, choice
from typing import List
from DungeonPy.scripts import items
from DungeonPy.scripts.jogador import personagem
from stringcolor import *


def jogar_dado(n: int) -> int:
    """Simula o jogar de dados,
    retornando um número semi-aleatório entre 1 e o parâmetro n inclusive"""
    dado = randint(1, n)
    return dado


def dificuldade():
    """Define a dificuldade da criatura que o jogador vai encontrar
    Retorna os pontos de ataque, vida, local, nome da criatura, experiência e chances de dar um item e poção"""
    dif: int = randint(1, 100)
# =========================================== DIFICULDADE: FÁCIL =======================================================
    if dif in range(1, 71):
        locais: List[str] = ['floresta', 'campo', 'caverna']
        monstros: List[str] = ['Aranha', 'Goblin', 'Lobo', 'Urso']
        max_dado = randint(2, 5)
        vida_gerada = randint(8, 10)
        xp_monstro = randint(20, 30)
        chance_premio = randint(75, 80)
        chance_pocao = randint(20, 25)
        return [locais, monstros, max_dado, vida_gerada, xp_monstro, chance_premio, chance_pocao]
# =========================================== DIFICULDADE: MÉDIA =======================================================
    if dif in range(81, 96):
        locais: List[str] = ['montanha', 'cemitério', 'vilarejo abandonado']
        monstros: List[str] = ['Ciclope', 'Esqueleto', 'Fantasma', 'Zumbi']
        max_dado = randint(3, 7)
        vida_gerada = randint(10, 15)
        xp_monstro = randint(30, 50)
        chance_premio = randint(60, 75)
        chance_pocao = randint(35, 45)
        return [locais, monstros, max_dado, vida_gerada, xp_monstro, chance_premio, chance_pocao]
# =========================================== DIFICULDADE: ALTA ========================================================
    if dif in range(96, 100):
        locais: List[str] = ['interior de um vulcão', 'topo de uma montanha', 'masmorra amaldiçoada']
        monstros: List[str] = ['Demônio', 'Dragão', 'Vampiro', 'Behemoth']
        max_dado = randint(9, 15)
        vida_gerada = randint(15, 20)
        xp_monstro = randint(80, 100)
        chance_premio = randint(40, 55)
        chance_pocao = randint(55, 65)
        return [locais, monstros, max_dado, vida_gerada, xp_monstro, chance_premio, chance_pocao]


def opcoes(local, monstro) -> int:
    """Imprime o local e a criatura que o jogador irá enfrentar e espera pelo INPUT do jogador
    Retorna a variavel o_opcao do tipo inteiro"""
    concluir = False
# =========================================== IMPRIME LOCAL/CRIATURA ===================================================
    print(cs(f'\n>>> Você está num(a) {local} e se depara com {monstro}! <<<\n', 'red').bold() +
          f'---- Opções:\n'
          f'1) Lutar\n'
          f'2) Fugir\n')
    while concluir is False:
        try:
            o_opcao = int(input('Escolha: '))
            if o_opcao == 1 or o_opcao == 2:
                return o_opcao
        except ValueError:
            o_opcao = 1
            return o_opcao


def checa_opcao(c_opcao, c_monstro, c_max_dado, c_vida_gerada, c_xp_monstro, c_chance_premio, c_chance_pocao):
    """Checa se o jogador escolheu lutar ou não conseguiu fugir
    Gera a criatura e o sistema de batalha"""
    apanhado = False
# ------------------------------ FUGA: CASO O JOGADOR ESCOLHA FUGIR ----------------------------------------------------
    if c_opcao == 2:
        sucesso = randint(1, 100)
        if sucesso in range(1, 61):
            print(cs('\n### Você foge com sucesso! ###', 'green'))
        else:
            print(cs(f'\n>>> Você foi apanhado por {c_monstro} <<<', 'red'))
            apanhado = True
# ================================= BATALHA: LOOP DO SISTEMA DE BATALHA ================================================
    if c_opcao == 1 or apanhado:
        vida_monstro = c_vida_gerada
        while vida_monstro != 0 or personagem.vida != 0:
            dado_jogador = jogar_dado(6)
            dado_monstro = jogar_dado(c_max_dado) + (((personagem.ataque + personagem.defesa) // 2) - 1)
# ------------------------------ BATALHA: BREAK SE O JOGADOR MORRER ----------------------------------------------------
            if personagem.vida <= 0:
                break
# ------------------------------ BATALHA: BREAK SE O JOGADOR VENCER ----------------------------------------------------
            if vida_monstro <= 0:
                # ======================== EXPERIENCIA E DROPS =========================================================
                print(f'\nVocê derrotou {c_monstro} e ganhou ' + cs(f'{c_xp_monstro} pontos de XP!', 'yellow'))
                personagem.derrotar()
                personagem.ganhar_xp(c_xp_monstro)
                if personagem.experiencia >= 100:
                    personagem.subir_nivel()
                    print(cs('\n††††† Você subiu um nivel, sua vida foi restaurada! ††††', '#FFFF00').bold())
                premio = randint(1, 100)
                if premio in range(c_chance_premio, 100):
                    item = items.gera_item()
                    print(cs(f'\nVocê encontrou um(a) {item.nome}!', 'pink').bold())
                    personagem.adicionar_na_mochila(item)
                    personagem.coletar()
                    if isinstance(item, items.Ataque):
                        personagem.aumenta_ataque(1)
                    else:
                        personagem.aumenta_defesa(1)
                if premio in range(1, c_chance_pocao):
                    quantidade = randint(1, 3)
                    personagem.ganhar_pocao(quantidade)
                    if quantidade == 1:
                        print(cs(f'\nVocê encontrou {quantidade} POT!', 'blue').bold())
                    else:
                        print(cs(f'\nVocê encontrou {quantidade} POTS!', 'blue').bold())
                break
# =================================== BATALHA: SISTEMA DE COMBATE ======================================================
            print(f'\nVocê rolou {dado_jogador} no dado! '
                  f'(ATK: {dado_jogador + personagem.ataque} / DEF: {dado_jogador + personagem.defesa})\n'
                  f'{c_monstro} rolou {dado_monstro} no dado!\n')
# ------------------------------------- CHECA SE O JOGADOR DEU DANO ----------------------------------------------------
            if (dado_jogador + personagem.ataque) > dado_monstro:
                vida_monstro -= (dado_jogador - dado_monstro) + personagem.ataque
                print(cs(f'>>> Você deu um dano de {(dado_jogador - dado_monstro) + personagem.ataque} '
                         f'em {c_monstro}\n', '#7CFC00').bold() +
                      bold(f'>>> Vida de {c_monstro}: {vida_monstro}'))
# ------------------------------------- CHECA SE O JOGADOR RECEBEU DANO ------------------------------------------------
            if (dado_jogador + personagem.defesa) < dado_monstro:
                personagem.receber_dano((dado_monstro - (dado_jogador + personagem.defesa)))
                print(cs(f'>>> Você recebeu {dado_monstro - (dado_jogador + personagem.defesa)} '
                         f'de dano\n', 'red').bold() +
                      bold(f'>>> Sua vida: {personagem.vida}'))
# ------------------------------------- CHECA SE A CRIATURA DEFENDEU ---------------------------------------------------
            if (dado_jogador + personagem.ataque) <= dado_monstro:
                print(cs(f'{c_monstro} defendeu seu ataque!', 'yellow'))
# --------------------------------------- CHECA SE O JOGADOR DEFENDEU --------------------------------------------------
            if (dado_jogador + personagem.defesa) >= dado_monstro:
                print(cs(f'Você defendeu o ataque de {c_monstro}!', 'yellow'))
# --------------------------------- ESPERA O INPUT PARA O PROXIMO TURNO ------------------------------------------------
            input('\n' + cs('----- Aperte ENTER para ir para o próximo TURNO! ------', '#BDB76B'))


def gerar_desafio():
    # ================================== TENTA GERAR VARIAVEIS CRIATURA ================================================
    try:
        gd_locais, gd_monstros, gd_max_dado, gd_vida_gerada, gd_xp_monstro, gd_chance_premio, gd_chance_pocao = \
            [x for x in dificuldade()]
    # ======================================= CASO FALHE GERA EMBOSCADA ================================================
    except TypeError:
        emb = choice(['Slime', 'Troll', 'Orc'])
        print('\n' +
              cs('############## EMBOSCADA! ##############', 'red') + '\n' +
              f'>>> UM ' + cs(f'{emb.upper()}', 'red') + ' APARECEU! <<<')
        checa_opcao(1, emb, 7, 12, 30, 70, 25)
    # =========================================== CHECA SE JOGADOR AINDA ESTÁ VIVO =====================================
    if personagem.vida > 0:
        # ================================ CASO SIM GERA VARIAVEIS (CRIATURA ESPECIAL) =================================
        try:
            monstro = choice(gd_monstros)
        except UnboundLocalError:
            monstro = choice(['Ladrão', 'Bandido', 'Orc Lider', 'Guerreiro Amaldiçoado', 'Beholder'])
        try:
            local = choice(gd_locais)
        except UnboundLocalError:
            local = choice(['pântano', 'buraco', 'desfiladeiro'])
        try:
            opcao = opcoes(local, monstro)
        except UnboundLocalError:
            opcao = 1
            # ================================== GERA DESAFIO/CRIATURA =================================================
        try:
            checa_opcao(opcao, monstro, gd_max_dado, gd_vida_gerada, gd_xp_monstro, gd_chance_premio, gd_chance_pocao)
        except:
            checa_opcao(opcao, monstro, 8, 15, 40, 70, 25)